# -*- coding: utf-8 -*-
"""
course-doc-to-local / gen_split.py
从 dataJson 全量块序列 + 拆分方案生成多篇 Markdown（含图片 URL 版）
用法:
  python3 gen_split.py <datajson.json> <plan.json> <out_dir>
  plan.json: [{"name": "01-总览：开篇", "start": 0, "end": 527}, ...]（end 为下一篇起点）
类型映射（实测确认）：2 text / 3 h1 / 4 h2 / 5 h3 / 12 bullet / 13 ordered /
14 code（内容在 a.code，不在 a.text！）/ 19 callout / 22 hr / 23 file /
24 grid / 25 grid_column / 27 image / 33 view / 34 quote_container
"""
import json, os, re, sys

def elems_text(attr, key):
    """提取 elements 文本；bold / background_color 转 **；相邻同状态 run 合并"""
    if not attr or key not in attr:
        return ""
    node = attr[key]
    if not node or "elements" not in node:
        return ""
    parts, prev_bold = [], None
    for el in node["elements"]:
        tr = el.get("text_run") or {}
        content = tr.get("content", "") or ""
        st = tr.get("text_element_style") or {}
        bold = bool(st.get("bold") or st.get("background_color"))
        if not content:
            continue
        if prev_bold is None:
            if bold:
                parts.append("**")
            parts.append(content)
        elif bold != prev_bold:
            if prev_bold:
                parts.append("**")
            if bold:
                parts.append("**")
            parts.append(content)
        else:
            parts.append(content)
        prev_bold = bold
    if prev_bold:
        parts.append("**")
    return "".join(parts)

def code_text(attr):
    """code 块纯文本（不加粗，保持代码原样）"""
    node = attr.get("code") or {}
    return "".join((el.get("text_run") or {}).get("content", "") or ""
                   for el in node.get("elements", []))

def render(data, img_urls, a, b, img_start):
    N = len(data)
    # 子树结束位置
    end = list(range(N))
    for i in range(N - 1, -1, -1):
        c = data[i]["c"]; e = i; cs = i + 1
        for _ in range(c):
            if cs >= N: break
            e = end[cs]; cs = e + 1
        end[i] = e
    # quote 容器标记
    quote_level = [0] * N
    for i in range(N):
        if data[i]["t"] == 34:
            for j in range(i + 1, min(end[i] + 1, N)):
                quote_level[j] += 1

    lines, img_idx = [], img_start
    ordered_num, prev_was_list = None, False
    i = a
    while i < b:
        blk = data[i]
        t = blk["t"]; ql = quote_level[i]
        attr = blk.get("a") or {}
        if t in (19, 24, 25, 33, 34):  # 容器跳过，子块自然输出
            i += 1; continue
        line, need_blank = None, True
        if t == 27:
            url = img_urls[img_idx] if img_idx < len(img_urls) else "MISSING"
            img_idx += 1
            line = f"![]({url})"
        elif t == 3: line = "## " + elems_text(attr, "heading1")
        elif t == 4: line = "### " + elems_text(attr, "heading2")
        elif t == 5: line = "#### " + elems_text(attr, "heading3")
        elif t == 14:
            ct = code_text(attr)
            if ct.strip(): line = "```\n" + ct + "\n```"
        elif t == 2:
            txt = elems_text(attr, "text")
            if not txt or txt.strip() in ("\u200b", ""):
                i += 1; continue
            line = ("> " * ql + txt) if ql else txt
        elif t == 12:
            txt = elems_text(attr, "bullet")
            if not txt.strip(): i += 1; continue
            line = ("> " * ql + "- " + txt) if ql else "- " + txt
            need_blank = not prev_was_list
        elif t == 13:
            txt = elems_text(attr, "ordered")
            if not txt.strip(): i += 1; continue
            seq = (attr.get("ordered") or {}).get("style", {}).get("sequence", "auto")
            ordered_num = (ordered_num or 0) + 1 if seq == "auto" else (int(seq) if str(seq).isdigit() else 1)
            line = f"{'> ' * ql}{ordered_num}. {txt}" if ql else f"{ordered_num}. {txt}"
            need_blank = str(seq).isdigit() and prev_was_list
        elif t == 23:
            line = "📹 " + (attr.get("file") or {}).get("name", "附件")
        elif t == 22:
            line = "---"
        if line is not None:
            if need_blank and lines and lines[-1] != "":
                lines.append("")
            lines.append(line)
            prev_was_list = bool(re.match(r'^(\d+\.|- )', line) and not line.startswith(">"))
        i += 1
    while lines and lines[-1] == "":
        lines.pop()
    return lines, img_idx

def main():
    if len(sys.argv) < 5:
        print(__doc__); sys.exit(1)
    datajson, planfile, outdir, imgsfile = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    data = json.load(open(datajson, encoding="utf-8"))
    plan = json.load(open(planfile, encoding="utf-8"))
    img_urls = json.load(open(imgsfile, encoding="utf-8"))
    os.makedirs(outdir, exist_ok=True)
    total_imgs = sum(1 for b in data if b["t"] == 27)
    img_idx, imgs_by_doc = 0, {}
    print(f"{'篇':<24}{'图片':>6}")
    for seg in plan:
        name, a, b = seg["name"], seg["start"], seg["end"]
        lines, img_idx = render(data, img_urls, a, b, img_idx)
        md = "\n".join(lines)
        with open(os.path.join(outdir, name + ".md"), "w", encoding="utf-8") as f:
            f.write(md)
        doc_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', md)
        imgs_by_doc[name] = doc_imgs
        print(f"{name:<24}{len(doc_imgs):>6}")
    tot = sum(len(v) for v in imgs_by_doc.values())
    print(f"\n总图片 {tot} == dataJson 图片块 {total_imgs}: {tot == total_imgs}")
    json.dump(imgs_by_doc, open(os.path.join(outdir, "imgs_by_doc.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("生成完成 →", outdir)

if __name__ == "__main__":
    main()
