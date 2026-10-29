#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""find_related.py — 为指定笔记在全库检索最相关的候选笔记
无第三方依赖：中文用相邻 bigram、英文用单词，tf-idf 简化打分，标题命中加权。
用法:
    python3 find_related.py <笔记相对/绝对路径> [候选数，默认12]
输出: 按相关度排序的候选笔记（相对路径 + 得分 + 命中词），供 context-link Skill 判关系。
"""
import os, re, sys, math, glob
from collections import Counter

VAULT = "/Users/panda/Desktop/knowledge-base"
STOP = set("""我们 你们 他们 她们 这个 那个 这些 那些 这样 那样 什么 怎么 怎样 因为 所以 但是 可是
如果 就是 可以 应该 需要 一个 一些 没有 不是 还是 或者 以及 等等 自己 大家 觉得 可能 现在 时候
这边 那里 这里 真的 其实 然后 比如 的话 对于 关于 通过 进行 已经 不要 这么 那么 一下 这种 那种
的话 大家 自己 它们 什么 如何 为何 哪些 一点 这种 东西 事情 地方 样子 东西""".split())

def strip_noise(text):
    if text.startswith("---"):
        m = re.match(r"---\s*\n.*?\n---\s*\n", text, re.S)
        if m:
            text = text[m.end():]
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)          # 图片
    text = re.sub(r"https?://\S+", " ", text)                  # 链接
    text = re.sub(r"[#>*`|~_=]", " ", text)
    return text

def tokens(text):
    text = strip_noise(text)
    out = []
    for w in re.findall(r"[A-Za-z][A-Za-z0-9_]+", text):
        w = w.lower()
        if len(w) >= 2:
            out.append(w)
    for seg in re.findall(r"[\u4e00-\u9fff]+", text):
        for i in range(len(seg) - 1):
            bg = seg[i:i+2]
            if bg not in STOP:
                out.append(bg)
    return out

def main():
    if len(sys.argv) < 2:
        print("用法: python3 find_related.py <笔记路径> [候选数]")
        sys.exit(1)
    target = sys.argv[1]
    if not os.path.isabs(target):
        target = os.path.join(VAULT, target)
    topn = int(sys.argv[2]) if len(sys.argv) > 2 else 12

    all_files = [f for f in glob.glob(os.path.join(VAULT, "**/*.md"), recursive=True)
                 if os.path.exists(f) and os.path.abspath(f) != os.path.abspath(target)]

    target_text = open(target, encoding="utf-8", errors="ignore").read()
    target_tf = Counter(tokens(target_text))
    # 目标关键词：保留 tf>=1，取 top 40，避免长尾拖慢
    target_terms = {t for t, c in target_tf.most_common(40)}

    # 第一遍：全库 tf + 文档频率 df
    docs = {}
    df = Counter()
    for f in all_files:
        try:
            tf = Counter(tokens(open(f, encoding="utf-8", errors="ignore").read()))
        except Exception:
            continue
        docs[f] = tf
        for t in tf:
            df[t] += 1

    N = len(docs) + 1
    def idf(t):
        return math.log((N + 1) / (df.get(t, 0) + 1)) + 1.0

    # 标题 token（文件名）
    def title_tokens(f):
        name = os.path.basename(f)[:-3]
        return set(tokens(name))

    ttitle = title_tokens(target)
    scored = []
    for f, tf in docs.items():
        score = 0.0
        hits = []
        for t in target_terms:
            if t in tf:
                s = idf(t) * (1 + math.log(tf[t]))
                score += s
                hits.append(t)
        # 标题命中强加权
        ftitle = title_tokens(f)
        for t in ttitle & ftitle:
            score += 3.0 * idf(t)
        if score > 0:
            scored.append((score, f, hits))

    scored.sort(reverse=True)
    rel_t = os.path.relpath(target, VAULT)
    print(f"目标：{rel_t}")
    print(f"全库候选 {len(docs)} 篇，展示相关度前 {min(topn, len(scored))}：\n")
    for i, (s, f, hits) in enumerate(scored[:topn], 1):
        h = "、".join(hits[:8])
        print(f"{i:>2}. [{s:6.1f}] {os.path.relpath(f, VAULT)}")
        print(f"      命中：{h}")

if __name__ == "__main__":
    main()
