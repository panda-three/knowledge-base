#!/usr/bin/env python3
"""给48篇已覆盖对应的8个本地笔记补写 YAML source 字段。"""
import json, os, re
from collections import defaultdict

BASE = "/Users/panda/Desktop/knowledge-base"
META = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/meta")

with open(os.path.join(META, "classification.json"), encoding="utf-8") as f:
    results = json.load(f)

covered = [r for r in results if r["status"] == "已覆盖"]

# 按本地文件分组
by_local = defaultdict(list)
for r in covered:
    by_local[r["local_path"]].append(r)

print(f"已覆盖 {len(covered)} 篇 → {len(by_local)} 个本地文件")

for local_path, docs in by_local.items():
    if not os.path.exists(local_path):
        print(f"  SKIP (not found): {local_path}")
        continue
    
    with open(local_path, encoding="utf-8") as f:
        content = f.read()
    
    # 检查是否已有 source 字段
    if re.search(r'^source:', content, re.MULTILINE):
        print(f"  SKIP (has source): {os.path.basename(local_path)}")
        continue
    
    # 构建 source 字段
    if len(docs) == 1:
        d = docs[0]
        source_line = f"source: {d['wiki_link']}（飞书 AI教育课 · {d['title']}）"
    else:
        lines = ["source:"]
        for d in docs:
            lines.append(f"  - {d['wiki_link']}（{d['title']}）")
        source_line = "\n".join(lines)
    
    # 在 YAML frontmatter 的 auto_filled 行后插入 source
    # 找到 frontmatter 结束位置（第二个 ---）
    parts = content.split("---", 2)
    if len(parts) >= 3:
        yaml_block = parts[1]
        rest = "---" + parts[2]
        
        # 在 auto_filled 行后追加，或在最后一个字段后追加
        if "auto_filled:" in yaml_block:
            yaml_block = re.sub(
                r'(auto_filled:[^\n]*\n)',
                r'\1' + source_line + '\n',
                yaml_block
            )
        else:
            # 在 frontmatter 末尾（---前）插入
            yaml_block = yaml_block.rstrip() + "\n" + source_line + "\n"
        
        new_content = "---" + yaml_block + rest
    else:
        # 没有 frontmatter，在开头创建
        new_content = "---\ntype: 课程笔记\n" + source_line + "\n---\n\n" + content
    
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"  OK: {os.path.basename(local_path)} ({len(docs)}个源)")

print("\n完成。")
