#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian 双链断链扫描与修复脚本
功能：
  1. 扫描全库 .md 文件中的 [[双链]]（排除代码块和行内代码）
  2. 对比全库文件名索引，找出断链
  3. 自动修复：精确匹配 → 模糊匹配 → 删除历史遗留链接
  4. 生成修复报告
用法：
  python3 fix_broken_links.py          # 扫描+修复+报告（dry-run 模式加 --dry-run）
  python3 fix_broken_links.py --scan   # 仅扫描，输出断链清单
  python3 fix_broken_links.py --fix    # 执行修复
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ============ 配置 ============
KB_ROOT = Path("/Users/panda/Desktop/knowledge-base")
EXCLUDE_DIRS = {".git", ".obsidian", "raw", ".backup_before_fix"}
# raw 目录的完整排除路径前缀
EXCLUDE_PATH_PREFIXES = [
    str(KB_ROOT / "00-天一生水/01-系统文档/AI教育课沉淀/raw"),
    str(KB_ROOT / "00-天一生水/01-系统文档/AI教育课沉淀/meta/断链修复报告.md"),
    str(KB_ROOT / "00-天一生水/01-系统文档/AI教育课沉淀/meta/秋马问题复盘报告.md"),
]
BACKUP_DIR = KB_ROOT / "00-天一生水/01-系统文档/AI教育课沉淀/meta/.backup_before_fix"
REPORT_PATH = KB_ROOT / "00-天一生水/01-系统文档/AI教育课沉淀/meta/断链修复报告.md"

# 历史遗留旧路径前缀模式（这些链接大概率是旧库遗留，删除保留文字）
LEGACY_PATH_PATTERNS = [
    r"^05\s*Man[/\\]",
    r"^05Man[/\\]",
    r"^01\s*主题[/\\]",
    r"^01主题[/\\]",
    r"^03\s*Areas[/\\]",
    r"^03Areas[/\\]",
    r"^03\s*outputs[/\\]",
    r"^03outputs[/\\]",
    r"^09\s*关于我[/\\]",
    r"^09关于我[/\\]",
]

# 目录式链接（Home文件中的文件夹索引链接，指向的是目录而非.md文件）
DIR_LINK_PATTERN = re.compile(r"^\d{2}[-_].+$")

# 日期前缀旧链接
DATE_PREFIX_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_")

# 旧项目文档链接（C语言教学系统等历史项目文档）
OLD_PROJECT_DOC_PATTERN = re.compile(
    r"^(\d{2}\s.*(C\s*语言|题目卡|相似题|开发文档|需求文档))"
)

# 英文 slug 模式（旧库英文链接）- 全小写/数字开头、连字符、无中文
ENGLISH_SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9\-_]*$")

# 人名 slug 模式（常见拼音人名格式）
PERSON_SLUG_PATTERN = re.compile(
    r"^(ban-mingyang|chen-xiaoqing|hua-zong|pan-honghai|tan-naichao|truman|xiang-xiang|"
    r"[a-z]+-[a-z]+)$"
)

