#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""整理后验证：回读根节点 + 各目标目录子节点，对比计划，输出实际落位。只读。"""
import json, subprocess, time, os

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
ENV = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY"]
CLI = ["lark-cli", "wiki", "+node-list", "--space-id", SPACE, "--as", "user", "--page-all", "--format", "json"]

def list_nodes(parent=None):
    cmd = ENV + CLI
    if parent: cmd += ["--parent-node-token", parent]
    for attempt in range(3):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        try:
            d = json.loads(r.stdout)
            if d.get("ok"): return d.get("data", {}).get("nodes", [])
        except Exception: pass
        time.sleep(15)
    return None

root = list_nodes()
assert root is not None, "root list failed"
print("root nodes:", len(root))

# 找到 16 个目标目录/节点
folders = {n["title"]: n for n in root if n.get("has_child") or n["title"] == "00-首页导航"}
top = {}
for t in ["01-课程成品","02-学习笔记","03-方法论与SOP","04-资料归档","05-待整理"]:
    n = folders.get(t)
    if n: top[t] = n
print("顶层目录找到:", {k: bool(v) for k, v in top.items()})

# 02-学习笔记 的子目录
series = {}
if "02-学习笔记" in top:
    kids = list_nodes(top["02-学习笔记"]["node_token"])
    if kids:
        for k in kids:
            series[k["title"]] = k
print("系列目录数:", len(series), sorted(series.keys()))

# 各目录的子节点 → actual_map: node_token -> (container_title)
actual = {}   # token -> path string
for t, n in top.items():
    for k in list_nodes(n["node_token"]) or []:
        actual[k["node_token"]] = t + "/" + k["title"]
for t, n in series.items():
    for k in list_nodes(n["node_token"]) or []:
        actual[k["node_token"]] = "02-学习笔记/" + t + "/" + k["title"]
for n in root:
    if n["node_token"] not in actual:
        actual[n["node_token"]] = "/" + n["title"]   # 仍在根

json.dump(actual, open(os.path.join(DIR, "actual_map.json"), "w"), ensure_ascii=False, indent=1)

# 对比计划
plan = json.load(open(os.path.join(DIR, "plan.json")))
moves = plan["moves"]
still_root, wrong, ok = [], [], 0
for m in moves:
    loc = actual.get(m["node_token"], "?")
    if loc == "/" + m["title"]:
        still_root.append(m["title"])
    elif loc.startswith(m["target"]):
        ok += 1
    else:
        wrong.append((m["title"], m["target"], loc))
print("\n=== 对比结果 ===")
print("已正确移动:", ok, "/", len(moves))
print("仍在根(需补移):", len(still_root))
for t in still_root: print("  -", t)
print("位置不符:", len(wrong))
for t, exp, got in wrong: print("  -", t, "| 预期:", exp, "| 实际:", got)
