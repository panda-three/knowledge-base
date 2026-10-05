#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补移 55 个仍留在根层的节点（限流后稳跑版）。间隔10s，每12成功暂停150s，失败退避300s重试。"""
import json, subprocess, time, os

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
BASE = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY",
        "lark-cli", "wiki"]

def run_raw(args):
    cmd = BASE + args + ["--as", "user", "--format", "json"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    try:
        return json.loads(r.stdout), None
    except Exception:
        return None, r.stdout[:200]

def journal(kind, title, ok, detail, node_token=""):
    with open(os.path.join(DIR, "execution_journal.jsonl"), "a") as f:
        f.write(json.dumps({"t": time.time(), "kind": kind, "title": title, "ok": ok,
                            "node_token": node_token, "detail": detail}, ensure_ascii=False) + "\n")

# ---------- 重新解析目标目录 token ----------
plan = json.load(open(os.path.join(DIR, "plan.json")))
actual = json.load(open(os.path.join(DIR, "actual_map.json")))
moves = plan["moves"]

def list_nodes(parent=None):
    args = ["+node-list", "--space-id", SPACE, "--as", "user", "--page-all", "--format", "json"]
    if parent: args = ["+node-list", "--space-id", SPACE, "--parent-node-token", parent, "--as", "user", "--page-all", "--format", "json"]
    d, err = run_raw(args)
    if d and d.get("ok"): return d["data"]["nodes"]
    return []

# 找顶层目录
root = list_nodes()
pt = {}
for n in root:
    if n["title"] in ["01-课程成品","02-学习笔记","03-方法论与SOP","04-资料归档","05-待整理"]:
        pt[n["title"]] = n["node_token"]
# 找系列目录
series = {}
if "02-学习笔记" in pt:
    for n in list_nodes(pt["02-学习笔记"]):
        series[n["title"]] = n["node_token"]
def resolve(target):
    if "/" in target:
        top, sub = target.split("/", 1)
        return series.get(sub)
    return pt.get(target)

# 待补移列表（仍在根）
pending = [m for m in moves if actual.get(m["node_token"], "?").startswith("/")]
print(f"[RESUME] 待补移 {len(pending)} 项", flush=True)

ok_cnt, fail_list = 0, []
consec = 0
for i, m in enumerate(pending, 1):
    tgt = resolve(m["target"])
    if not tgt:
        print(f"[SKIP] {m['title']}: 目标目录 token 缺失", flush=True)
        fail_list.append((m["title"], "no target token")); continue
    moved = False
    for attempt in range(3):
        d, err = run_raw(["+move", "--node-token", m["node_token"], "--target-parent-token", tgt])
        if d is not None and d.get("ok"):
            moved = True; break
        # 限流/瞬态：退避
        time.sleep(60 if attempt == 0 else 300)
    if moved:
        ok_cnt += 1; consec += 1
        journal("move", m["title"], True, "ok(resume)", m["node_token"])
        time.sleep(10)
        if consec % 12 == 0:
            print(f"[PAUSE] 已成功 {ok_cnt}，暂停150s重置限流", flush=True)
            time.sleep(150)
    else:
        journal("move", m["title"], False, "resume failed", m["node_token"])
        fail_list.append((m["title"], "resume failed"))
        print(f"[FAIL] {m['title']}", flush=True)
        time.sleep(10)
    if i % 10 == 0 or i == len(pending):
        print(f"[PROGRESS] 补移 {ok_cnt}/{len(pending)} 成功，失败 {len(fail_list)}", flush=True)

json.dump({"resume_ok": ok_cnt, "failed": fail_list}, open(os.path.join(DIR, "resume_result.json"), "w"), ensure_ascii=False, indent=1)
print(f"[RESUME DONE] 成功 {ok_cnt}/{len(pending)}，失败 {len(fail_list)}", flush=True)
for t, why in fail_list: print("  -", t, why, flush=True)