# 已知的英文 slug → 中文笔记名映射表（基于观察到的断链和库中文件）
EN_SLUG_TO_CHINESE = {
    "inspiration-flash": "灵感闪现",
    "ai-fifty-point-ceiling": "AI 能力上限",
    "dual-triangle-model": "双三角模型",
    "product-core": "产品核心",
    "key-assumption": "关键假设",
    "key-assumption-evaluation": "关键假设评估",
    "key-assumption-pool": "关键假设池",
    "jtbd": "JTBD",
    "ipo-model-scientific-learning": "IPO 科学学习",
    "deep-review-four-steps": "深度复盘四步法",
    "deep-review-iceberg": "深度复盘冰山",
    "deliberate-practice": "刻意练习",
    "universal-product-design": "泛产品设计",
    "muse-model": "MUSE 模型",
    "omega-model": "OMEGA 模型",
    "oscar-framework": "OSCAR 框架",
    "paso-framework": "PASO 框架",
    "five-step-method": "五步法",
    "yitang-five-steps": "一堂五步法",
    "growth-cycle-model": "增长周期模型",
    "feature-minimum-capability-unit": "特征最小能力单元",
    "demand-decomposition-3-5-cuts": "需求拆解 3-5 刀",
    "three-principles-of-demand-decomposition": "需求拆解三原则",
    "low-cost-validation": "低成本验证",
    "low-cost-validation-five-borrows": "低成本验证五借",
    "comprehensive-prediction-plus-fast-trial": "综合预测+快试",
    "business-prediction": "业务预测",
    "falsifiability-in-learning": "学习可证伪性",
    "aesthetic-as-filter": "审美即过滤器",
    "aesthetic-four-stages": "审美四阶段",
    "beautiful-work-imagination": "美好作品想象",
    "best-practice-modeling": "最佳实践建模",
    "how-to-balance-inspiration-and-polishing": "灵感与打磨的平衡",
    "how-to-measure-inspiration-quality": "灵感质量衡量",
    "accumulation-dependency-of-inspiration": "灵感积累依赖性",
    "ai-progress-paradigm": "AI 进步范式",
    "ai-four-elements": "AI 四要素",
    "ai-agent-note-taking-timeline": "AI Agent 笔记时间线",
    "ai-note-collaboration-modes": "AI 笔记协作模式",
    "note-taking-six-levels": "笔记六层",
    "soul-workflow": "SOUL 工作流",
    "encapsulation-hierarchy": "封装层级",
    "hard-stripping": "硬剥离",
    "black-hard-injury-cards": "黑硬伤卡片",
    "card-play-method": "卡片玩法",
    "36-card-toolkit": "36 卡片工具包",
    "259-framework": "259 框架",
    "259-scenario-framework": "259 场景框架",
    "subtraction-three-principles": "减法三原则",
    "switching-cost": "切换成本",
    "residual-brainpower": "剩余脑力",
    "self-sufficiency-confidence": "自足自信",
    "confident-yet-dissatisfied": "自信但不满意",
    "diseconomies-of-scale": "规模不经济",
    "research-weapon-arsenal": "调研武器库",
    "three-end-research": "三端调研",
    "usp-demand-formula": "USP 需求公式",
    "product-core-canvas": "产品核心画布",
    "prompt-tuning-model-yitang": "一堂提示词调优模型",
    "virtual-idol-case": "虚拟偶像案例",
    "world-learning-method": "世界学习法",
    "yitang": "一堂",
}

# 明确的断链 → 实际文件名映射（高置信度，直接修正）
EXPLICIT_LINK_MAP = {
    # 泛产品设计全景图系列
    "一堂 · 泛产品设计全景图（认知篇）": "01 全员必修：泛产品设计认知篇",
    "一堂 · 泛产品设计武器库全景图（框架篇）": "02 全员必修：泛产品设计框架篇",
    "一堂 · 泛产品设计 · 需求篇全景图": "03 泛产品实操1：需求篇",
    "一堂 · 泛产品设计 · 审美篇全景图": "04 泛产品实操2：审美篇",
    "一堂 · 泛产品设计 · 落地篇全景图": "05 泛产品实操3：落地篇",
    # 人生红点系列
    "人生红点": "一堂 · 人生红点全景图（认知篇）",
    # 其他已知映射
    "00-天一生水/03-基本法/知识库运营计划": "00-知识库总索引",
    "03-基本法/知识库运营计划": "00-知识库总索引",
}

# ============ 工具函数 ============

def should_exclude(filepath: Path) -> bool:
    """判断文件是否应被排除"""
    parts = filepath.parts
    for excl in EXCLUDE_DIRS:
        if excl in parts:
            return True
    filepath_str = str(filepath.resolve())
    for prefix in EXCLUDE_PATH_PREFIXES:
        if filepath_str.startswith(prefix):
            return True
    return False


