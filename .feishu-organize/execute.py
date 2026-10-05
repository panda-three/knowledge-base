#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI教育课知识库整理：执行创建+移动（完整计划 100 项）。内部维护 journal 与 rollback_snapshot。"""
import json, subprocess, time, sys, os

SPACE = "7669431379494440158"
DIR = "/Users/panda/Desktop/knowledge-base/.feishu-organize"
BASE = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY",
        "lark-cli", "wiki"]

journal_path = os.path.join(DIR, "execution_journal.jsonl")
snap_path = os.path.join(DIR, "rollback_snapshot.json")

def run(args, retries=2, wait=2.0):
    cmd = BASE + args + ["--as", "user", "--format", "json"]
    last = None
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        except Exception as e:
            last = f"run error {e}"; time.sleep(wait); continue
        if r.returncode != 0:
            last = f"rc={r.returncode} {r.stderr[:200]}"; time.sleep(wait); continue
        try:
            d = json.loads(r.stdout)
        except Exception:
            last = f"parse error: {r.stdout[:200]}"; time.sleep(wait); continue
        if d.get("ok"):
            return d, None
        s = json.dumps(d, ensure_ascii=False)
        last = s[:300]
        if any(k in s for k in ["rate_limit", "限流", "invalid_", "internal", "too many"]):
            time.sleep(30); continue
        return d, last
    return None, last

def journal(kind, title, ok, detail, node_token=""):
    with open(journal_path, "a") as f:
        f.write(json.dumps({"t": time.time(), "kind": kind, "title": title, "ok": ok,
                            "node_token": node_token, "detail": detail}, ensure_ascii=False) + "\n")

def create_node(title, parent=None):
    args = ["+node-create", "--space-id", SPACE, "--title", title]
    if parent:
        args += ["--parent-node-token", parent]
    d, err = run(args)
    if err or d is None:
        journal("create", title, False, err)
        return None
    tok = d["data"].get("node_token", "")
    journal("create", title, True, "ok", tok)
    return tok

def move_node(node_token, title, parent_token):
    d, err = run(["+move", "--node-token", node_token, "--target-parent-token", parent_token])
    if err or d is None:
        journal("move", title, False, err, node_token)
        return False
    journal("move", title, True, "ok", node_token)
    return True

# ---------- 加载计划 ----------
plan = json.load(open(os.path.join(DIR, "plan.json")))
creates, moves = plan["creates"], plan["moves"]
total = len(creates) + len(moves)
print(f"[START] 执行开始：创建 {len(creates)} 项 + 移动 {len(moves)} 项 = {total} 项", flush=True)

# 先建 rollback_snapshot（所有源节点当前都在空间根）
snap = {"space_id": SPACE, "items": [{"title": m["title"], "node_token": m["node_token"],
        "obj_token": m["obj_token"], "origin": "wiki_space_root", "space_id": SPACE} for m in moves]}
json.dump(snap, open(snap_path, "w"), ensure_ascii=False, indent=1)

path_tokens = {"/": ""}   # 目标路径 -> node_token
op_count = 0
def pace(kind="op"):
    global op_count
    op_count += 1
    time.sleep(2.0)
    if op_count % 15 == 0:
        time.sleep(40)   # 限流窗口重置
    if op_count % 20 == 0:
        print(f"[PROGRESS] 已执行 {op_count}/{total} 项操作", flush=True)

# ---------- 1. 创建（浅到深） ----------
# 根层：00 节点 + 5 顶层目录
created_ok = 0
tok = create_node("00-首页导航")
if tok: path_tokens["00-首页导航"] = tok; created_ok += 1
pace()
for t in ["01-课程成品", "02-学习笔记", "03-方法论与SOP", "04-资料归档", "05-待整理"]:
    tok = create_node(t)
    if tok: path_tokens[t] = tok; created_ok += 1
    pace()
# 02 下 10 个系列目录
parent02 = path_tokens.get("02-学习笔记", "")
for s in ["01-AI双三角","02-一堂五步法","03-调研方法论","04-产品与验证","05-领导力",
          "06-泛产品设计","07-个人成长","08-AI技能与创作","09-AI应用与场景","10-其他课程"]:
    tok = create_node(s, parent02)
    if tok: path_tokens[f"02-学习笔记/{s}"] = tok; created_ok += 1
    pace()
print(f"[CREATE DONE] 创建成功 {created_ok}/{len(creates)}", flush=True)

# ---------- 2. 移动 ----------
moved_ok, moved_fail = 0, []
for m in moves:
    tgt = path_tokens.get(m["target"])
    if not tgt:
        moved_fail.append((m["title"], "目标目录 token 缺失"))
        journal("move", m["title"], False, "no target token", m["node_token"])
        pace(); continue
    ok = move_node(m["node_token"], m["title"], tgt)
    if ok: moved_ok += 1
    else: moved_fail.append((m["title"], "move 失败"))
    pace()

print(f"[MOVE DONE] 移动成功 {moved_ok}/{len(moves)}", flush=True)
if moved_fail:
    print("[FAILED]", json.dumps(moved_fail, ensure_ascii=False), flush=True)
# 汇总结果
json.dump({"creates_ok": created_ok, "moves_ok": moved_ok, "failed": moved_fail},
          open(os.path.join(DIR, "execution_result.json"), "w"), ensure_ascii=False, indent=1)
print("[DONE]", flush=True)
