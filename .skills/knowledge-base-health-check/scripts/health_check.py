#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库体检脚本 — 扫描 /Users/panda/Desktop/knowledge-base 全维度健康
版本 2.0（2026-09-18 P0 修复，只修检测 bug、不降检测标准）：
  1. 断链/入链统计排除行内反引号教学文字（`[[...]]`）
  2. names 构造只删结尾 .md（修复 .md__hash 双后缀文件匹配错位），重复 basename 显式报告
  3. 相似标题排除：同名（去标点后）、openclaw 系统文件、版本序列（V+数字）
  4. read() 编码失败显式记录 READ_ERRORS，不再静默当空文件
  5. 新增文件名规范检测（.md.md 双后缀 / .md__ 中缀 / 非法字符），只报告不扣分
"""
import os, re, glob, datetime, difflib

VAULT = "/Users/panda/Desktop/knowledge-base"
OUT_DIR = os.path.join(VAULT, "00-天一生水/01-系统文档/知识库体检")
META_DIR = os.path.join(VAULT, "00-天一生水/01-系统文档/AI教育课沉淀/meta")
TODAY = datetime.date.today().isoformat()
ENGINE_VERSION = "2.0 (2026-09-18 P0)"
READ_ERRORS = []

def all_md():
    return [f for f in glob.glob(os.path.join(VAULT, "**/*.md"), recursive=True)]

def rel(f):
    return os.path.relpath(f, VAULT)

def read(f):
    try:
        with open(f, encoding="utf-8") as fp:
            return fp.read()
    except Exception as e:
        READ_ERRORS.append((rel(f), str(e)))
        return ""

def is_code_block_clean(text):
    """去除代码块后的文本"""
    return re.sub(r"```.*?```", "", text, flags=re.S)

def strip_inline_code(text):
    """去除行内反引号代码（教学文字如 `[[双链]]`，Obsidian 不渲染为链接）"""
    return re.sub(r"`[^`\n]*`", "", text)

def link_clean_text(text):
    """链接统计用文本：先剥代码块，再剥行内反引号"""
    return strip_inline_code(is_code_block_clean(text))

def strip_trailing_md(name):
    """只删结尾的 .md（保留 .md__hash 中缀）"""
    return name[:-3] if name.endswith(".md") else name

def extract_links(text):
    return re.findall(r"\[\[([^\]|#]+)", text)

def levenshtein(a, b):
    m, n = len(a), len(b)
    d = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): d[i][0] = i
    for j in range(n+1): d[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+(a[i-1]!=b[j-1]))
    return d[m][n]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = all_md()
    n = len(files)
    names = {os.path.basename(f).replace(".md",""): f for f in files}

    # 1. 断链
    broken = []
    total_links = 0
    # names：只删结尾 .md，保留 .md__hash 中缀；同名冲突显式记录（链接歧义，不算断链）
    names = {}
    name_conflicts = []
    for f in files:
        key = strip_trailing_md(os.path.basename(f))
        if key in names:
            name_conflicts.append((key, names[key], f))
        else:
            names[key] = f
    for f in files:
        # meta 报告文件中的描述性 [[ 不参与断链统计（仍保留其自身被其他维度检查）
        if os.path.dirname(f).startswith(META_DIR):
            continue
        text = link_clean_text(read(f))
        for l in extract_links(text):
            total_links += 1
            name = strip_trailing_md(l.strip().split("/")[-1])
            if name not in names:
                broken.append((rel(f), l))
    broken_rate = len(broken) / max(total_links, 1) * 100

    # 2. 入链/出链（孤儿 & 枢纽）
    inlinks = {f: 0 for f in files}
    outlinks = {f: 0 for f in files}
    for f in files:
        text = link_clean_text(read(f))
        ls = extract_links(text)
        outlinks[f] = len(ls)
        for l in ls:
            name = strip_trailing_md(l.strip().split("/")[-1])
            if name in names:
                inlinks[names[name]] += 1
    orphans = [rel(f) for f in files if inlinks[f]==0 and outlinks[f]==0]
    hubs = sorted(files, key=lambda f: -inlinks[f])[:10]

    # 3. 质量
    empty, tiny, no_yaml, no_source = [], [], [], []
    for f in files:
        size = os.path.getsize(f)
        text = read(f)
        if size < 100: empty.append((rel(f), size))
        elif size < 500 and not text.lstrip().startswith("---"): tiny.append((rel(f), size))
        if not text.lstrip().startswith("---"): no_yaml.append(rel(f))
        elif "source:" not in text.split("---",2)[1]: no_source.append(rel(f))

    # 4. 冗余
    pointers, dup_names, huge = [], [], []
    for f in files:
        text = read(f)
        low = text[:800]
        if "type: 指针" in low or "本文件为指针" in low:
            pointers.append(rel(f))
        size = os.path.getsize(f)
        if size > 200*1024: huge.append((rel(f), size//1024))
    # 相似标题（P0：排除同名模板/openclaw 系统文件/版本序列——均非内容级重复）
    bases = [(rel(f), re.sub(r"[\s：:·—\-（）()]", "", os.path.basename(f).replace(".md",""))) for f in files]
    dup_names = []
    for i in range(len(bases)):
        for j in range(i+1, len(bases)):
            a, b = bases[i][1], bases[j][1]
            if not a or not b: continue
            if a == b: continue  # 去标点后同名 → 不同目录模板，不算重复
            if "openclaw" in bases[i][0] or "openclaw" in bases[j][0]: continue  # 系统文件
            if re.search(r"V\d+(\.\d+)*", a) or re.search(r"V\d+(\.\d+)*", b): continue  # 版本序列
            sim = 1 - levenshtein(a,b)/max(len(a),len(b))
            if sim > 0.92 and abs(len(a)-len(b)) < 6:
                dup_names.append((bases[i][0], bases[j][0], round(sim,2)))

    # 文件名规范（基本法 2.1：禁 .md.md 双后缀/中缀、非法字符）——只报告不扣分
    naming_bad = []
    for f in files:
        base = os.path.basename(f)
        r = rel(f)
        if base.endswith(".md.md") or ".md__" in base:
            naming_bad.append((r, "双后缀/中缀（基本法 2.1）"))
        bad = sorted(set(re.findall(r"[\\/:*?\"<>|\x00-\x1f]", base)))
        if bad:
            naming_bad.append((r, f"非法字符 {' '.join(bad)}"))

    # 5. 时效
    stale, inbox_stale = [], []
    cutoff90 = datetime.datetime.now().timestamp() - 90*86400
    cutoff30 = datetime.datetime.now().timestamp() - 30*86400
    for f in files:
        m = os.path.getmtime(f)
        if m < cutoff90: stale.append((rel(f), datetime.date.fromtimestamp(m).isoformat()))
        if "05-收件箱" in f and m < cutoff30: inbox_stale.append(rel(f))

    # 6. 新增 & 价值
    recent = []
    cutoff14 = datetime.datetime.now().timestamp() - 14*86400
    for f in files:
        if os.path.getmtime(f) > cutoff14: recent.append(rel(f))
    valuable_orphans = [rel(f) for f in files if inlinks[f]==0 and os.path.getsize(f) > 5*1024]

    # 7. 结构分布
    dirs = {}
    for f in files:
        top = rel(f).split("/")[0]
        dirs[top] = dirs.get(top, 0) + 1
    root_files = [rel(f) for f in files if rel(f).count("/")==0]

    # 评分
    score = 100.0
    score -= min(broken_rate * 3, 30)          # 结构
    score -= min(len(no_yaml) * 0.5, 15)       # 质量
    score -= min(len(no_source) * 0.3, 15)
    score -= min(len(pointers) * 2, 15)        # 冗余
    score -= min(len(empty) * 2, 10)
    score -= min(len(inbox_stale) * 2, 5)      # 时效
    score -= min(len(stale) * 0.2, 10)         # 时效
    score = max(0, round(score, 1))

    L = []
    L.append(f"# 知识库体检报告 {TODAY}")
    L.append("")
    L.append(f"> 扫描范围：`{VAULT}` | 共 {n} 个 .md 文件 | 体检引擎 v{ENGINE_VERSION}")
    L.append("")
    L.append(f"## 健康总分：**{score}/100**")
    L.append("")
    L.append(f"**一句话结论：** " + ("结构健康，质量良好。" if score >= 85 else "存在需处理问题，见下方清单。" if score >= 60 else "结构异常，需优先修复红线项。"))
    if READ_ERRORS:
        L.append("")
        L.append("> ⚠️ 以下文件读取失败（编码/损坏），结果可能不完整：")
        for r, err in READ_ERRORS[:10]:
            L.append(f"> - `{r}`：{err}")
    L.append("")
    L.append("## 一、结构健康")
    L.append("")
    L.append(f"- 双链总数：{total_links}，断链：**{len(broken)}**（断链率 **{broken_rate:.1f}%**）" + (" 🔴 超红线 5%" if broken_rate > 5 else ""))
    L.append(f"- 孤儿笔记（无入链无出链）：{len(orphans)}")
    L.append(f"- 根目录散文件：{len(root_files)}")
    if name_conflicts:
        L.append(f"- 同名文件 {len(name_conflicts)} 处（链接有歧义，需人工确认）：")
        for k, p1, p2 in name_conflicts[:10]:
            L.append(f"  - `{k}`：`{p1}` 与 `{p2}`")
    if naming_bad:
        L.append(f"- 文件名不规范（基本法 2.1）：{len(naming_bad)}")
        for r, why in naming_bad[:20]:
            L.append(f"  - {r} —— {why}")
    if broken:
        L.append("")
        L.append("### 断链明细")
        for f, l in broken[:30]:
            # 明细文本转义：换行折叠、半角方括号转全角，避免报告自身再次产生 [[ 链接语法
            l_disp = l.replace("\n", " ⏎ ").replace("[", "［").replace("]", "］").replace("|", "｜")
            L.append(f"- `{f}` → `{l_disp}`")
    if orphans:
        L.append("")
        L.append("### 孤儿明细")
        for o in orphans[:30]: L.append(f"- {o}")
    L.append("")
    L.append("## 二、质量合规")
    L.append("")
    L.append(f"- 空文件（<100B）：{len(empty)} | 疑似垃圾小文件（<500B无YAML）：{len(tiny)}")
    L.append(f"- 无 YAML：{len(no_yaml)} | 缺 source：{len(no_source)}")
    for f, s in empty[:20]: L.append(f"  - 空: {f} ({s}B)")
    for f, s in tiny[:20]: L.append(f"  - 小: {f} ({s}B)")
    L.append("")
    L.append("## 三、冗余检测")
    L.append("")
    L.append(f"- 指针/骨架文件：{len(pointers)}")
    for p in pointers: L.append(f"  - {p}")
    L.append(f"- 高度相似标题（疑似重复）：{len(dup_names)}")
    for a, b, s in dup_names[:20]: L.append(f"  - {a} ≈ {b}（相似度 {s}）")
    L.append(f"- 超大文件（>200KB）：{len(huge)}")
    for f, kb in huge: L.append(f"  - {f}（{kb}KB）")
    L.append("")
    L.append("## 四、时效")
    L.append("")
    L.append(f"- 90 天未更新：{len(stale)} | 收件箱超 30 天未清：{len(inbox_stale)}")
    for f, d in stale[:20]: L.append(f"  - {f}（最后更新 {d}）")
    for f in inbox_stale[:10]: L.append(f"  - 收件箱滞留: {f}")
    L.append("")
    L.append("## 五、价值评估")
    L.append("")
    L.append(f"- 近 14 天新增/更新：{len(recent)} 篇")
    for r in recent[:20]: L.append(f"  - {r}")
    L.append("")
    L.append("### 枢纽笔记（入链 Top10）")
    for f in hubs:
        L.append(f"- {rel(f)}（入链 {inlinks[f]}）")
    L.append("")
    L.append(f"- 零入链但有实质内容（>5KB，潜在高价值孤儿）：{len(valuable_orphans)}")
    for v in valuable_orphans[:20]: L.append(f"  - {v}")
    L.append("")
    L.append("## 六、结构分布")
    L.append("")
    L.append("| 目录 | 文件数 |")
    L.append("|---|---|")
    for d, c in sorted(dirs.items(), key=lambda x: -x[1]):
        L.append(f"| {d} | {c} |")
    L.append("")
    L.append("## 七、清理候选清单（待用户确认，不自动删除）")
    L.append("")
    for p in pointers: L.append(f"- [ ] 指针文件 {p} —— 完整转写后冗余，建议删除（确认后）")
    for f, s in empty: L.append(f"- [ ] 空文件 {f} —— 建议删除（确认后）")
    for f, s in tiny: L.append(f"- [ ] 小文件 {f} —— 疑似垃圾，建议人工查看后删除（确认后）")
    for a, b, s in dup_names[:20]: L.append(f"- [ ] 疑似重复 {a} ≈ {b} —— 建议合并或删除其一（确认后）")
    for r, why in naming_bad[:20]: L.append(f"- [ ] 文件名不规范 {r} —— {why}，建议重命名（确认后）")
    if not (pointers or empty or tiny or dup_names or naming_bad):
        L.append("- （无）")
    L.append("")
    L.append("---")
    L.append("> 由 knowledge-base-health-check skill 自动生成（引擎 v" + ENGINE_VERSION + "）。删除/移动任何文件前必须经用户确认。")

    report = "\n".join(L)
    out = os.path.join(OUT_DIR, f"体检报告-{TODAY}.md")
    with open(out, "w", encoding="utf-8") as fp:
        fp.write(report)
    print(f"✅ 体检完成：{out}")
    print(f"   引擎 v{ENGINE_VERSION} | 总分 {score}/100 | 断链率 {broken_rate:.1f}% | 空文件 {len(empty)} | 指针 {len(pointers)} | 相似标题 {len(dup_names)} | 命名不规范 {len(naming_bad)} | 读取失败 {len(READ_ERRORS)}")

if __name__ == "__main__":
    main()
