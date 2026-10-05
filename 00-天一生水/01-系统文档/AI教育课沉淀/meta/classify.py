#!/usr/bin/env python3
"""
飞书AI教育课文档 vs 本地知识库 三分类比对脚本。
产出：比对清单 Markdown + 分类 JSON。
"""
import json, os, re

BASE = "/Users/panda/Desktop/knowledge-base"
META = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/meta")
RAW = os.path.join(BASE, "00-天一生水/01-系统文档/AI教育课沉淀/raw")
KB = BASE

# ── 加载数据 ──
with open(os.path.join(META, "leaf_docs.json"), encoding="utf-8") as f:
    leaf_docs = json.load(f)
with open(os.path.join(META, "fetch_results_all.json"), encoding="utf-8") as f:
    fetch_results = json.load(f)
with open(os.path.join(META, "local_files.json"), encoding="utf-8") as f:
    local_files = json.load(f)
with open(os.path.join(META, "leaf_slides.json"), encoding="utf-8") as f:
    leaf_slides = json.load(f)

# 建 obj_token -> fetch_result 映射
fetch_map = {r["obj_token"]: r for r in fetch_results}

# 建本地文件名 -> 绝对路径映射（用于快速查找）
local_by_name = {}
for lf in local_files:
    basename = os.path.basename(lf["path"]).replace(".md", "")
    local_by_name[basename] = lf["abs_path"]

def clean_title(title):
    """清洗飞书标题，去掉噪声。"""
    t = title
    t = re.sub(r'[（(]截图[^）)]*[）)]', '', t)
    t = re.sub(r'-截图笔记$', '', t)
    t = re.sub(r'[（(]阅读优化版[）)]', '', t)
    t = re.sub(r'\s+逐字稿$', '', t)
    t = t.strip().rstrip('-').strip()
    return t

def get_content_length(obj_token):
    r = fetch_map.get(obj_token)
    if r:
        return r.get("content_length", 0)
    return 0

def get_wiki_link(obj_token):
    """生成飞书 wiki 链接。"""
    return f"https://feishu.cn/docx/{obj_token}"

# ══════════════════════════════════════════════════════════════
# 本地已覆盖映射表：飞书文档主题关键词 -> 本地文件绝对路径
# 基于对本地 255 个文件的逐一分析
# ══════════════════════════════════════════════════════════════

def p(rel):
    """相对路径转绝对路径。"""
    return os.path.join(KB, rel)