def extract_links_from_content(content: str) -> list:
    """
    从 Markdown 内容中提取 [[链接]]，排除代码块和行内代码中的链接。
    返回 [(link_text, full_match, start_pos, end_pos), ...]
    """
    results = []
    lines = content.split("\n")
    in_code_block = False
    code_block_lang = ""

    pos = 0
    for line_idx, line in enumerate(lines):
        stripped = line.lstrip()

        # 检测代码块开始/结束
        if stripped.startswith("```") or stripped.startswith("~~~"):
            if not in_code_block:
                in_code_block = True
                code_block_lang = stripped.strip("`~").strip()
            else:
                # 结束代码块（只看开头匹配即可，简单处理）
                in_code_block = False
                code_block_lang = ""
            pos += len(line) + 1
            continue

        if in_code_block:
            pos += len(line) + 1
            continue

        # 处理行内代码：逐字符扫描，跳过反引号内的内容
        i = 0
        line_len = len(line)
        while i < line_len:
            # 检查行内代码
            if line[i] == "`":
                # 找到结束反引号
                j = i + 1
                while j < line_len and line[j] != "`":
                    j += 1
                if j < line_len:
                    i = j + 1
                    continue
                else:
                    i += 1
                    continue

            # 检查 [[ 链接
            if line[i:i+2] == "[[":
                # 找到 ]]
                j = i + 2
                depth = 0
                while j < line_len:
                    if line[j:j+2] == "[[":
                        depth += 1
                    elif line[j:j+2] == "]]":
                        if depth == 0:
                            break
                        depth -= 1
                    j += 1

                if j < line_len:
                    link_inner = line[i+2:j]
                    # 处理别名：[[目标|别名]] → 目标是 | 前面的部分
                    target = link_inner.split("|")[0].strip()
                    # 处理 heading 链接：[[目标#标题]] → 取 # 前面
                    target = target.split("#")[0].strip()
                    # 处理 block 链接：[[目标^blockid]]
                    target = target.split("^")[0].strip()

                    full_match = line[i:j+2]
                    results.append({
                        "line": line_idx + 1,
                        "target": target,
                        "full_match": full_match,
                        "raw_inner": link_inner,
                        "char_start": pos + i,
                        "char_end": pos + j + 2,
                    })
                    i = j + 2
                    continue
            i += 1

        pos += len(line) + 1

    return results


def normalize_name(name: str) -> str:
    """
    规范化文件名用于模糊匹配：
    - 去除 .md 后缀
    - 去除首尾空格
    - 统一空格：去掉所有空格
    - 全角→半角括号
    - · → - 统一
    - 去除常见前缀后缀
    """
    n = name.strip()
    if n.endswith(".md"):
        n = n[:-3]
    # 全角括号转半角
    n = n.replace("（", "(").replace("）", ")")
    # 统一分隔符
    n = n.replace("·", "-").replace("—", "-").replace("–", "-")
    # 去掉所有空格
    n = re.sub(r"\s+", "", n)
    # 去掉常见前缀
    n = re.sub(r"^一堂[·\-\s]*", "", n)
    n = re.sub(r"^全员必修[：:]*", "", n)
    n = re.sub(r"^课程[：:]*", "", n)
    # 去掉常见后缀
    n = re.sub(r"全景图.*$", "", n)
    n = re.sub(r"武器库.*$", "", n)
    n = re.sub(r"篇$", "", n)
    n = re.sub(r"实操\d*[：:]*", "", n)
    n = re.sub(r"^第?\d+[篇章节]?[：:\s]*", "", n)
    return n.lower()


def build_file_index() -> dict:
    """
    构建全库文件索引：
    返回 {normalized_basename: [relative_path1, relative_path2, ...]}
    同时也保留原始 basename → 路径的映射
    """
    index_normalized = defaultdict(list)
    index_raw = defaultdict(list)
    all_files = []

    for root, dirs, files in os.walk(KB_ROOT):
        # 过滤排除目录
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for f in files:
            if not f.endswith(".md"):
                continue
            full_path = Path(root) / f
            if should_exclude(full_path):
                continue

            rel_path = full_path.relative_to(KB_ROOT)
            basename = f[:-3]  # 去掉 .md
            normalized = normalize_name(basename)

            index_raw[basename].append(str(rel_path))
            index_normalized[normalized].append((str(rel_path), basename))
            all_files.append((str(rel_path), basename, normalized))

    return index_normalized, index_raw, all_files


