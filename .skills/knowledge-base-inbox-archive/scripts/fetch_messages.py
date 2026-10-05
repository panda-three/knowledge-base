#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_messages.py — 拉取「知识库输入」飞书群消息（确定性步骤）

用途：知识库输入归档流水线的第 1 步。调用 lark-cli im +chat-messages-list 拉取
飞书「知识库输入」群消息，自动绕过本地代理（127.0.0.1:7890 未开启时会
proxyconnect connection refused），输出结构化消息列表供后续分拣。

用法：
    python3 fetch_messages.py                 # 默认拉最近 30 条
    python3 fetch_messages.py --limit 50      # 指定条数
    python3 fetch_messages.py --chat-id oc_xxx  # 指定群

依赖：lark-cli 已安装且已认证（user 身份）。
"""
import argparse
import json
import os
import subprocess
import sys

# 「知识库输入」群默认 chat_id
DEFAULT_CHAT_ID = "oc_0177ac80245e12edd6c959ef0becf45b"
# 本地代理变量（未开启时会阻塞 API 调用，需移除）
PROXY_ENV_KEYS = ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY",
                  "all_proxy", "ALL_PROXY"]


def run_lark_cli(chat_id: str, limit: int) -> dict:
    """绕过代理调用 lark-cli，返回解析后的 JSON。"""
    env = {k: v for k, v in os.environ.items() if k not in PROXY_ENV_KEYS}
    cmd = [
        "lark-cli", "im", "+chat-messages-list",
        "--chat-id", chat_id,
        "--page-limit", str(limit),
        "--page-size", "50",
        "--order", "desc",
        "--format", "json",
    ]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(f"lark-cli 调用失败 rc={proc.returncode}: {proc.stderr[:800]}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"lark-cli 输出非 JSON: {proc.stdout[:800]}") from e


def main() -> int:
    parser = argparse.ArgumentParser(description="拉取知识库输入群消息")
    parser.add_argument("--chat-id", default=DEFAULT_CHAT_ID)
    parser.add_argument("--limit", type=int, default=30, help="返回消息条数上限")
    parser.add_argument("--json", action="store_true", help="输出原始 JSON")
    args = parser.parse_args()

    data = run_lark_cli(args.chat_id, args.limit)
    if not data.get("ok"):
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 1

    if args.json:
        print(json.dumps(data["data"], ensure_ascii=False, indent=2))
        return 0

    msgs = data["data"].get("messages", [])
    print(f"群内消息总数(返回): {len(msgs)}  has_more: {data['data'].get('has_more', False)}")
    for m in reversed(msgs):
        print("---")
        print(f"time: {m.get('create_time')} | type: {m.get('msg_type')}")
        print(f"sender: {(m.get('sender') or {}).get('name')}")
        print(f"msg_id: {m.get('message_id')}")
        print(f"content: {str(m.get('content', ''))[:500]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
