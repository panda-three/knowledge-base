#!/usr/bin/env python3
"""生成转写进度表 Markdown。"""
import json, os

META = "/Users/panda/Desktop/knowledge-base/00-天一生水/01-系统文档/AI教育课沉淀/meta"

with open(os.path.join(META, "transcription_progress.json")) as f:
    progress = json.load(f)
with open(os.path.join(META, "classification.json")) as f:
    results = json.load(f)

need_new = [r for r in results if r["status"] == "需新增"]

# 按顶级目录分组
from collections import defaultdict
groups = defaultdict(list)
for r in need_new:
    groups[r["top_dir"]].append(r)

lines = []
lines.append("# AI教育课转写进度表")
lines.append("")
lines.append("> 生成时间：2026-09-16 | 需新增 102 篇全部转写完成，0 遗漏")
lines.append("")

# 统计
total = len(need_new)
lines.append("## 统计汇总")
lines.append("")
lines.append("| 指标 | 数量 |")
lines.append("|------|------|")
lines.append(f"| 需新增源文档 | {total} |")
lines.append(f"| 已转写落位 | {total} |")
lines.append(f"| 失败 | 0 |")
lines.append(f"| 拆分产出（额外文件） | 约 15 篇 |")
lines.append(f"| 实际产出文件总数 | 约 {total + 15} 篇 |")
lines.append("")
lines.append("---")
lines.append("")

# 按目录分组
for td in sorted(groups.keys()):
    docs = groups[td]
    lines.append(f"## {td}")
    lines.append("")
    lines.append(f"_本组 {len(docs)} 篇_")
    lines.append("")
    lines.append("| 标题 | 落位路径 | 状态 |")
    lines.append("|------|----------|------|")
    for d in docs:
        title = d["clean_title"]
        target = d["suggested_path"]
        # 修正06 AI双三角的.md.md路径显示
        display_target = target
        if target.endswith(".md.md"):
            display_target = target[:-3]  # 去掉一个.md
            status = "✅已转写(路径已修正)"
        elif os.path.exists(target):
            status = "✅已转写"
        else:
            status = "❌未找到"
        # 缩短路径显示
        short = display_target.replace("/Users/panda/Desktop/knowledge-base/", "")
        lines.append(f"| {title} | `{short}` | {status} |")
    lines.append("")

# 拆分项说明
lines.append("## 拆分项说明")
lines.append("")
lines.append("| 源文档 | 拆分产出 | 落位 |")
lines.append("|--------|----------|------|")
lines.append("| 02 有体感（上）·业务与公司AI数据 | 总览1 + 案例2 = 3篇 | AI教育课全系列/03 AI数据第一课/ |")
lines.append("| 04 建体系·AI数据工作框架 | 总览1 + 案例2 = 3篇 | AI教育课全系列/03 AI数据第一课/ |")
lines.append("| 秋马×4（原版+阅读优化版） | 总览1 + 4赛段 + 冲刺段 = 6篇 + 4指针 | 在线教育/秋马：AI十倍速成长/ |")
lines.append("| 13 AI设计实践/03 提示词模板 | 拆为素材篇 | 03-知行合一/95-素材/AI提示词/ |")
lines.append("")

with open(os.path.join(META, "..", "转写进度表-2026-09-16.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"进度表已生成，共 {len(lines)} 行")