def is_legacy_link(target: str) -> bool:
    """判断是否为历史遗留旧路径链接"""
    for pattern in LEGACY_PATH_PATTERNS:
        if re.match(pattern, target):
            return True
    return False


def is_english_slug(target: str) -> bool:
    """判断是否为英文 slug 链接"""
    if "/" in target:
        return False
    return bool(ENGLISH_SLUG_PATTERN.match(target))


def is_person_slug(target: str) -> bool:
    """判断是否为人名 slug 链接"""
    if "/" in target:
        return False
    return bool(PERSON_SLUG_PATTERN.match(target))


def fuzzy_match(target: str, index_normalized: dict, index_raw: dict) -> list:
    """
    尝试模糊匹配目标链接到实际文件。
    返回匹配到的 [(rel_path, basename), ...]
    """
    target_norm = normalize_name(target)
    if not target_norm or len(target_norm) < 2:
        return []

    matches = []

    # 1. 精确规范化匹配
    if target_norm in index_normalized:
        matches.extend(index_normalized[target_norm])
        return matches

    # 2. 关键词拆分匹配：把目标按 - 拆分，逐个关键词匹配
    target_parts = set(p for p in target_norm.split("-") if len(p) >= 2)
    if len(target_parts) >= 2:
        scored_matches = []
        for norm_name, files in index_normalized.items():
            if not norm_name or len(norm_name) < 2:
                continue
            name_parts = set(p for p in norm_name.split("-") if len(p) >= 2)
            if not name_parts:
                continue
            overlap = len(target_parts & name_parts)
            if overlap >= 2:
                score = overlap / max(len(target_parts), len(name_parts))
                # 排除过于通用的短文件名（如只有2-3个字符的）
                if len(norm_name) >= 4:
                    scored_matches.append((score, files))
        scored_matches.sort(key=lambda x: -x[0])
        if scored_matches and scored_matches[0][0] >= 0.6:
            matches = scored_matches[0][1]
            return matches

    # 3. 子串匹配：目标和文件名互相包含（要求至少4个字符以上的公共子串）
    for norm_name, files in index_normalized.items():
        if not norm_name or len(norm_name) < 4:
            continue
        if len(target_norm) < 4:
            continue
        if target_norm in norm_name or norm_name in target_norm:
            # 确保公共部分有意义（至少占目标的一半）
            common_len = min(len(target_norm), len(norm_name))
            if common_len >= 4 and common_len >= len(target_norm) * 0.5:
                matches.extend(files)

    return matches


# ============ 主流程 ============