# 明确已覆盖的映射（飞书标题关键词 -> 本地绝对路径）
COVERED_MAP = {
    # ── 全员必修系列 ──
    "全员必修：重新理解「科学理念」": p("01-实事求是/创业必修/04 底层逻辑/01 科学理念/全员必修：重新理解「科学理念」· 清单体笔记.md"),
    "全员必修：重新理解解放思想": p("01-实事求是/创业必修/04 底层逻辑/03 解放思想/全员必修：重新理解「解放思想」· 清单体笔记.md"),
    "全员必修：深度复盘第一课": p("01-实事求是/个人必修/02 不断提认知/02 深度复盘/01 全员必修：深度复盘第一课.md"),
    # ── 调研系列 ──
    "调研黑客5部曲认知篇": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/02 调研黑客：系统式调研认知篇 — L6 清单体笔记.md"),
    "调研黑客5部曲实操篇": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/03 调研黑客：系统式调研实操篇 — L6 清单体笔记.md"),
    "调研-武器篇": p("01-实事求是/创业必修/02 起盘阶段/05 情报调研/04 调研黑客：挖掘式调研武器库 — L6 清单体笔记.md"),
    # ── 十指讲香 ──
    "十指讲香模型": p("01-实事求是/个人必修/03 不断练能力/05 卖点讲香/讲香实操：一堂十指模型.md"),
    # ── AI力系列（本地已有） ──
    "AI场景第一课": p("01-实事求是/个人必修/04 形成竞争力/03 AI 力/04 全员必修：AI场景第一课.md"),
    "AI数据第一课": p("01-实事求是/个人必修/04 形成竞争力/03 AI 力/05 AI数据第一课 待补充.md"),
    # ── 个人必修系列 ──
    "时间管理": p("01-实事求是/个人必修/01 时间管理/《全员必修：时间管理必修课》L6 清单体笔记.md"),
    "人生红点": p("01-实事求是/个人必修/05 人生红点/01 一堂 · 人生红点全景图（认知篇）.md"),
    "刻意练习": p("01-实事求是/个人必修/03 不断练能力/01 刻意练习/01 刻意练习：重新理解「科学成长」.md"),
    "知识管理": p("01-实事求是/个人必修/02 不断提认知/03 知识管理/全员必修：知识管理必修课.md"),
    "IPO": p("01-实事求是/个人必修/02 不断提认知/01 科学学习/01 IPO 认知篇：重新理解 科学学习.md"),
    # ── 泛产品设计 ──
    "泛产品设计": p("01-实事求是/个人必修/04 形成竞争力/02 设计力/01 全员必修：泛产品设计认知篇.md"),
    # ── 创业必修系列 ──
    "一堂五步法": p("01-实事求是/创业必修/02 起盘阶段/01 关键假设/03 全员必修：重新理解「一堂五步法」· L6 萃取笔记.md"),
    "低成本验证": p("01-实事求是/创业必修/02 起盘阶段/06 精益实验/01 全员必修：低成本验证认知篇 — L6 清单体笔记.md"),
    "MVP": p("01-实事求是/创业必修/02 起盘阶段/06 精益实验/03 低成本验证实操2：MVP设计篇 — L6 清单体笔记.md"),
    "产品内核": p("01-实事求是/创业必修/02 起盘阶段/03 产品内核/产品内核2：剥离最小内核 — L6 清单体笔记.md"),
    "需求侦探": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操1：剥离拆解篇 · 清单体笔记.md"),
    "需求洞察": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操2：场景推演篇.md"),
    "需求分析": p("01-实事求是/创业必修/02 起盘阶段/02 需求分析/需求实操3：定性评估篇.md"),
    # ── 管理必修 ──
    "科学决策": p("01-实事求是/管理必修/03 管业务/03 做决策/01 全员必修：科学决策审美篇.md"),
    "领导力": p("01-实事求是/管理必修/02 管团队/01 基本功/01 全员必修：重新理解苦练基本功.md"),  # 领导力无直接对应，用最接近的
    # ── 双三角（本地马拉松系列有覆盖） ──
    "AI双三角": p("01-实事求是/案例课/06 一堂马拉松/01 AI时代竞争力双三角模型：案例实践落地汇总.md"),
}

# ══════════════════════════════════════════════════════════════
# 建议落位规则
# ══════════════════════════════════════════════════════════════

