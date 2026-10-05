#!/usr/bin/env python3
"""
飞书AI教育课文档 vs 本地知识库 三分类比对脚本 v2。
核心逻辑：
- 已覆盖：截图笔记系列的父主题在本地有对应清单体笔记（整系列含子节），或独立文档直接对应
- 需新增：本地无对应笔记的AI课截图笔记、原创课原文、案例课、方法论等
- 待定：青少年营改编版（本地有成人版但是否单独沉淀需确认）
"""
import json, os, re

BASE = "/Users/panda/Desktop/knowledge-base"
META = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/meta")

with open(os.path.join(META, "leaf_docs.json"), encoding="utf-8") as f:
    leaf_docs = json.load(f)
with open(os.path.join(META, "fetch_results_all.json"), encoding="utf-8") as f:
    fetch_results = json.load(f)
with open(os.path.join(META, "leaf_slides.json"), encoding="utf-8") as f:
    leaf_slides = json.load(f)

fetch_map = {r["obj_token"]: r for r in fetch_results}

def p(rel):
    return os.path.join(BASE, rel)

def clean_title(title):
    t = title
    t = re.sub(r'[（(]截图[^）)]*[）)]', '', t)
    t = re.sub(r'-截图笔记$', '', t)
    t = re.sub(r'[（(]阅读优化版[）)]', '', t)
    t = re.sub(r'\s+逐字稿$', '', t)
    t = t.strip().rstrip('-').strip()
    return t

def get_content_length(obj_token):
    r = fetch_map.get(obj_token)
    return r.get("content_length", 0) if r else 0

# ══════════════════════════════════════════════════════════════
# 已覆盖的截图笔记系列：顶级目录名 -> 本地对应文件绝对路径
# 这些系列的所有子节都判定为已覆盖（同一课程主题，本地已有清单体笔记）
# ══════════════════════════════════════════════════════════════
COVERED_SERIES = {
    "07 AI场景第一课-截图笔记": p("01-实事求是/个人必修/04 形成竞争力/03 AI 力/04 全员必修：AI场景第一课.md"),
    "10 十指讲香模型-截图笔记": p("01-实事求是/个人必修/03 不断练能力/05 卖点讲香/讲香实操：一堂十指模型.md"),
    "11 调研-武器篇-截图笔记": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/04 调研黑客：挖掘式调研武器库 — L6 清单体笔记.md"),
    "12 调研黑客5部曲认知篇-截图笔记": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/02 调研黑客：系统式调研认知篇 — L6 清单体笔记.md"),
    "13 调研黑客5部曲实操篇-截图笔记": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/03 调研黑客：系统式调研实操篇 — L6 清单体笔记.md"),
}

# 独立文档已覆盖：标题精确匹配 -> 本地路径
COVERED_STANDALONE = {
    "全员必修：重新理解「科学理念」": p("01-实事求是/创业必修/04 底层逻辑/01 科学理念/全员必修：重新理解「科学理念」· 清单体笔记.md"),
    "全员必修：重新理解解放思想": p("01-实事求是/创业必修/04 底层逻辑/03 解放思想/全员必修：重新理解「解放思想」· 清单体笔记.md"),
    "全员必修：深度复盘第一课": p("01-实事求是/个人必修/02 不断提认知/02 深度复盘/01 全员必修：深度复盘第一课.md"),
}

# ══════════════════════════════════════════════════════════════
# 青少年营系列：顶级目录名以 22-54 编号开头
# ══════════════════════════════════════════════════════════════
YOUTH_NUMBERS = [str(i) for i in range(22, 55)]

def is_youth_series(top_dir):
    # 青少年营：22-54编号，但排除秋马（26 秋马）
    if "秋马" in top_dir:
        return False
    for n in YOUTH_NUMBERS:
        if top_dir.startswith(n + " "):
            return True
    return False

# ══════════════════════════════════════════════════════════════
# 建议落位
# ══════════════════════════════════════════════════════════════
def filename_clean(title):
    """生成文件名时仅去除截图噪声，保留逐字稿/阅读优化版等区分后缀。"""
    t = title
    t = re.sub(r'[（(]截图[^）)]*[）)]', '', t)
    t = re.sub(r'-截图笔记$', '', t)
    t = t.strip()
    t = re.sub(r'[\\/:*?"<>|]', '_', t)
    return t if t else "untitled"

