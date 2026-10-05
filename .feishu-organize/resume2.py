#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补移 v2：超保守节奏。间隔30s，每6成功暂停300s，失败先冷却300s再重试1次（最多2次），记录真实报错。"""
import json, subprocess, time, os

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
BASE = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY",
        "lark-cli", "wiki"]

def run_raw(args):
    cmd = BASE + args + ["--as", "user", "--format", "json"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    try:
        d = json.loads(r.stdout)
        return d, None
    except Exception:
        return None, (r.stdout or r.stderr)[:300]

def journal(title, ok, detail, node_token=""):
    with open(os.path.join(DIR, "execution_journal.jsonl"), "a") as f:
        f.write(json.dumps({"t": time.time(), "kind": "move", "title": title, "ok": ok,
                            "node_token": node_token, "detail": detail}, ensure_ascii=False) + "\n")

def list_nodes(parent=None):
    args = ["+node-list", "--space-id", SPACE, "--parent-node-token", parent,
            "--as", "user", "--page-all", "--format", "json"] if parent else \
           ["+node-list", "--space-id", SPACE, "--as", "user", "--page-all", "--format", "json"]
    d, err = run_raw(args)
    if d and d.get("ok"): return d["data"]["nodes"]
    return []

plan = json.load(open(os.path.join(DIR, "plan.json")))
actual = json.load(open(os.path.join(DIR, "actual_map.json")))
moves = plan["moves"]

root = list_nodes()
pt = {}
for n in root:
    if n["title"] in ["01-课程成品","02-学习笔记","03-方法论与SOP","04-资料归档","05-待整理"]:
        pt[n["title"]] = n["node_token"]
series = {}
if "02-学习笔记" in pt:
    for n in list_nodes(pt["02-学习笔记"]):
        series[n["title"]] = n["node_token"]
def resolve(target):
    if "/" in target:
        return series.get(target.split("/", 1)[1])
    return pt.get(target)

pending = [m for m in moves if actual.get(m["node_token"], "?").startswith("/")]
print(f"[RESUME2] 待补移 {len(pending)} 项", flush=True)

ok_cnt, fail_list, consec = 0, [], 0
for i, m in enumerate(pending, 1):
    tgt = resolve(m["target"])
    if not tgt:
        journal(m["title"], False, "no target token")
        fail_list.append((m["title"], "no target token")); continue
    moved = False
    last_err = ""
    for attempt in range(2):
        d, err = run_raw(["+move", "--node-token", m["node_token"], "--target-parent-token", tgt])
        if d is not None and d.get("ok"):
            moved = True; last_err = "ok"; break
        last_err = (err or json.dumps(d, ensure_ascii=False))[:200]
        time.sleep(300)  # 失败先冷却5分钟
    if moved:
        ok_cnt += 1; consec += 1
        journal(m["title"], True, "ok(resume2)")
        time.sleep(30)
        if consec % 6 == 0:
            print(f"[PAUSE] 已成功 {ok_cnt}，暂停300s", flush=True)
            time.sleep(300)
    else:
        journal(m["title"], False, f"resume2 failed: {last_err}")
        fail_list.append((m["title"], last_err))
        print(f"[FAIL] {m['title']} | {last_err[:80]}", flush=True)
        time.sleep(30)
    if i % 8 == 0 or i == len(pending):
        print(f"[PROGRESS] 补移成功 {ok_cnt}/{len(pending)}，失败 {len(fail_list)}", flush=True)

json.dump({"resume2_ok": ok_cnt, "failed": fail_list},
          open(os.path.join(DIR, "resume2_result.json"), "w"), ensure_ascii=False, indent=1)
print(f"[RESUME2 DONE] 成功 {ok_cnt}/{len(pending)}，失败 {len(fail_list)}", flush=True)
for t, why in fail_list: print("  -", t, "|", why[:100], flush=True)
