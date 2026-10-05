#!/usr/bin/env python3
"""递归枚举飞书 wiki 全树，产出完整节点清单 JSON。"""
import json, subprocess, sys, time, os

SPACE_ID = "7669431379494440158"
OUT_DIR = "/Users/panda/Desktop/knowledge-base/00-天一生水/01-系统文档/AI教育课沉淀/meta"
ENV_PREFIX = ["env", "-u", "http_proxy", "-u", "https_proxy", "-u", "HTTP_PROXY", "-u", "HTTPS_PROXY"]

def run_lark(args):
    cmd = ENV_PREFIX + ["lark-cli"] + args
    for attempt in range(3):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if r.returncode == 0:
                data = json.loads(r.stdout)
                if data.get("ok"):
                    return data
            time.sleep(1 * (attempt + 1))
        except Exception as e:
            print(f"  retry {attempt+1}: {e}", file=sys.stderr)
            time.sleep(2)
    print(f"  FAILED: {' '.join(args)}", file=sys.stderr)
    return None

def list_nodes(parent_token=None):
    args = ["wiki", "+node-list", "--space-id", SPACE_ID, "--as", "user",
            "--page-all", "--page-limit", "20", "--format", "json"]
    if parent_token:
        args += ["--parent-node-token", parent_token]
    data = run_lark(args)
    if data and "data" in data:
        return data["data"].get("nodes", [])
    return []

all_nodes = []
seen_obj_tokens = set()

def walk(parent_token=None, path=""):
    nodes = list_nodes(parent_token)
    for n in nodes:
        obj_token = n.get("obj_token", "")
        title = n.get("title", "")
        node_token = n.get("node_token", "")
        has_child = n.get("has_child", False)
        obj_type = n.get("obj_type", "")
        full_path = f"{path}/{title}" if path else title
        
        # 按 obj_token 去重（树内存在重复节点）
        if obj_token in seen_obj_tokens:
            print(f"  DUP skip: {full_path} ({obj_token})", file=sys.stderr)
            continue
        seen_obj_tokens.add(obj_token)
        
        entry = {
            "obj_token": obj_token,
            "node_token": node_token,
            "title": title,
            "obj_type": obj_type,
            "has_child": has_child,
            "path": full_path,
            "parent_node_token": parent_token or "",
        }
        all_nodes.append(entry)
        print(f"  [{len(all_nodes)}] {full_path} ({obj_type}, child={has_child})")
        
        if has_child:
            time.sleep(0.3)
            walk(node_token, full_path)

print("=== 开始枚举全树 ===")
walk()
print(f"\n=== 枚举完成：共 {len(all_nodes)} 个唯一节点 ===")

# 保存全量节点
with open(os.path.join(OUT_DIR, "all_nodes.json"), "w", encoding="utf-8") as f:
    json.dump(all_nodes, f, ensure_ascii=False, indent=2)

# 筛选叶子节点（has_child=false 且 obj_type != slides 的需要抓取）
leaf_docs = [n for n in all_nodes if not n["has_child"] and n["obj_type"] in ("docx", "file", "markdown")]
leaf_slides = [n for n in all_nodes if not n["has_child"] and n["obj_type"] == "slides"]
containers = [n for n in all_nodes if n["has_child"]]

print(f"叶子文档(待抓取): {len(leaf_docs)}")
print(f"叶子slides(跳过): {len(leaf_slides)}")
print(f"容器目录: {len(containers)}")

with open(os.path.join(OUT_DIR, "leaf_docs.json"), "w", encoding="utf-8") as f:
    json.dump(leaf_docs, f, ensure_ascii=False, indent=2)
with open(os.path.join(OUT_DIR, "leaf_slides.json"), "w", encoding="utf-8") as f:
    json.dump(leaf_slides, f, ensure_ascii=False, indent=2)

print(f"\n清单已保存到 {OUT_DIR}/")