def suggest_placement(doc):
    title = doc["title"]
    path = doc["path"]
    clean = clean_title(title)
    top_dir = path.split("/")[0] if "/" in path else title
    fname = f"{filename_clean(title)}.md"

    # 提示词模板
    if "提示词模板" in title:
        return os.path.join(BASE, "03-知行合一/95-素材/AI提示词", fname)

    # 方法论/SOP
    if "截图转文字" in title or "课程链接提取" in title:
        return os.path.join(BASE, "00-天一生水/02-工具标准", fname)

    # 知识库设计
    if title.strip() == "知识库":
        return os.path.join(BASE, "00-天一生水/05-架构设计", fname)

    # 直播/行动营/秋马/蓝鱼
    if any(k in title for k in ["🎯", "秋马", "蓝鱼", "行动营"]):
        return os.path.join(BASE, "01-实事求是/在线教育", fname)

    # 原创课材料（根节点 + 03 AI数据第一课子节点）
    original_titles = [
        "01 AI双三角", "01 AI双三角 逐字稿", "02 AI如何生图", "03 AI数据",
        "04 同一个人", "05 提示词复制", "07 数据的计算", "AI教育课", "AI简历",
        "AI课程PPT制作经验总结",
    ]
    if any(title.startswith(k) for k in original_titles) or path.startswith("03 AI数据第一课/"):
        sub = ""
        if path.startswith("03 AI数据第一课/"):
            sub = "03 AI数据第一课"
        return os.path.join(BASE, "03-知行合一/01 AI 教育/AI教育课全系列", sub, fname)

    # AI课截图笔记 → AI技能/
    ai_skill_dirs = [
        "04 AI口喷", "05 AI基本功", "06 AI双三角", "07 AI场景第一课",
        "16 AI场景如何落地", "08 双三角思考", "12 AI内容工业化",
        "18 AI落地", "09 如何设计 partner", "13 AI设计实践",
        "20 如何写一篇文章", "14 AI制作ppt", "15 AI自动化生成网感视频",
        "10 十指讲香模型", "09 调研-爆炸式调研",
    ]
    for kw in ai_skill_dirs:
        if top_dir.startswith(kw):
            sub = clean_title(top_dir)
            return os.path.join(BASE, "01-实事求是/AI技能", sub, fname)

    # 案例课 → 案例课/
    case_dirs = {
        "17 如何把汇报打磨成一个好案例": "如何把汇报打磨成好案例",
        "19 一堂的信": "一堂的信",
        "10 一堂 X探月": "一堂X探月",
        "21 龙虾员工实践": "龙虾员工实践",
        "11 做课培训": "做课培训",
        "08 我用一堂做一堂": "我用一堂做一堂",
    }
    for kw, sub in case_dirs.items():
        if top_dir.startswith(kw):
            return os.path.join(BASE, "01-实事求是/案例课", sub, fname)

    # 调研系列 → 情报调研/
    if "爆炸式调研" in top_dir:
        return os.path.join(BASE, "01-实事求是/创业必修/02 起盘阶段/05 情报调研", fname)

    # 青少年营 → 按课程域
    youth_map = {
        "五步法": "01-实事求是/创业必修/02 起盘阶段/01 关键假设/青少年营",
        "MVP": "01-实事求是/创业必修/02 起盘阶段/06 精益实验/青少年营",
        "低成本验证": "01-实事求是/创业必修/02 起盘阶段/06 精益实验/青少年营",
        "mvp验证": "01-实事求是/创业必修/02 起盘阶段/06 精益实验/青少年营",
        "需求侦探": "01-实事求是/创业必修/02 起盘阶段/02 需求分析/青少年营",
        "需求洞察": "01-实事求是/创业必修/02 起盘阶段/02 需求分析/青少年营",
        "需求分析": "01-实事求是/创业必修/02 起盘阶段/02 需求分析/青少年营",
        "调研黑客": "01-实事求是/创业必修/02 起盘阶段/05 情报调研/青少年营",
        "产品内核": "01-实事求是/创业必修/02 起盘阶段/03 产品内核/青少年营",
        "科学决策": "01-实事求是/管理必修/03 管业务/03 做决策/青少年营",
        "把好想法变成真事": "01-实事求是/创业必修/02 起盘阶段/01 关键假设/青少年营",
        "暑假完整介绍": "01-实事求是/创业必修/青少年营",
        "领导力": "01-实事求是/管理必修/02 管团队/青少年营",
        "时间管理": "01-实事求是/个人必修/01 时间管理/青少年营",
        "人生红点": "01-实事求是/个人必修/05 人生红点/青少年营",
        "刻意练习": "01-实事求是/个人必修/03 不断练能力/01 刻意练习/青少年营",
        "知识管理": "01-实事求是/个人必修/02 不断提认知/03 知识管理/青少年营",
        "IPO": "01-实事求是/个人必修/02 不断提认知/01 科学学习/青少年营",
        "自我介绍": "01-实事求是/个人必修/04 形成竞争力/01 表达力/青少年营",
        "泛产品设计": "01-实事求是/个人必修/04 形成竞争力/02 设计力/青少年营",
        "AI双三角": "01-实事求是/AI技能/青少年营",
    }
    for kw, target in youth_map.items():
        if kw in top_dir:
            return os.path.join(BASE, target, fname)

    return os.path.join(BASE, "01-实事求是/AI技能", fname)

