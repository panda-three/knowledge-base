#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据 inventory.json 生成分类规则 + 目标目录树 + 完整移动计划（只读，无写操作）"""
import json

inv = json.load(open("/Users/panda/Desktop/knowledge-base/.feishu-organize/inventory.json"))
root = inv["root"]
by_title = {}
for n in root:
    by_title.setdefault(n["title"], []).append(n)

PLAN = {"creates": [], "moves": [], "version": "v1"}

# ---------- 创建项 ----------
PLAN["creates"].append({"action": "create_node", "title": "00-首页导航", "target": "/", "reason": "新建全库入口页（移动完成后撰写内容）", "confidence": "high"})
for t in ["01-课程成品", "02-学习笔记", "03-方法论与SOP", "04-资料归档", "05-待整理"]:
    PLAN["creates"].append({"action": "create_folder", "title": t, "target": "/", "reason": "方案A顶层分区", "confidence": "high"})

SERIES = [
    ("01-AI双三角", ["06 AI双三角-截图笔记", "37 7.27 AI双三角-截图笔记", "43 8.4 AI双三角-截图笔记", "45 8.7 AI双三角-截图笔记", "08 双三角思考-截图笔记"]),
    ("02-一堂五步法", ["22 7.14 一堂五步法-截图笔记", "29 7.20 一堂五步法-截图笔记", "30 7.21 一堂五步法-截图笔记", "35 7.24 一堂五步法-截图笔记"]),
    ("03-调研方法论", ["27 7.16 调研黑客-截图笔记", "09 调研-爆炸式调研-截图笔记", "11 调研-武器篇-截图笔记", "12 调研黑客5部曲认知篇-截图笔记", "13 调研黑客5部曲实操篇-截图笔记"]),
    ("04-产品与验证", ["24 7.14 低成本验证之MVP-截图笔记", "25 7.15 需求侦探之旅-截图笔记", "28 7.17 需求洞察-截图笔记", "31 7.21 低成本验证-截图笔记", "32 7.22 青少年mvp验证课-截图笔记", "33 7.22 需求分析-截图笔记", "34 7.23 产品内核-截图笔记", "36 7.26 产品内核-截图笔记"]),
    ("05-领导力", ["39 7.28 重新理解领导力-截图笔记", "41 7.31 AI时代的领导力-截图笔记", "46 8.7 领导力-截图笔记"]),
    ("06-泛产品设计", ["40 7.30 泛产品设计-截图笔记", "44 8.6 泛产品设计-截图笔记"]),
    ("07-个人成长", ["42 8.14 人生红点-截图笔记", "49 人生红点-截图笔记", "50 时间管理-截图笔记", "51 知识管理-截图笔记", "52 刻意练习1-截图笔记", "53 刻意练习2-截图笔记"]),
    ("08-AI技能与创作", ["04 AI口喷-截图笔记", "05 AI基本功-截图笔记", "12 AI内容工业化生产-截图笔记", "13 AI设计实践-截图笔记", "14 AI制作ppt-截图笔记", "15 AI自动化生成网感视频-截图笔记"]),
    ("09-AI应用与场景", ["03 AI数据第一课", "07 AI场景第一课-截图笔记", "16 AI场景如何落地-截图笔记", "18 AI落地-探索AI协作新范式-截图笔记"]),
    ("10-其他课程", ["17 如何把汇报打磨成一个好案例-截图笔记", "09 如何设计 partner-截图笔记", "20 如何写一篇文章-截图笔记", "21 龙虾员工实践-截图笔记", "38 7.27 科学决策-截图笔记", "47 IPO1-截图笔记", "48 IPO2-截图笔记", "54 从交叉到交付，从新设计你的自我介绍-截图笔记", "11 做课培训-截图笔记", "10 十指讲香模型-截图笔记", "19 一堂的信-截图笔记", "10 一堂 X探月-截图笔记", "23 7.14 暑假完整介绍-截图笔记", "26 7.15 把好想法变成真事-截图笔记", "08 我用一堂做一堂-战略笃定篇-截图笔记"]),
]
for s, titles in SERIES:
    PLAN["creates"].append({"action": "create_folder", "title": f"02-学习笔记/{s}", "target": "/02-学习笔记", "reason": f"截图笔记按课程系列分组（{len(titles)} 个目录）", "confidence": "high"})

