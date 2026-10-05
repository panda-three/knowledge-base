#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clean_and_stitch.py — 课程文档快照清洗与拼接

把浏览器滚动采集到的快照 JSON（list of {"sy":..,"txt":..}）清洗为完整正文。

清洗步骤（顺序重要）：
  1. 规范化行（去尾部零宽空格 U+200B / 空格）
  2. 摘除常驻左侧目录（TOC）：--toc-lines 显式指定，或自动检测公共前缀
  3. 截断评论区：从第一个评论者行（"名字 时间戳"）或"全文评论"起截断
  4. 删除页脚行（默认 "真诚点赞，手留余香"）与 UI 标签（PlainText / 复制）
  5. 后缀-前缀最大重叠拼接，去重相邻快照重叠内容
  6. （可选 --merge-lists）把 "•"/"◦" 与 "N."/"a." 序号与后续内容合并，方便转 Markdown

用法：
  python3 clean_and_stitch.py --snaps /tmp/snaps.json --out /tmp/clean.txt [--toc-lines 29] [--no-comment-cut]

注意：
  - 快照 JSON 结构必须为 list，每项含 "txt" 字段（建议同时带 "sy" 便于调试）
  - 若页面无评论区，用 --no-comment-cut 跳过截断
  - TOC 行数因站而异（yitang.top 两个文档分别约 23 / 29 行），页面每次可能变化：
    优先从浏览器观察（快照开头固定重复的块）后传 --toc-lines；不传时自动检测公共前缀。
"""
import argparse
import json
import re
import sys


def norm(line: str) -> str:
    return line.rstrip("\u200b ").strip()


def detect_toc(snaps_lines, min_len=5):
    """自动检测所有快照的公共前缀行数（即常驻目录）。不足 min_len 视为无目录。"""
    if not snaps_lines:
        return 0
    base = snaps_lines[0]
    k = 0
    for i in range(min(len(base), 400)):
        if all(len(sl) > i and sl[i] == base[i] for sl in snaps_lines):
            k = i + 1
        else:
            break
    return k if k >= min_len else 0


def cut_comments(lines, comment_re=None):
    """从第一个评论者行或"全文评论"起截断，返回截断后的行。"""
    if comment_re is None:
        comment_re = re.compile(r"^.+\s\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
    cut = None
    for i, l in enumerate(lines):
        if l.startswith("全文评论") or comment_re.match(l):
            cut = i
            break
    return lines[:cut] if cut is not None else lines


def stitch(lines_list):
    """后缀-前缀最大重叠拼接。"""
    acc = []
    for lines in lines_list:
        if not lines:
            continue
        if not acc:
            acc = list(lines)
            continue
        max_k = 0
        lim = min(len(acc), len(lines))
        for k in range(lim, 0, -1):
            if acc[-k:] == lines[:k]:
                max_k = k
                break
        acc.extend(lines[max_k:])
    return acc


def merge_markers(lines):
    """把 '•'/'◦' 与 'N.'/'a.' 序号与后续内容合并为单行，便于转 Markdown 列表。"""
    out = []
    i = 0
    n = len(lines)
    while i < n:
        l = lines[i]
        nxt = lines[i + 1] if i + 1 < n else None
        if l in ("•", "◦") and nxt and nxt.strip() and nxt not in ("•", "◦"):
            out.append("- " + nxt.strip())
            i += 2
            continue
        m = re.fullmatch(r"(\d+)\.", l.strip())
        if m and nxt and nxt.strip():
            out.append(f"{m.group(1)}. {nxt.strip()}")
            i += 2
            continue
        m = re.fullmatch(r"([a-z])\.", l.strip())
        if m and nxt and nxt.strip():
            out.append(f"{m.group(1)}. {nxt.strip()}")
            i += 2
            continue
        out.append(l)
        i += 1
    return out


def main():
    ap = argparse.ArgumentParser(description="课程文档快照清洗与拼接")
    ap.add_argument("--snaps", required=True, help="快照 JSON 文件路径")
    ap.add_argument("--out", default="", help="输出文件路径（默认 stdout）")
    ap.add_argument("--toc-lines", type=int, default=0, help="左侧目录行数，0=自动检测")
    ap.add_argument("--no-comment-cut", action="store_true", help="跳过评论区截断")
    ap.add_argument("--footers", default="真诚点赞，手留余香", help="页脚行，逗号分隔，可多个")
    ap.add_argument("--ui-labels", default="PlainText,复制", help="UI 标签行，逗号分隔")
    ap.add_argument("--merge-lists", action="store_true", help="合并 bullet/序号标记与后续内容")
    args = ap.parse_args()

    with open(args.snaps, encoding="utf-8") as f:
        snaps = json.load(f)

    snaps_lines = [[norm(l) for l in s["txt"].split("\n")] for s in snaps]

    toc_lines = args.toc_lines
    if toc_lines <= 0:
        toc_lines = detect_toc(snaps_lines)
    if toc_lines:
        snaps_lines = [sl[toc_lines:] if sl[:toc_lines] == snaps_lines[0][:toc_lines] else sl for sl in snaps_lines]

    footers = {x.strip() for x in args.footers.split(",") if x.strip()}
    ui_labels = {x.strip() for x in args.ui_labels.split(",") if x.strip()}

    cleaned = []
    for sl in snaps_lines:
        if not args.no_comment_cut:
            sl = cut_comments(sl)
        sl = [l for l in sl if l not in footers and l not in ui_labels]
        cleaned.append(sl)

    acc = stitch(cleaned)
    if args.merge_lists:
        acc = merge_markers(acc)

    full = "\n".join(acc)
    while full.startswith("\n"):
        full = full[1:]
    full = re.sub(r"\n{3,}", "\n\n", full)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(full)
        print(f"OK: {len(full)} chars -> {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(full)


if __name__ == "__main__":
    main()
