#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""003_高阶建模第一课-课程文档 组装脚本：拼接分片 + 素材归位 + 高保真替换 + 目录锚点 + 台账合并 + 校验"""
import re, os, glob

OUT = "/Users/panda/Desktop/knowledge-base/05-收件箱/003_高阶建模第一课-课程文档"
WORK = os.path.join(OUT, ".work")
IMG = os.path.join(OUT, "images")

# ---------- 1. 拼接主片段 ----------
frags = ["frag_01-04.md", "frag_05-08.md", "frag_09-12.md", "frag_13-14.md"]
body_parts = []
for fn in frags:
    txt = open(os.path.join(WORK, fn), encoding="utf-8").read()
    # 去掉片段尾的转录范围注释（统一在文档末尾加）
    txt = re.sub(r"\n*<!--\s*转录范围[^>]*-->\s*$", "", txt).strip()
    body_parts.append(txt)
body = "\n\n---\n\n".join(body_parts)

# ---------- 2. 高保真同图替换（素材版分辨率更高，统一采用素材版） ----------
replace_map = {
    "images/13-04.png": "images/19-01.png",
    "images/13-05.png": "images/19-02.png",
    "images/14-04.png": "images/20-01.png",
    "images/14-05.png": "images/20-02.png",
    "images/14-06.png": "images/20-03.png",
}
for old, new in replace_map.items():
    body = body.replace(old, new)
# 删除被替换的低分辨率孤儿文件
for old in replace_map:
    p = os.path.join(OUT, old)
    if os.path.exists(p):
        os.remove(p)
        print("删除孤儿低清图:", old)

# ---------- 3. 提取素材块 ----------
mat = open(os.path.join(WORK, "frag_素材.md"), encoding="utf-8").read()
blocks = {}
for m in re.finditer(r"(#### 主题素材：.*?)(?=\n#### 主题素材：|\Z)", mat, re.S):
    blk = m.group(1).strip()
    name = re.match(r"#### 主题素材：(.+)", blk).group(1).strip()
    # 去掉「建议归位」行
    blk = re.sub(r"\n*建议归位：[^\n]*", "", blk).strip()
    blocks[name] = blk
print("素材块提取:", list(blocks.keys()))

# ---------- 4. 素材归位插入 ----------
def insert_after(body, anchor, insert_text):
    assert body.count(anchor) == 1, f"锚点不唯一或不存在: {anchor!r} count={body.count(anchor)}"
    return body.replace(anchor, anchor + "\n\n" + insert_text)

def insert_before(body, anchor, insert_text):
    assert body.count(anchor) == 1, f"锚点不唯一或不存在: {anchor!r} count={body.count(anchor)}"
    return body.replace(anchor, insert_text + "\n\n" + anchor)

# 16 before/after → 07 页「直播通知文案」案例（07-02 图后）
body = insert_after(body, "![文案before/after对比分析截图](images/07-02.png)", blocks["before/after 对比"])
# 18 战略 → 08 页「建模案例：各种艰难筛选」之后、「建模案例：一堂个人地图」之前
body = insert_before(body, "#### 建模案例：一堂个人地图", blocks["战略"])
# 17 AI 拉满 → 11 页末尾
body = insert_after(body, "大家初步感觉到\"AI辅助建模\"的快了么：）", blocks["AI 拉满建模（里程碑研究）"])
# 15 复盘 → 14 页 IPO 循环图组之后（14-06 已替换为 20-03）
anchor15 = "![IPO循环图：一堂足够好的课](images/20-03.png)"
assert body.count(anchor15) == 1, "14页IPO组锚点异常"
body = body.replace(anchor15, anchor15 + "\n\n" + blocks["复盘的不同段位"])
# 19/20 组：已通过高保真替换并入（19→13页创业地图/基本功清单、20→14页IPO循环图）

# ---------- 5. 头部 + 目录 ----------
def github_anchor(t):
    t = t.lower()
    t = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", t, flags=re.UNICODE)  # 去标点
    t = re.sub(r"\s+", "-", t)  # 空格转连字符
    return t

heads = re.findall(r"^### (.+)$", body, re.M)
toc_lines = ["## 目录", ""]
for h in heads:
    toc_lines.append(f"- [{h}](#{github_anchor(h)})")

header = """# 高阶建模第一课 · 课程文档

> 本文档由课程截图转录整理而成。**文字内容完整保留**，截图中的图片、金句卡片、案例封面等视觉元素已从正文中分离，单独存放于 `images/` 文件夹，并在原位置以引用形式嵌入。
>
> 整理原则：
> - 讲课正文逐字转录，保留原本的口语表达
> - 原文中的红字/黄字强调，用 **加粗** 标示
> - 案例代入、互动等标签保留为引用块
> - 截图中的图片只保留图像本身，alt 文本为简短提示
>
> 覆盖范围：14 张主课程截图（页 01~14）+ 6 组主题素材共 28 张图（页 15~20，按主题并入相应小节）。
>
> 补充说明：
> - 05 页原文顶部无标题，直接从正文开始，按原文处理
> - 06 / 10 / 13 页原文顶部标题相同（「提升：背后的策略」），07 / 11 页相同（「提速：试试带着AI做」），为课程各阶段同名的固定小节，按原文保留
> - 主题素材「本质」（19-01/19-02）与主截图 13 页内嵌图同图、「如何练习」（20-01~03）与主截图 14 页 IPO 循环图同图，文档统一采用分辨率更高的素材版本

---

"""
final = header + "\n".join(toc_lines) + "\n\n---\n\n" + body + "\n\n<!-- 转录范围：01 ~ 14（主截图）+ 15 ~ 20（主题素材） -->\n"