# ---------- 移动项：顶层映射 ----------
TOP = {
    "01-课程成品": [
        "01 AI双三角", "01 AI双三角 逐字稿", "02 AI如何生图", "03 AI数据",
        "04 同一个人，同一个AI，一分钱没多花：改五句话，图片能好到什么程度",
        "05 提示词复制", "07 数据的计算", "AI时代的数据计算", "AI时代的数据计算（互动精简版）",
    ],
    "03-方法论与SOP": [
        "方法论：课程链接提取入库与复用方案",
        "08 截图转文字：经验沉淀·不足复盘·标准流程SOP",
        "AI课程PPT制作经验总结", "AI课程PPT制作提示词模板",
    ],
    "04-资料归档": [
        "全员必修：深度复盘第一课", "全员必修：重新理解「科学理念」", "全员必修：重新理解解放思想",
        "🎯AI落地Live 87·蓝鱼：素人上手搭AI知识体系", "🎯一堂行动营：刻意练习AI落地篇",
        "26 秋马：AI 十倍速成长 1/2（阅读优化版）", "26 秋马：AI 十倍速成长 2/2（阅读优化版）",
    ],
}
TITLE_TARGET = {}
for _folder, _titles in TOP.items():
    for _t in _titles:
        TITLE_TARGET[_t] = _folder
# 待人工确认（→ 05-待整理）
REVIEW = {
    "12 调研黑客5部曲认知篇-截图笔记": "与同名文件夹（8子文档版）重复，确认后删除单文档",
    "26 秋马：AI 十倍速成长 1/2": "原版，已被「阅读优化版」取代",
    "26 秋马：AI 十倍速成长 2/2": "原版，已被「阅读优化版」取代",
    "AI教育课": "文档基本为空，疑似旧索引",
    "知识库": "归属不明，疑似旧入口",
    "AI简历": "归属不明，需确认是模板/成品/资料",
}
SERIES_MAP = {}
for s, titles in SERIES:
    for t in titles:
        SERIES_MAP[t] = f"02-学习笔记/{s}"

def find_nodes(title):
    return by_title.get(title, [])

unmatched = []
for n in root:
    t, hc = n["title"], n["has_child"]
    if t in TITLE_TARGET:
        target = TITLE_TARGET[t]; conf, reason = "high", "课程成品/讲义/课件"
    elif t in REVIEW and not hc:
        target = "05-待整理"; conf, reason = "low", REVIEW[t]
    elif t in SERIES_MAP and hc:
        target = SERIES_MAP[t]; conf = "medium" if t in [
            "09 如何设计 partner-截图笔记", "11 做课培训-截图笔记", "03 AI数据第一课-截图笔记",
            "07 AI场景第一课-截图笔记", "18 AI落地-探索AI协作新范式-截图笔记", "16 AI场景如何落地-截图笔记",
            "10 十指讲香模型-截图笔记", "38 7.27 科学决策-截图笔记", "21 龙虾员工实践-截图笔记",
            "08 我用一堂做一堂-战略笃定篇-截图笔记", "19 一堂的信-截图笔记", "10 一堂 X探月-截图笔记",
            "23 7.14 暑假完整介绍-截图笔记", "26 7.15 把好想法变成真事-截图笔记",
            "54 从交叉到交付，从新设计你的自我介绍-截图笔记", "17 如何把汇报打磨成一个好案例-截图笔记",
        ] else "high"
        reason = "截图笔记按课程系列归档"
    else:
        target = "05-待整理"; conf, reason = "low", "未匹配到分类，需人工确认"
        unmatched.append(t)
    PLAN["moves"].append({
        "title": t, "type": n["type"], "node_token": n["node_token"], "obj_token": n["obj_token"],
        "has_child": hc, "source": "/" + t, "target": target, "action": "move",
        "reason": reason, "confidence": conf,
        "needs_review": target == "05-待整理",
    })

json.dump(PLAN, open("/Users/panda/Desktop/knowledge-base/.feishu-organize/plan.json", "w"), ensure_ascii=False, indent=1)

# ---------- 输出汇总 ----------
from collections import Counter
moves = PLAN["moves"]
creates = PLAN["creates"]
print("总计划项:", len(moves) + len(creates))
print("创建:", len(creates), "| 移动:", len(moves))
print("待人工确认:", sum(1 for m in moves if m["needs_review"]))
print("置信度:", dict(Counter(m["confidence"] for m in moves)))
print("\n移动按目标分组：")
for target, cnt in Counter(m["target"] for m in moves).most_common():
    print(f"  {target}: {cnt}")
if unmatched:
    print("\n未匹配:", unmatched)
