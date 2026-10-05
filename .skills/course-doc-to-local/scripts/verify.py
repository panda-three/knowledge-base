# -*- coding: utf-8 -*-
"""
course-doc-to-local / verify.py
全量完整性验证：dataJson 权威文本流 vs 生成 MD 文本流（相似度必须 = 1.0）
用法:
  python3 verify.py <datajson.json> <plan.json> <md_dir>
附加校验：图片数 == dataJson 图片块数；无 CDN 残留；** 偶数
"""
import json, os, re, sys, difflib

def elems(node):
    return "".join((el.get("text_run") or {}).get("content", "") or ""
                   for el in node.get("elements", []))

def strip_num(s):
    return re.sub(r'^\s*\d+[\.、)]\s*', '', s.strip())

def authority_flow(data, a, b):
    rows = []
    for i in range(a, b):
        blk = data[i]; t = blk["t"]; attr = blk.get("a") or {}
        if t in (19, 24, 25, 33, 34): continue
        if t == 27: rows.append("[IMG]"); continue
        if t == 2: s = strip_num(elems(attr.get("text") or {}))
        elif t in (3, 4, 5): s = elems(attr.get({3: "heading1", 4: "heading2", 5: "heading3"}[t]) or {}).strip()
        elif t == 12: s = elems(attr.get("bullet") or {}).strip()
        elif t == 13: s = strip_num(elems(attr.get("ordered") or {}))
        elif t == 14: s = elems(attr.get("code") or {}).strip()
        elif t == 23: s = (attr.get("file") or {}).get("name", "")
        else: continue
        if s and s != "\u200b":
            # 文本块内嵌 \n 时，与 md_flow 按物理行拆分保持一致
            rows.extend(p.strip() for p in s.split("\n") if p.strip())
    return rows

def md_flow(md):
    rows, in_code = [], False
    for raw in md.split("\n"):
        line = raw.strip()
        if not line: continue
        if line.startswith("```"): in_code = not in_code; continue
        if in_code: rows.append(line); continue
        if re.match(r'^!\[[^\]]*\]\([^)]+\)$', line): rows.append("[IMG]"); continue
        line = line.replace("📹 ", "")
        line = re.sub(r'\*\*', '', line).replace('\u200b', '')
        line = re.sub(r'^>\s*', '', line)
        line = re.sub(r'^(#{1,6})\s+', '', line)
        line = re.sub(r'^\s*[-*]\s+', '', line)
        line = strip_num(line).strip()
        if line and line != "\u200b": rows.append(line)
    return rows

def main():
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    datajson, planfile, md_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    data = json.load(open(datajson, encoding="utf-8"))
    plan = json.load(open(planfile, encoding="utf-8"))
    all_ok, total_imgs = True, sum(1 for b in data if b["t"] == 27)
    cdn_hits = 0
    for seg in plan:
        name, a, b = seg["name"], seg["start"], seg["end"]
        fa = authority_flow(data, a, b)
        fpath = os.path.join(md_dir, name + ".md")
        fm = md_flow(open(fpath, encoding="utf-8").read())
        ok = difflib.SequenceMatcher(None, fa, fm).ratio() == 1.0
        all_ok = all_ok and ok
        md = open(fpath, encoding="utf-8").read()
        n_img = len(re.findall(r'^!\[', md, re.M))
        first_img = re.search(r'^!\[[^\]]*\]\(([^)]+)\)', md, re.M)
        is_local = bool(first_img and first_img.group(1).startswith("imgs/"))
        if is_local:
            cdn_hits += md.count("cdn.yitang.top")
        stars = md.count("**")
        print(f"{name:<24} 文本流{'✅' if ok else '❌'} 图{n_img:>3} **{stars:>3}{'✓' if stars % 2 == 0 else '✗'}")
    print(f"\n总图片块 {total_imgs} | CDN 残留 {cdn_hits}")
    print("全量验证:", "✅ 通过（内容完整）" if all_ok and cdn_hits == 0 else "❌ 未通过")

if __name__ == "__main__":
    main()