def suggest_placement(doc):
    """根据文档标题和路径，给出建议落位绝对路径（含文件名）。"""
    title = doc["title"]
    path = doc["path"]
    clean = clean_title(title)
    fname = f"{clean}.md"
    
    # 1. 提示词模板类 → 03/95-素材/AI提示词/
    if "提示词模板" in title:
        return os.path.join(KB, "03-知行合一/95-素材/AI提示词", fname)
    
    # 2. 运营方法论/SOP → 00-天一生水/02-工具标准/
    if "截图转文字" in title or "课程链接提取" in title:
        return os.path.join(KB, "00-天一生水/02-工具标准", fname)
    
    # 3. 知识库设计文档 → 00-天一生水/05-架构设计/
    if title.strip() == "知识库":
        return os.path.join(KB, "00-天一生水/05-架构设计", fname)
    
    # 4. 直播/行动营/全员必修/秋马/蓝鱼 → 01-实事求是/在线教育/
    if any(k in title for k in ["🎯", "秋马", "蓝鱼", "行动营"]):
        return os.path.join(KB, "01-实事求是/在线教育", fname)
    
    # 5. 原创课材料（根节点的课程原文）→ 03-知行合一/01 AI 教育/AI教育课全系列/
    root_original = [
        "01 AI双三角", "01 AI双三角 逐字稿", "02 AI如何生图", "03 AI数据",
        "04 同一个人", "05 提示词复制", "07 数据的计算", "AI教育课", "AI简历",
        "AI课程PPT制作经验总结",
    ]
    if any(title.startswith(k) for k in root_original):
        return os.path.join(KB, "03-知行合一/01 AI 教育/AI教育课全系列", fname)
    
    # 03 AI数据第一课 的子节点也属于原创课材料
    if path.startswith("03 AI数据第一课/"):
        return os.path.join(KB, "03-知行合一/01 AI 教育/AI教育课全系列/03 AI数据第一课", fname)
    
    # 6. AI课笔记（截图笔记系列）→ 01-实事求是/AI技能/
    ai_skill_keywords = [
        "AI口喷", "AI基本功", "AI双三角-截图笔记", "AI场景第一课",
        "AI场景如何落地", "如何设计 partner", "AI内容工业化",
        "AI制作ppt", "AI自动化生成网感视频", "十指讲香模型",
        "如何写一篇文章", "AI设计实践", "AI落地-探索AI协作新范式",
        "双三角思考",
    ]
    # 检查路径的顶级目录
    top_dir = path.split("/")[0] if "/" in path else title
    if any(k in top_dir for k in ai_skill_keywords):
        # 按子目录组织
        sub = clean_title(top_dir).replace("-截图笔记", "")
        return os.path.join(KB, "01-实事求是/AI技能", sub, fname)
    
    # 7. 青少年营系列（22-54编号）→ 按课程域分
    youth_course_map = {
        # 创业必修
        "五步法": "01-实事求是/创业必修/02 起盘阶段/01 关键假设",
        "MVP": "01-实事求是/创业必修/02 起盘阶段/06 精益实验",
        "低成本验证": "01-实事求是/创业必修/02 起盘阶段/06 精益实验",
        "需求侦探": "01-实事求是/创业必修/02 起盘阶段/02 需求分析",
        "需求洞察": "01-实事求是/创业必修/02 起盘阶段/02 需求分析",
        "需求分析": "01-实事求是/创业必修/02 起盘阶段/02 需求分析",
        "调研黑客": "01-实事求是/创业必修/02 起盘阶段/05 情报调研",
        "产品内核": "01-实事求是/创业必修/02 起盘阶段/03 产品内核",
        "科学决策": "01-实事求是/管理必修/03 管业务/03 做决策",
        "把好想法变成真事": "01-实事求是/创业必修/02 起盘阶段/01 关键假设",
        "暑假完整介绍": "01-实事求是/创业必修",
        "mvp验证": "01-实事求是/创业必修/02 起盘阶段/06 精益实验",
        # 管理必修
        "领导力": "01-实事求是/管理必修/02 管团队",
        # 个人必修
        "时间管理": "01-实事求是/个人必修/01 时间管理",
        "人生红点": "01-实事求是/个人必修/05 人生红点",
        "刻意练习": "01-实事求是/个人必修/03 不断练能力/01 刻意练习",
        "知识管理": "01-实事求是/个人必修/02 不断提认知/03 知识管理",
        "IPO": "01-实事求是/个人必修/02 不断提认知/01 科学学习",
        "自我介绍": "01-实事求是/个人必修/04 形成竞争力/01 表达力",
        # 泛产品设计
        "泛产品设计": "01-实事求是/个人必修/04 形成竞争力/02 设计力",
        # AI双三角（青少年版）
        "AI双三角": "01-实事求是/AI技能",
    }
    for kw, target_dir in youth_course_map.items():
        if kw in top_dir:
            return os.path.join(KB, target_dir, "青少年营", fname)
    
    # 8. 案例课系列
    case_keywords = {
        "做课培训": "01-实事求是/案例课",
        "如何把汇报打磨成一个好案例": "01-实事求是/案例课",
        "龙虾员工实践": "01-实事求是/案例课",
        "我用一堂做一堂": "01-实事求是/案例课",
        "一堂的信": "01-实事求是/案例课",
        "一堂 X探月": "01-实事求是/案例课",
    }
    for kw, target_dir in case_keywords.items():
        if kw in top_dir:
            return os.path.join(KB, target_dir, clean_title(top_dir), fname)
    
    # 9. 调研系列（爆炸式调研）
    if "爆炸式调研" in top_dir:
        return os.path.join(KB, "01-实事求是/创业必修/02 起盘阶段/05 情报调研", fname)
    
    # 默认：AI技能
    return os.path.join(KB, "01-实事求是/AI技能", fname)


# ══════════════════════════════════════════════════════════════
# 判定逻辑
# ══════════════════════════════════════════════════════════════