final_path = os.path.join(OUT, "003_高阶建模第一课-课程文档.md")
open(final_path, "w", encoding="utf-8").write(final)
print(f"\n主文档已写出: {final_path}  ({len(final.splitlines())} 行)")

# ---------- 6. 台账合并 ----------
from PIL import Image
def img_size(fn):
    p = os.path.join(IMG, fn)
    try:
        im = Image.open(p); s = im.size; im.close(); return f"{s[0]}×{s[1]}"
    except Exception:
        return "—"

led_rows = []   # (编号, 尺寸, 画面, 要点)
# 主分片台账（两列）
for fn in ["台账_01-04.md", "台账_05-08.md", "台账_09-12.md", "台账_13-14.md"]:
    txt = open(os.path.join(WORK, fn), encoding="utf-8").read()
    for m in re.finditer(r"^\|\s*(\d{2}-\d{2})\s*\|\s*(.+?)\s*\|\s*$", txt, re.M):
        code, desc = m.group(1), m.group(2).strip()
        if code in ("13-04", "13-05", "14-04", "14-05", "14-06"):
            continue  # 已被高保真素材版取代，台账头部有说明
        led_rows.append((code, img_size(code), desc, "—"))
# 素材台账（四列：编号|尺寸|画面|要点）——用 split 解析，尺寸列可能含注释
mat_txt = open(os.path.join(WORK, "图注台账.md"), encoding="utf-8").read()
for line in mat_txt.splitlines():
    if not re.match(r"^\|\s*\d{2}-\d{2}\s*\|", line):
        continue
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    if len(parts) < 4:
        continue
    code, sz, desc, pts = parts[0], parts[1], parts[2], parts[3]
    sz = re.match(r"\d+×\d+", sz).group(0) if re.match(r"\d+×\d+", sz) else img_size(code)
    led_rows.append((code, sz, desc, pts))

led_rows.sort()
led_header = """# 高阶建模第一课 · 图注台账

> 逐张实际打开图片后记录的「编号 → 实际画面」。主截图 01~14 + 主题素材 15~20。
> 主截图内嵌图（01~14）尺寸由文件读取；主题素材（15~20）另附逐字看到的图内文字要点。
> 说明：13-04/13-05（创业地图、基本功清单）与 14-04~06（IPO 循环图三张）为低分辨率裁图，
> 与主题素材 19-01/19-02、20-01~03 内容相同，主文档已统一采用高分辨率素材版，本台账不再单独列出低清版。

| 编号 | 尺寸 | 实际画面 | 图内文字要点 |
|---|---|---|---|
"""
led_body = "\n".join(f"| {c} | {s} | {d} | {p} |" for c, s, d, p in led_rows)
led_path = os.path.join(OUT, "图注台账.md")
open(led_path, "w", encoding="utf-8").write(led_header + led_body + "\n")
print(f"台账已写出: {led_path}  ({len(led_rows)} 行)")

# ---------- 7. 校验 ----------
doc = final
used = set(re.findall(r"images/(\d{2}-\d{2})\.png", doc))
missing = [u for u in used if not os.path.exists(os.path.join(IMG, u + ".png"))]
led_codes = {c for c, *_ in led_rows}
print("\n=== 校验 ===")
print(f"文档引用图: {len(used)} 个编号; 缺失: {missing or '无'}")
print(f"台账编号: {len(led_codes)} 个")
print("文档有台账无:", sorted(used - led_codes) or "无")
print("台账有文档无:", sorted(led_codes - used) or "无")
alts = re.findall(r"!\[([^\]]*)\]\(images/", doc)
print(f"alt 平均 {sum(len(a) for a in alts)/len(alts):.1f} 字, 最长 {max(len(a) for a in alts)} 字")
# 锚点唯一性
anchors = [github_anchor(h) for h in heads]
dup = [a for a in set(anchors) if anchors.count(a) > 1]
print(f"### 标题 {len(heads)} 个; 重复锚点: {dup or '无'}")
# 图片文件 vs 引用（文件存在但未被引用 = 孤儿）
allfiles = set(f[:-4] for f in os.listdir(IMG) if f.endswith(".png"))
print("孤儿图文件（未被引用）:", sorted(allfiles - used) or "无")
print("images 最终文件数:", len(allfiles))