# ══════════════════════════════════════════════════════════════
# 判定
# ══════════════════════════════════════════════════════════════
results = []
for doc in leaf_docs:
    title = doc["title"]
    path = doc["path"]
    top_dir = path.split("/")[0] if "/" in path else title
    clean = clean_title(title)
    obj_token = doc["obj_token"]
    content_len = get_content_length(obj_token)
    wiki_link = f"https://feishu.cn/docx/{obj_token}"

    status = None
    local_path = ""
    reason = ""
    suggested = ""

    # 1. 独立文档精确匹配 → 已覆盖
    if title in COVERED_STANDALONE:
        status = "已覆盖"
        local_path = COVERED_STANDALONE[title]

    # 2. 已覆盖截图笔记系列 → 已覆盖（含所有子节）
    elif top_dir in COVERED_SERIES:
        status = "已覆盖"
        local_path = COVERED_SERIES[top_dir]

    # 3. 青少年营系列 → 待定
    elif is_youth_series(top_dir):
        status = "待定"
        reason = "青少年营改编版，本地有成人版对应课程但是否需单独沉淀需确认"
        suggested = suggest_placement(doc)
        # 尝试找本地成人版对应
        youth_local_hints = {
            "五步法": p("01-实事求是/创业必修/02 起盘阶段/01 关键假设/03 全员必修：重新理解「一堂五步法」· L6 萃取笔记.md"),
            "MVP": p("01-实事求是/创业必修/02 起盘阶段/06 精益实验/03 低成本验证实操2：MVP设计篇 — L6 清单体笔记.md"),
            "低成本验证": p("01-实事求是/创业必修/02 起盘阶段/06 精益实验/01 全员必修：低成本验证认知篇 — L6 清单体笔记.md"),
            "需求侦探": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操1：剥离拆解篇 · 清单体笔记.md"),
            "需求洞察": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操2：场景推演篇.md"),
            "需求分析": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操3：定性评估篇.md"),
            "调研黑客": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/02 调研黑客：系统式调研认知篇 — L6 清单体笔记.md"),
            "产品内核": p("01-实事求是/创业必修/02 起盘阶段/03 产品内核/产品内核2：剥离最小内核 — L6 清单体笔记.md"),
            "科学决策": p("01-实事求是/管理必修/03 管业务/03 做决策/01 全员必修：科学决策审美篇.md"),
            "领导力": p("01-实事求是/管理必修/02 管团队/01 基本功/01 全员必修：重新理解苦练基本功.md"),
            "时间管理": p("01-实事求是/个人必修/01 时间管理/《全员必修：时间管理必修课》L6 清单体笔记.md"),
            "人生红点": p("01-实事求是/个人必修/05 人生红点/01 一堂 · 人生红点全景图（认知篇）.md"),
            "刻意练习": p("01-实事求是/个人必修/03 不断练能力/01 刻意练习/01 刻意练习：重新理解「科学成长」.md"),
            "知识管理": p("01-实事求是/个人必修/02 不断提认知/03 知识管理/全员必修：知识管理必修课.md"),
            "IPO": p("01-实事求是/个人必修/02 不断提认知/01 科学学习/01 IPO 认知篇：重新理解 科学学习.md"),
            "泛产品设计": p("01-实事求是/个人必修/04 形成竞争力/02 设计力/01 全员必修：泛产品设计认知篇.md"),
            "AI双三角": p("01-实事求是/案例课/06 一堂马拉松/01 AI时代竞争力双三角模型：案例实践落地汇总.md"),
        }
        for kw, lp in youth_local_hints.items():
            if kw in top_dir:
                local_path = lp
                reason += f"；本地成人版参考：{os.path.basename(lp)}"
                break

    # 4. 其余 → 需新增
    else:
        status = "需新增"
        suggested = suggest_placement(doc)

    results.append({
        "title": title,
        "clean_title": clean,
        "path": path,
        "top_dir": top_dir,
        "obj_token": obj_token,
        "obj_type": doc["obj_type"],
        "wiki_link": wiki_link,
        "status": status,
        "local_path": local_path,
        "suggested_path": suggested,
        "reason": reason,
        "content_length": content_len,
    })

# 统计
stats = {"已覆盖": 0, "需新增": 0, "待定": 0}
for r in results:
    stats[r["status"]] += 1

print(f"分类完成：")
print(f"  叶子文档总数: {len(results)}")
print(f"  已覆盖: {stats['已覆盖']}")
print(f"  需新增: {stats['需新增']}")
print(f"  待定: {stats['待定']}")
print(f"  跳过(slides): {len(leaf_slides)}")
print(f"  抓取失败: 0")
print(f"  总计(含slides): {len(results) + len(leaf_slides)}")

# 按顶级目录分组统计
print("\n── 按顶级目录分组 ──")
from collections import defaultdict
group_stats = defaultdict(lambda: {"已覆盖":0, "需新增":0, "待定":0, "total":0})
for r in results:
    g = group_stats[r["top_dir"]]
    g[r["status"]] += 1
    g["total"] += 1
for td in sorted(group_stats.keys()):
    g = group_stats[td]
    print(f"  {td[:40]:40s} 总{g['total']:3d} 覆{g['已覆盖']:3d} 新{g['需新增']:3d} 定{g['待定']:3d}")

with open(os.path.join(META, "classification.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("\n分类结果已保存。")
