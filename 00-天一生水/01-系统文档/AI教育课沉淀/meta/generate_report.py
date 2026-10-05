#!/usr/bin/env python3
"""生成最终比对清单 Markdown。"""
import json, os
from collections import defaultdict

BASE = "/Users/panda/Desktop/knowledge-base"
META = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/meta")
OUTPUT = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/AI教育课比对清单-2026-09-16.md")

with open(os.path.join(META, "classification.json"), encoding="utf-8") as f:
    results = json.load(f)
with open(os.path.join(META, "leaf_slides.json"), encoding="utf-8") as f:
    leaf_slides = json.load(f)

BADGE = {"已覆盖": "✅", "需新增": "🆕", "待定": "❓", "跳过": "⏭"}

# 统计
stats = defaultdict(int)
for r in results:
    stats[r["status"]] += 1
stats["跳过"] = len(leaf_slides)
stats["抓取失败"] = 0
total = len(results) + stats["跳过"]

# 按顶级目录分组，保持飞书原顺序
groups = defaultdict(list)
group_order = []
for r in results:
    td = r["top_dir"]
    if td not in groups:
        group_order.append(td)
    groups[td].append(r)

lines = []
lines.append("# AI教育课知识库比对清单")
lines.append("")
lines.append(f"> 生成时间：2026-09-16 | 飞书 wiki space_id: 7669431379494440158")
lines.append(f"> 原始 markdown 正文已抓取至：`00-天一生水/01-系统文档/AI教育课沉淀/raw/`（236 篇）")
lines.append("")

# 统计汇总表
lines.append("## 统计汇总")
lines.append("")
lines.append("| 指标 | 数量 |")
lines.append("|------|------|")
lines.append(f"| 文档总数（含 slides） | {total} |")
lines.append(f"| ✅ 已覆盖 | {stats['已覆盖']} |")
lines.append(f"| 🆕 需新增 | {stats['需新增']} |")
lines.append(f"| ❓ 待定 | {stats['待定']} |")
lines.append(f"| ⏭ 跳过（slides） | {stats['跳过']} |")
lines.append(f"| ❌ 抓取失败 | {stats['抓取失败']} |")
lines.append("")
lines.append("---")
lines.append("")

# 图例
lines.append("## 图例")
lines.append("")
lines.append("- ✅ **已覆盖**：本地已有对应清单体笔记")
lines.append("- 🆕 **需新增**：本地无对应笔记，建议按指定路径新增")
lines.append("- ❓ **待定**：青少年营改编版等需人工确认是否单独沉淀")
lines.append("- ⏭ **跳过**：slides 类型不抓取正文")
lines.append("")
lines.append("---")
lines.append("")

# 按目录分组输出
for td in group_order:
    docs = groups[td]
    # 组统计
    g_stats = defaultdict(int)
    for d in docs:
        g_stats[d["status"]] += 1
    
    lines.append(f"## {td}")
    lines.append("")
    lines.append(f"_本组 {len(docs)} 篇：✅{g_stats['已覆盖']} 🆕{g_stats['需新增']} ❓{g_stats['待定']}_")
    lines.append("")
    
    for d in docs:
        badge = BADGE[d["status"]]
        title = d["clean_title"]
        link = d["wiki_link"]
        clen = d["content_length"]
        
        # 右侧信息
        if d["status"] == "已覆盖":
            right = f"本地：`{d['local_path']}`"
        elif d["status"] == "需新增":
            right = f"建议：`{d['suggested_path']}`"
        else:  # 待定
            parts = []
            if d["local_path"]:
                parts.append(f"参考：`{d['local_path']}`")
            if d["suggested_path"]:
                parts.append(f"建议：`{d['suggested_path']}`")
            right = " | ".join(parts) if parts else ""
        
        note = d.get("reason", "")
        note_str = f" _{note}_" if note else ""
        
        lines.append(f"- {badge} **{title}** — [飞书]({link}) | {clen}字 | {right}{note_str}")
    
    lines.append("")

# slides 跳过
lines.append("## Slides（跳过）")
lines.append("")
for s in leaf_slides:
    lines.append(f"- ⏭ **{s['title']}** — obj_token: `{s['obj_token']}` | slides 类型不抓取正文")
lines.append("")

# 抓取失败
lines.append("## 抓取失败")
lines.append("")
lines.append("_无_")
lines.append("")

# 写入
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"比对清单已生成：{OUTPUT}")
print(f"总行数：{len(lines)}")
print(f"文件大小：{os.path.getsize(OUTPUT)} bytes")