def classify(doc):
    """对单篇文档进行三分类判定。"""
    title = doc["title"]
    path = doc["path"]
    clean = clean_title(title)
    top_dir = path.split("/")[0] if "/" in path else title
    obj_token = doc["obj_token"]
    content_len = get_content_length(obj_token)
    
    # 检查是否已覆盖：精确匹配 COVERED_MAP
    covered_path = None
    for kw, lp in COVERED_MAP.items():
        if kw in title or kw in clean or kw in top_dir:
            covered_path = lp
            break
    
    # 特殊：青少年营版本的课程，本地只有成人版，判定为"待定"（主题相同但是青少年改编版）
    youth_prefixes = ["22 ", "23 ", "24 ", "25 ", "26 ", "27 ", "28 ", "29 ",
                      "30 ", "31 ", "32 ", "33 ", "34 ", "35 ", "36 ", "37 ",
                      "38 ", "39 ", "40 ", "41 ", "42 ", "43 ", "44 ", "45 ",
                      "46 ", "47 ", "48 ", "49 ", "50 ", "51 ", "52 ", "53 ", "54 "]
    is_youth = any(top_dir.startswith(p) for p in youth_prefixes)
    
    if is_youth and covered_path:
        # 青少年营版本：本地有成人版对应笔记，但青少年版是改编内容
        # 判定为待定，说明原因
        return {
            "status": "待定",
            "reason": f"青少年营改编版，本地有成人版对应笔记（{os.path.basename(covered_path)}），但是否需单独沉淀需确认",
            "local_path": covered_path,
            "suggested_path": suggest_placement(doc),
            "content_length": content_len,
        }
    
    if covered_path:
        return {
            "status": "已覆盖",
            "reason": "",
            "local_path": covered_path,
            "suggested_path": "",
            "content_length": content_len,
        }
    
    # 检查是否为子节点（截图笔记的分节），父主题已覆盖
    # 例如 "07 AI场景第一课-截图笔记/01 热身篇..." 的父主题 AI场景第一课 已覆盖
    parent_covered = None
    for kw, lp in COVERED_MAP.items():
        if kw in top_dir:
            parent_covered = lp
            break
    
    if parent_covered and not is_youth:
        # 父主题已覆盖的子节截图笔记 → 待定（截图笔记是原始素材，本地清单体笔记是萃取版）
        return {
            "status": "待定",
            "reason": f"父主题「{clean_title(top_dir)}」本地已有清单体笔记，此为分节截图笔记原始素材，是否需单独保留需确认",
            "local_path": parent_covered,
            "suggested_path": suggest_placement(doc),
            "content_length": content_len,
        }
    
    # 其余为需新增
    return {
        "status": "需新增",
        "reason": "",
        "local_path": "",
        "suggested_path": suggest_placement(doc),
        "content_length": content_len,
    }


# ══════════════════════════════════════════════════════════════
# 执行分类
# ══════════════════════════════════════════════════════════════

results = []
for doc in leaf_docs:
    r = classify(doc)
    r.update({
        "title": doc["title"],
        "clean_title": clean_title(doc["title"]),
        "path": doc["path"],
        "obj_token": doc["obj_token"],
        "obj_type": doc["obj_type"],
        "wiki_link": get_wiki_link(doc["obj_token"]),
    })
    results.append(r)

# 统计
stats = {"已覆盖": 0, "需新增": 0, "待定": 0, "跳过": 0, "抓取失败": 0}
for r in results:
    stats[r["status"]] += 1
stats["跳过"] = len(leaf_slides)
stats["总数"] = len(results) + stats["跳过"]

# 保存分类结果 JSON
with open(os.path.join(META, "classification.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"分类完成：")
print(f"  总数(含slides): {stats['总数']}")
print(f"  已覆盖: {stats['已覆盖']}")
print(f"  需新增: {stats['需新增']}")
print(f"  待定: {stats['待定']}")
print(f"  跳过(slides): {stats['跳过']}")
print(f"  抓取失败: {stats['抓取失败']}")

# 按状态分组打印摘要
for s in ["已覆盖", "需新增", "待定"]:
    items = [r for r in results if r["status"] == s]
    print(f"\n── {s} ({len(items)}) ──")
    for r in items[:5]:
        print(f"  {r['clean_title'][:50]}")
    if len(items) > 5:
        print(f"  ... 共 {len(items)} 篇")
