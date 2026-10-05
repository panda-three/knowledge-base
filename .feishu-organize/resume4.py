#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补移 v3：burst 模式。每轮最多 6 次成功（间隔60s），遇失败立即停轮；
轮间冷却 25 分钟；失败项进入下一轮重试。直到全部完成或轮次用尽。"""
import json, subprocess, time, os, sys

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
BASE = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY",
        "lark-cli", "wiki"]
BURST = 5
GAP = 60
SLEEP_ROUND = 900    # 15 min
SLEEP_FAIL = 1200    # 20 min
MAX_ROUNDS = 12

def run_move(node_token, target):
    cmd = BASE + ["+move", "--node-token", node_token, "--target-parent-token", target,
                  "--as", "user", "--format", "json"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    try:
        d = json.loads(r.stdout)
        if d.get("ok"):
            return True, "ok"
        return False, (r.stdout or r.stderr)[:200]
    except Exception:
        return False, (r.stdout or r.stderr)[:200]

def journal(title, ok, detail, node_token=""):
    with open(os.path.join(DIR, "execution_journal.jsonl"), "a") as f:
        f.write(json.dumps({"t": time.time(), "kind": "move", "title": title, "ok": ok,
                            "node_token": node_token, "detail": detail}, ensure_ascii=False) + "\n")

def list_nodes(parent=None):
    args = (["+node-list", "--space-id", SPACE, "--parent-node-token", parent] if parent
            else ["+node-list", "--space-id", SPACE]) + ["--as", "user", "--page-all", "--format", "json"]
    d, _ = run_raw(args)
    if d and d.get("ok"): return d["data"]["nodes"]
    return []

def run_raw(args):
    cmd = BASE + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return json.loads(r.stdout), None
    except Exception:
        return None, None

# 解析目标目录 token
plan = json.load(open(os.path.join(DIR, "plan.json")))
moves = plan["moves"]
root = list_nodes()
pt = {n["title"]: n["node_token"] for n in root if n["title"] in
      ["01-课程成品","02-学习笔记","03-方法论与SOP","04-资料归档","05-待整理"]}
series = {}
if "02-学习笔记" in pt:
    for n in list_nodes(pt["02-学习笔记"]):
        series[n["title"]] = n["node_token"]
def resolve(target):
    if "/" in target:
        return series.get(target.split("/", 1)[1])
    return pt.get(target)

# 当前仍在根（先从飞书重扫，避免用旧 actual_map）
by_token = {m["node_token"]: m for m in moves}
root_now = {n["node_token"] for n in list_nodes()}
pending = [by_token[t] for t in root_now if t in by_token]
# 按计划顺序排序
order = {m["node_token"]: i for i, m in enumerate(moves)}
pending.sort(key=lambda m: order[m["node_token"]])
print(f"[RESUME3] 待补移 {len(pending)} 项，首轮先探测 1 项校准限流", flush=True)

def one_round(remaining):
    """一轮：最多 BURST 次成功；遇失败立即返回剩余项。返回 (done_titles, still_remaining)"""
    still = []
    succ = 0
    for m in remaining:
        tgt = resolve(m["target"])
        if not tgt:
            journal(m["title"], False, "no target token")
            still.append(m); continue
        ok, detail = run_move(m["node_token"], tgt)
        if ok:
            succ += 1
            journal(m["title"], True, "ok(resume3)")
            print(f"[OK] {m['title'][:28]} (本轮第{succ}次)", flush=True)
        else:
            journal(m["title"], False, f"resume3 fail: {detail}")
            print(f"[FAIL] {m['title'][:28]} | {detail[:60]}", flush=True)
            still.append(m)
            time.sleep(SLEEP_FAIL)  # 失败后长冷却
            return still  # 立即停轮
        if succ >= BURST:
            return still
        time.sleep(GAP)
    return still

round_no = 1
while pending and round_no <= MAX_ROUNDS:
    print(f"===== 第 {round_no} 轮开始（剩余 {len(pending)} 项） =====", flush=True)
    pending = one_round(pending)
    if pending:
        print(f"第 {round_no} 轮结束：剩余 {len(pending)} 项，冷却 {SLEEP_ROUND//60} 分钟后继续", flush=True)
        time.sleep(SLEEP_ROUND)
    round_no += 1

json.dump({"rounds_used": round_no-1, "remaining": [m["title"] for m in pending]},
          open(os.path.join(DIR, "resume3_result.json"), "w"), ensure_ascii=False, indent=1)
if pending:
    print(f"[RESUME3 结束] 仍有 {len(pending)} 项未完成：", flush=True)
    for m in pending: print("  -", m["title"], flush=True)
else:
    print("[RESUME3 完成] 全部 37 项已移动", flush=True)
