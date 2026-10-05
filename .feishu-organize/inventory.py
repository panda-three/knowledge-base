#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI教育课 知识库全量盘点（只读）：根节点 + 所有子节点，输出 inventory.json"""
import json, subprocess, time, sys

SPACE = "7669431379494440158"
OUT = "/Users/panda/Desktop/knowledge-base/.feishu-organize/inventory.json"
ENV = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY"]
CLI = ["lark-cli", "wiki", "+node-list", "--space-id", SPACE, "--as", "user", "--page-all", "--format", "json"]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return None, r.stderr[:300]
    return r.stdout, None

def list_nodes(parent=None):
    cmd = ENV + CLI
    if parent:
        cmd += ["--parent-node-token", parent]
    out, err = run(cmd)
    if out is None:
        return None, err
    try:
        d = json.loads(out)
        return d.get("data", {}).get("nodes", []), None
    except Exception as e:
        return None, f"parse error: {e} | {out[:200]}"

def norm(n):
    return {
        "title": n.get("title", ""),
        "type": n.get("obj_type", ""),
        "node_token": n.get("node_token", ""),
        "obj_token": n.get("obj_token", ""),
        "has_child": n.get("has_child", False),
        "parent": n.get("parent_node_token", ""),
    }

inv = {"space_id": SPACE, "root": [], "children": {}}

root, err = list_nodes()
if root is None:
    print("ROOT FAIL:", err); sys.exit(1)
for n in root:
    item = norm(n)
    inv["root"].append(item)
    if n.get("has_child"):
        time.sleep(0.4)
        kids, kerr = list_nodes(n["node_token"])
        if kids is None:
            print("CHILD FAIL", n["title"], kerr)
            inv["children"][n["node_token"]] = []
        else:
            inv["children"][n["node_token"]] = [norm(k) for k in kids]
        print(f"[{len(inv['children'][n['node_token']]):>2}] {n['title']}", flush=True)

json.dump(inv, open(OUT, "w"), ensure_ascii=False, indent=1)
total_children = sum(len(v) for v in inv["children"].values())
print("=== SUMMARY ===")
print("root:", len(inv["root"]), "| folders:", len(inv["children"]), "| children:", total_children)