def scan_all_links(index_normalized, index_raw):
    """扫描全库所有链接，返回断链清单"""
    all_links = []
    broken_links = []
    total_links = 0

    for root, dirs, files in os.walk(KB_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for f in files:
            if not f.endswith(".md"):
                continue
            filepath = Path(root) / f
            if should_exclude(filepath):
                continue

            try:
                content = filepath.read_text(encoding="utf-8")
            except Exception as e:
                print(f"  [WARN] 无法读取 {filepath}: {e}")
                continue

            links = extract_links_from_content(content)
            rel_path = str(filepath.relative_to(KB_ROOT))

            for link in links:
                total_links += 1
                target = link["target"]

                # 检查是否存在
                exists = False
                # 1. 原始 basename 匹配
                if target in index_raw:
                    exists = True
                # 2. 规范化匹配
                elif normalize_name(target) in index_normalized:
                    exists = True
                # 3. 路径式链接：检查作为相对路径是否存在
                elif "/" in target:
                    candidate = KB_ROOT / (target if target.endswith(".md") else target + ".md")
                    if candidate.exists():
                        exists = True

                if not exists:
                    broken_links.append({
                        "source_file": rel_path,
                        "line": link["line"],
                        "target": target,
                        "full_match": link["full_match"],
                        "raw_inner": link["raw_inner"],
                        "char_start": link["char_start"],
                        "char_end": link["char_end"],
                    })

                all_links.append({
                    "source_file": rel_path,
                    "target": target,
                    "exists": exists,
                })

    return all_links, broken_links, total_links


def classify_broken(broken_links, index_normalized, index_raw):
    """
    对断链进行分类：
    - auto_fixable: 可自动修正（有精确或高置信模糊匹配）
    - fuzzy_fixable: 模糊匹配可修正
    - legacy_delete: 历史遗留旧路径，删除链接保留文字
    - english_slug_delete: 英文slug，删除链接保留文字
    - person_slug_delete: 人名slug，删除链接保留文字
    - pending: 待确认
    """
    classifications = {
        "auto_fixable": [],   # 高置信度可自动修复
        "fuzzy_fixable": [],  # 模糊匹配，需谨慎
        "legacy_delete": [],  # 历史旧路径，删除链接
        "english_slug_delete": [],  # 英文slug，删除链接
        "person_slug_delete": [],    # 人名slug，删除链接
        "dir_link_delete": [],  # 目录式链接，删除链接
        "old_date_delete": [],   # 日期前缀旧链接，删除链接
        "old_project_delete": [], # 旧项目文档链接，删除链接
        "pending": [],        # 待确认
    }

    for bl in broken_links:
        target = bl["target"]

        # 0. 先查明确映射表（最高优先级）
        if target in EXPLICIT_LINK_MAP:
            suggested = EXPLICIT_LINK_MAP[target]
            if suggested in index_raw:
                bl["suggested_basename"] = suggested
                bl["suggested_path"] = index_raw[suggested][0]
                classifications["auto_fixable"].append(bl)
                continue

        # 1. 先判断已知的删除类别（这些不需要尝试匹配）
        if is_legacy_link(target):
            classifications["legacy_delete"].append(bl)
            continue
        if is_person_slug(target):
            classifications["person_slug_delete"].append(bl)
            continue
        if is_english_slug(target):
            # 英文 slug 先尝试通过映射表找中文笔记
            if target in EN_SLUG_TO_CHINESE:
                cn_name = EN_SLUG_TO_CHINESE[target]
                # 先查明确映射
                if cn_name in index_raw:
                    bl["suggested_basename"] = cn_name
                    bl["suggested_path"] = index_raw[cn_name][0]
                    classifications["auto_fixable"].append(bl)
                    continue
                cn_matches = fuzzy_match(cn_name, index_normalized, index_raw)
                if cn_matches:
                    unique_cn = set(m[1] for m in cn_matches)
                    if len(unique_cn) == 1:
                        bl["suggested_basename"] = list(unique_cn)[0]
                        bl["suggested_path"] = cn_matches[0][0]
                        classifications["auto_fixable"].append(bl)
                        continue
            classifications["english_slug_delete"].append(bl)
            continue
        if DATE_PREFIX_PATTERN.match(target):
            classifications["old_date_delete"].append(bl)
            continue
        if OLD_PROJECT_DOC_PATTERN.match(target):
            classifications["old_project_delete"].append(bl)
            continue
        if DIR_LINK_PATTERN.match(target) and "/" not in target:
            classifications["dir_link_delete"].append(bl)
            continue

        # 2. 再尝试模糊匹配
        matches = fuzzy_match(target, index_normalized, index_raw)

        if matches:
            unique_targets = set(m[1] for m in matches)
            if len(unique_targets) == 1:
                bl["suggested_basename"] = list(unique_targets)[0]
                bl["suggested_path"] = matches[0][0]
                classifications["auto_fixable"].append(bl)
            else:
                bl["suggested_matches"] = matches[:5]
                classifications["fuzzy_fixable"].append(bl)
        else:
            classifications["pending"].append(bl)

    return classifications


def fix_links_in_file(filepath: Path, fixes: list, dry_run: bool = False):
    """
    在单个文件中应用链接修复。
    fixes: [{"old": "[[xxx]]", "new": "[[yyy]] 或纯文字"}, ...]
    返回修复数量
    """
    if not fixes:
        return 0

    content = filepath.read_text(encoding="utf-8")
    original_content = content
    fix_count = 0

    # 按 char 位置倒序修复，避免位置偏移
    fixes_sorted = sorted(fixes, key=lambda x: -x["char_start"])

    for fix in fixes_sorted:
        old_text = fix["old_text"]
        new_text = fix["new_text"]
        # 验证 old_text 在预期位置
        start = fix["char_start"]
        end = fix["char_end"]
        if start < len(content) and content[start:end] == old_text:
            content = content[:start] + new_text + content[end:]
            fix_count += 1
        else:
            # 位置不匹配，尝试全文替换（第一次出现）
            if old_text in content:
                content = content.replace(old_text, new_text, 1)
                fix_count += 1

    if not dry_run and fix_count > 0:
        filepath.write_text(content, encoding="utf-8")

    return fix_count


def backup_file(filepath: Path):
    """备份文件到备份目录"""
    rel_path = filepath.relative_to(KB_ROOT)
    backup_path = BACKUP_DIR / rel_path
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(filepath, backup_path)


def main():
    parser = argparse.ArgumentParser(description="Obsidian 断链扫描与修复")
    parser.add_argument("--scan", action="store_true", help="仅扫描")
    parser.add_argument("--fix", action="store_true", help="执行修复")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不实际修改文件")
    args = parser.parse_args()

    mode = "scan" if args.scan else ("fix" if args.fix else "all")
    dry_run = args.dry_run

    print("=" * 60)
    print("Obsidian 断链扫描与修复工具")
    print(f"知识库根目录: {KB_ROOT}")
    print(f"模式: {'仅扫描' if mode == 'scan' else ('修复' if mode == 'fix' else '扫描+修复')}")
    print(f"试运行: {'是' if dry_run else '否（实际修改文件）'}")
    print("=" * 60)

    # 1. 构建文件索引
    print("\n[1/5] 构建全库文件索引...")
    index_normalized, index_raw, all_files = build_file_index()
    print(f"  共索引 {len(all_files)} 个 Markdown 文件")

    # 2. 扫描所有链接
    print("\n[2/5] 扫描全库双链...")
    all_links, broken_links, total_links = scan_all_links(index_normalized, index_raw)
    broken_rate = len(broken_links) / total_links * 100 if total_links > 0 else 0
    print(f"  总链接数: {total_links}")
    print(f"  断链数: {len(broken_links)} ({broken_rate:.1f}%)")

    # 3. 分类断链
    print("\n[3/5] 分类断链...")
    classifications = classify_broken(broken_links, index_normalized, index_raw)
    for cat, items in classifications.items():
        print(f"  {cat}: {len(items)}")

    if mode == "scan":
        print("\n[扫描模式] 输出断链清单：")
        for bl in broken_links:
            print(f"  [{bl['source_file']}:{bl['line']}] {bl['full_match']}")
        return

    # 4. 执行修复
    print("\n[4/5] 执行修复...")
    if not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        print(f"  备份目录: {BACKUP_DIR}")

    # 按文件分组修复操作
    file_fixes = defaultdict(list)
    fixed_count = 0
    deleted_count = 0
    pending_count = 0

    # 4a. 自动可修复的链接
    for item in classifications["auto_fixable"]:
        old_text = item["full_match"]
        new_basename = item["suggested_basename"]
        # 保留别名部分
        raw_inner = item["raw_inner"]
        if "|" in raw_inner:
            alias = raw_inner.split("|", 1)[1]
            new_text = f"[[{new_basename}|{alias}]]"
        else:
            new_text = f"[[{new_basename}]]"

        filepath = KB_ROOT / item["source_file"]
        file_fixes[str(filepath)].append({
            "old_text": old_text,
            "new_text": new_text,
            "char_start": item["char_start"],
            "char_end": item["char_end"],
            "type": "auto_fix",
        })
        fixed_count += 1

    # 4b. 模糊匹配可修复的（也自动修复，但置信度稍低）
    for item in classifications["fuzzy_fixable"]:
        if item.get("suggested_matches"):
            # 取第一个匹配
            best = item["suggested_matches"][0]
            new_basename = best[1]
            old_text = item["full_match"]
            raw_inner = item["raw_inner"]
            if "|" in raw_inner:
                alias = raw_inner.split("|", 1)[1]
                new_text = f"[[{new_basename}|{alias}]]"
            else:
                new_text = f"[[{new_basename}]]"

            filepath = KB_ROOT / item["source_file"]
            file_fixes[str(filepath)].append({
                "old_text": old_text,
                "new_text": new_text,
                "char_start": item["char_start"],
                "char_end": item["char_end"],
                "type": "fuzzy_fix",
            })
            fixed_count += 1

    # 4c. 历史遗留链接 → 删除 [[ ]] 保留文字
    for category in ["legacy_delete", "english_slug_delete", "person_slug_delete",
                      "dir_link_delete", "old_date_delete", "old_project_delete"]:
        for item in classifications[category]:
            old_text = item["full_match"]
            raw_inner = item["raw_inner"]
            # 保留显示文字：有别名用别名，没有就用目标名
            if "|" in raw_inner:
                display_text = raw_inner.split("|", 1)[1]
            else:
                display_text = raw_inner
            new_text = display_text

            filepath = KB_ROOT / item["source_file"]
            file_fixes[str(filepath)].append({
                "old_text": old_text,
                "new_text": new_text,
                "char_start": item["char_start"],
                "char_end": item["char_end"],
                "type": "delete_link",
            })
            deleted_count += 1

    # 4d. 待确认的（暂不处理）
    pending_count = len(classifications["pending"])

    # 执行文件级修复
    print(f"  待修复文件数: {len(file_fixes)}")
    for filepath_str, fixes in file_fixes.items():
        filepath = Path(filepath_str)
        if not dry_run:
            backup_file(filepath)
        count = fix_links_in_file(filepath, fixes, dry_run=dry_run)
        if dry_run:
            print(f"    [DRY-RUN] {filepath.relative_to(KB_ROOT)}: {count} 处修改")

    print(f"\n  修复链接数: {fixed_count}")
    print(f"  删除链接数: {deleted_count}")
    print(f"  待确认数: {pending_count}")

    # 5. 重新扫描验证
    print("\n[5/5] 重新扫描验证...")
    if not dry_run:
        index_normalized2, index_raw2, all_files2 = build_file_index()
        all_links2, broken_links2, total_links2 = scan_all_links(index_normalized2, index_raw2)
        new_broken_rate = len(broken_links2) / total_links2 * 100 if total_links2 > 0 else 0
        print(f"  修复后总链接数: {total_links2}")
        print(f"  修复后断链数: {len(broken_links2)} ({new_broken_rate:.1f}%)")
    else:
        broken_links2 = broken_links
        total_links2 = total_links
        new_broken_rate = broken_rate
        print("  [DRY-RUN] 跳过实际验证")

    # 6. 生成报告
    print("\n生成修复报告...")
    report_lines = []
    report_lines.append("# Obsidian 断链修复报告")
    report_lines.append("")
    report_lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"**知识库根目录**: `{KB_ROOT}`")
    report_lines.append(f"**运行模式**: {'试运行（未实际修改）' if dry_run else '实际修复'}")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 一、总览")
    report_lines.append("")
    report_lines.append(f"| 指标 | 数值 |")
    report_lines.append(f"|---|---|")
    report_lines.append(f"| 总链接数 | {total_links} |")
    report_lines.append(f"| 修复前断链数 | {len(broken_links)} |")
    report_lines.append(f"| 修复前断链率 | {broken_rate:.1f}% |")
    report_lines.append(f"| 自动修复数 | {fixed_count} |")
    report_lines.append(f"| 删除链接数（历史遗留） | {deleted_count} |")
    report_lines.append(f"| 保留待确认数 | {pending_count} |")
    report_lines.append(f"| 修复后断链数 | {len(broken_links2) if not dry_run else 'N/A'} |")
    report_lines.append(f"| 修复后断链率 | {new_broken_rate:.1f}% |" if not dry_run else "| 修复后断链率 | N/A |")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 二、断链分类统计")
    report_lines.append("")
    report_lines.append(f"| 类别 | 数量 | 处理方式 |")
    report_lines.append(f"|---|---|---|")
    report_lines.append(f"| 可自动修复（精确/高置信匹配） | {len(classifications['auto_fixable'])} | 修正为实际文件名 |")
    report_lines.append(f"| 模糊匹配修复 | {len(classifications['fuzzy_fixable'])} | 按最佳匹配修正 |")
    report_lines.append(f"| 历史旧路径链接 | {len(classifications['legacy_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 英文 slug 链接 | {len(classifications['english_slug_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 人名 slug 链接 | {len(classifications['person_slug_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 目录式链接 | {len(classifications['dir_link_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 日期前缀旧链接 | {len(classifications['old_date_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 旧项目文档链接 | {len(classifications['old_project_delete'])} | 删除 [[ ]] 保留文字 |")
    report_lines.append(f"| 待确认 | {len(classifications['pending'])} | 暂不处理，人工确认 |")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 三、修复明细（自动修复）")
    report_lines.append("")
    if classifications["auto_fixable"]:
        report_lines.append("| 来源文件 | 行号 | 原链接 | 修正为 |")
        report_lines.append("|---|---|---|---|")
        for item in classifications["auto_fixable"][:50]:  # 只列前50条
            report_lines.append(f"| {item['source_file']} | {item['line']} | `{item['full_match']}` | `[[{item['suggested_basename']}]]` |")
        if len(classifications["auto_fixable"]) > 50:
            report_lines.append(f"\n... 共 {len(classifications['auto_fixable'])} 条，仅展示前50条")
    else:
        report_lines.append("（无自动修复项）")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 四、删除链接明细（历史遗留）")
    report_lines.append("")
    if any([classifications["legacy_delete"], classifications["english_slug_delete"],
            classifications["person_slug_delete"], classifications["dir_link_delete"],
            classifications["old_date_delete"], classifications["old_project_delete"]]):
        report_lines.append("| 来源文件 | 行号 | 原链接 | 类别 |")
        report_lines.append("|---|---|---|---|")
        for cat_name, cat_label in [
            ("legacy_delete", "历史旧路径"),
            ("english_slug_delete", "英文slug"),
            ("person_slug_delete", "人名slug"),
            ("dir_link_delete", "目录式链接"),
            ("old_date_delete", "日期前缀旧链接"),
            ("old_project_delete", "旧项目文档"),
        ]:
            for item in classifications[cat_name][:30]:
                report_lines.append(f"| {item['source_file']} | {item['line']} | `{item['full_match']}` | {cat_label} |")
    else:
        report_lines.append("（无删除项）")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 五、剩余断链明细（待确认）")
    report_lines.append("")
    if classifications["pending"]:
        report_lines.append("| 来源文件 | 行号 | 断链目标 |")
        report_lines.append("|---|---|---|")
        for item in classifications["pending"]:
            report_lines.append(f"| {item['source_file']} | {item['line']} | `{item['target']}` |")
    else:
        report_lines.append("（无待确认断链）")
    report_lines.append("")

    # 写入报告
    report_text = "\n".join(report_lines)
    if not dry_run:
        REPORT_PATH.write_text(report_text, encoding="utf-8")
        print(f"  报告已保存: {REPORT_PATH}")
    else:
        print("\n--- 报告预览 ---")
        print(report_text[:2000])

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
