#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用原生 POST API 批量移动剩余节点（绕过 +move 封装的 Content-Type 误判）。
响应保存到 download.txt 后解析 code。"""
import json, subprocess, time, os, glob

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
DL = os.path.join(DIR, "download.txt")
BASE = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY",
        "lark-cli"]

def run_raw(args):
    r = subprocess.run(BASE + args, capture_output=True, text=True, timeout=90)
    return r

def node_list(parent=None):
    args = ["wiki", "+node-list", "--space-id", SPACE, "--as", "user", "--page-all", "--format", "json"]
    if parent: args = ["wiki", "+node-list", "--space-id", SPACE, "--parent-node-token", parent,
                       "--as", "user", "--page-all", "--format", "json"]
    r = run_raw(args)
    try:
        d = json.loads(r.stdout)
        if d.get("ok"): return d["data"]["nodes"]
    except Exception: pass
    return []

def move_node(node_token, target_token):
    """返回 (ok, detail)"""
    if os.path.exists(DL): os.remove(DL)
    url = f"/open-apis/wiki/v2/spaces/{SPACE}/nodes/{node_token}/move"
    r = run_raw(["api", "POST", url, "--data", json.dumps({"target_parent_token": target_token}),
                 "--as", "user", "--format", "json"])
    out = r.stdout
    # 响应可能被存到文件
    if "saved_path" in out:
        try:
            meta = json.loads(out)
            with open(meta["saved_path"], "r") as f:
                content = f.read().strip()
            d = json.loads(content)
            if d.get("code") == 0:
                return True, "code:0 success"
            return False, content[:200]
        except Exception as e:
            return False, f"parse fail: {out[:200]} {e}"
    try:
        d = json.loads(out)
        if d.get("ok") and d.get("data", {}).get("node", {}).get("parent_node_token") == target_token:
            return True, "ok"
        return False, out[:200]
    except Exception:
        return False, out[:200]

def journal(title, ok, detail, node_token=""):
    with open(os.path.join(DIR, "execution_journal.jsonl"), "a") as f:
        f.write(json.dumps({"t": time.time(), "kind": "move_api", "title": title, "ok": ok,
                            "node_token": node_token, "detail": detail}, ensure_ascii=False) + "\n")

# 1. 解析目标 token
root = node_list()
pt = {n["title"]: n["node_token"] for n in root if n["title"] in
      ["01-课程成品","02-学习笔记","03-方法论与SOP","04-资料归档","05-待整理"]}
series = {}
if "02-学习笔记" in pt:
    for n in node_list(pt["02-学习笔记"]):
        series[n["title"]] = n["node_token"]
def resolve(target):
    if "/" in target:
        return series.get(target.split("/", 1)[1])
    return pt.get(target)

# 2. 找仍在根的节点（重扫根层）
plan = json.load(open(os.path.join(DIR, "plan.json")))
by_token = {m["node_token"]: m for m in plan["moves"]}
root_now = {n["node_token"] for n in node_list()}
pending = [by_token[t] for t in root_now if t in by_token]
order = {m["node_token"]: i for i, m in enumerate(plan["moves"])}
pending.sort(key=lambda m: order[m["node_token"]])
print(f"[BATCH-API] 待移动 {len(pending)} 项", flush=True)

ok_list, fail_list = [], []
for i, m in enumerate(pending, 1):
    tgt = resolve(m["target"])
    if not tgt:
        fail_list.append((m["title"], "no target token")); continue
    ok, detail = move_node(m["node_token"], tgt)
    if ok:
        ok_list.append(m["title"])
        journal(m["title"], True, f"api ok: {detail}", m["node_token"])
        print(f"[OK {i}/{len(pending)}] {m['title'][:30]}", flush=True)
    else:
        # 失败：冷却 60 秒重试一次
        journal(m["title"], False, f"api fail: {detail}", m["node_token"])
        print(f"[FAIL {i}/{len(pending)}] {m['title'][:30]} | {detail[:60]}", flush=True)
        time.sleep(60)
        ok2, detail2 = move_node(m["node_token"], tgt)
        if ok2:
            ok_list.append(m["title"])
            journal(m["title"], True, f"api ok(retry): {detail2}", m["node_token"])
            print(f"[RETRY-OK] {m['title'][:30]}", flush=True)
        else:
            fail_list.append((m["title"], detail2))
            journal(m["title"], False, f"api fail retry: {detail2}", m["node_token"])
    time.sleep(3)

json.dump({"ok": ok_list, "failed": fail_list},
          open(os.path.join(DIR, "batch_api_result.json"), "w"), ensure_ascii=False, indent=1)
print(f"\n[BATCH-API 完成] 成功 {len(ok_list)}/{len(pending)}", flush=True)
for t, why in fail_list: print("  -", t, "|", why[:80], flush=True)
