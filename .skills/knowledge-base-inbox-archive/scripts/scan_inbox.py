#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库收件箱扫描辅助脚本（手动分拣候选清单生成器）

用途：用户手动触发「归档收件箱」时先跑本脚本，扫描 05-收件箱，
输出结构化《分拣候选清单》（Markdown），供 AI 按内容放置路由表补「建议去向」，
列清单给用户确认后执行落位。

铁律：本脚本【只扫描、不移动、不删除、不改写】任何文件。
落位动作永远由 AI 提议 + 用户确认后执行。

输出：
  1. stdout 打印摘要
  2. 清单落 `00-天一生水/01-系统文档/收件箱分拣/分拣候选清单-YYYY-MM-DD.md`
"""
import os
import sys
import glob
import datetime

VAULT = "/Users/panda/Desktop/knowledge-base"
INBOX = os.path.join(VAULT, "05-收件箱")
OUT_DIR = os.path.join(VAULT, "00-天一生水/01-系统文档/收件箱分拣")

# 过程垃圾标记（转录类 skill 遗留，落位前必须清理）
# 注意：目录与文件分开两个集合；.DS_Store 是文件，只放 JUNK_FILES
JUNK_DIRS = {".venv", ".venv-course-docs", ".tmp_seg", "__pycache__"}
JUNK_FILES = {".DS_Store", "Thumbs.db"}


def fmt_size(n):
    """字节 → 人类可读体积"""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"


def dir_size(path):
    """递归统计目录体积"""
    total = 0
    for root, dirs, files in os.walk(path):
        # 不进入过程垃圾目录统计（它们本就不该入库）
        dirs[:] = [d for d in dirs if d not in JUNK_DIRS]
        for fn in files:
            if fn in JUNK_FILES:
                continue
            try:
                total += os.path.getsize(os.path.join(root, fn))
            except OSError:
                pass
    return total


def has_junk(path):
    """检测条目内是否含过程垃圾"""
    found = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d in JUNK_DIRS:
                found.append(os.path.join(os.path.relpath(root, path), d))
        for fn in files:
            if fn in JUNK_FILES:
                found.append(os.path.join(os.path.relpath(root, path), fn))
    return found


def scan():
    if not os.path.isdir(INBOX):
        print(f"❌ 收件箱不存在：{INBOX}")
        sys.exit(1)

    entries = []
    skipped_junk = []  # 顶级过程垃圾目录（收件箱直接子项），只记录不删
    for name in sorted(os.listdir(INBOX)):
        p = os.path.join(INBOX, name)
        if name in JUNK_FILES:
            continue
        # 顶级垃圾目录：不进候选清单，仅提示（落位时由 AI 一并清理）
        if name in JUNK_DIRS and os.path.isdir(p):
            skipped_junk.append(name)
            continue
        if os.path.isdir(p):
            # 成品目录后缀表：命中即先标「成品目录」，再按 md+图 结构精确判
            # 可扩展：新增转录类 skill 的命名后缀时在此追加
            shape = "成品目录" if name.endswith(("课程文档", "第一课", "实操篇", "认知篇", "落地篇")) else "目录"
            # 判断是否成品：含 .md + imgs/ 的课程转录结构
            mds = glob.glob(os.path.join(p, "*.md"))
            imgs = os.path.isdir(os.path.join(p, "imgs")) or os.path.isdir(os.path.join(p, "images"))
            if mds and imgs:
                shape = "成品（md+图）"
            size = dir_size(p)
            junk = has_junk(p)
            mtime = datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()
            entries.append({"name": name, "shape": shape, "size": fmt_size(size),
                            "size_raw": size, "mtime": mtime, "junk": junk, "is_dir": True})
        else:
            size = os.path.getsize(p)
            mtime = datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat()
            shape = "散件md" if name.endswith(".md") else "散件文件"
            entries.append({"name": name, "shape": shape, "size": fmt_size(size),
                            "size_raw": size, "mtime": mtime, "junk": [], "is_dir": False})

    total_raw = sum(e["size_raw"] for e in entries)
    today = datetime.date.today().isoformat()

    L = []
    L.append(f"# 收件箱分拣候选清单 {today}")
    L.append("")
    L.append(f"> 扫描范围：`{INBOX}` | 共 {len(entries)} 条 | 总有效体积约 {fmt_size(total_raw)}")
    L.append("> 本清单由 `scan_inbox.py` 自动生成（只扫描，不移动/不删除）。")
    L.append("> AI 按《内容放置路由表》（06_知识库Skill优化计划 §五）补「建议去向」，用户确认后落位。")
    L.append("")
    L.append("## 候选清单")
    L.append("")
    L.append("| # | 条目 | 形态 | 体积 | 日期 | 过程垃圾 | 建议去向 | 置信度 | 备注 |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for i, e in enumerate(entries, 1):
        junk_txt = "；".join(e["junk"]) if e["junk"] else "无"
        L.append(f"| {i} | {e['name']} | {e['shape']} | {e['size']} | {e['mtime']} | {junk_txt} |  |  |  |")
    L.append("")
    L.append("---")
    L.append("> 由 knowledge-base-inbox-archive skill 的 scan_inbox.py 生成。落位前请用户确认；涉及隐私/未定稿先不落位。")

    report = "\n".join(L)
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"分拣候选清单-{today}.md")
    # 同日重跑防覆盖：当日清单已存在时，旧版改名保留（加 -HHMM，过程数据留痕）
    if os.path.exists(out):
        ts = datetime.datetime.now().strftime("%H%M")
        old = os.path.join(OUT_DIR, f"分拣候选清单-{today}-{ts}.md")
        os.rename(out, old)
        print(f"↩️ 同日旧清单已改存：{old}")
    with open(out, "w", encoding="utf-8") as fp:
        fp.write(report)

    print(f"✅ 扫描完成：{out}")
    print(f"   共 {len(entries)} 条 | 总有效体积 {fmt_size(total_raw)}")
    if skipped_junk:
        print(f"   ⚠️ 跳过顶级过程垃圾目录（落位前需清理）：{'、'.join(skipped_junk)}")
    for e in entries:
        junk_txt = " ⚠️含垃圾" if e["junk"] else ""
        print(f"   - {e['name']} [{e['shape']} {e['size']} {e['mtime']}]{junk_txt}")


if __name__ == "__main__":
    scan()
