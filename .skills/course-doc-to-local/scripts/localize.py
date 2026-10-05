# -*- coding: utf-8 -*-
"""
course-doc-to-local / localize.py
把生成的 MD 中图片 URL 替换为本地相对路径（imgs/pNN_MMM.ext）
用法:
  python3 localize.py <src_dir> <out_dir>
  src_dir 含 N 篇 md（图片为 URL）与 imgs_by_doc.json；out_dir 为最终交付目录
校验：每篇图片替换数 == imgs_by_doc 数；本地文件必须全部存在
"""
import json, os, re, sys

IMG_RE = re.compile(r'^!\[[^\]]*\]\(([^)]+)\)$')

def ext_of(url):
    base = url.rsplit('/', 1)[-1]
    if '.' in base:
        e = base.rsplit('.', 1)[-1].split('?')[0].lower()
        if e in ("png", "jpg", "jpeg", "gif", "webp", "bmp"):
            return "jpg" if e == "jpeg" else e
    return "jpg"

def main():
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    src, out, imgs_root = sys.argv[1], sys.argv[2], sys.argv[3]
    imgs_by_doc = json.load(open(os.path.join(src, "imgs_by_doc.json"), encoding="utf-8"))
    os.makedirs(os.path.join(out, "imgs"), exist_ok=True)
    doc_no = {name: name.split("-")[0] for name in imgs_by_doc}
    missing, summary = 0, []
    for name, urls in imgs_by_doc.items():
        no = doc_no[name]
        md = open(os.path.join(src, name + ".md"), encoding="utf-8").read()
        locals_ = [f"imgs/p{no}_{k:03d}.{ext_of(u)}" for k, u in enumerate(urls, 1)]
        lines, k, out_lines = md.split("\n"), 0, []
        for line in lines:
            m = IMG_RE.match(line)
            if m:
                k += 1
                lf = locals_[k - 1]
                if not os.path.exists(os.path.join(imgs_root, lf)):
                    missing += 1
                out_lines.append(f"![]({lf})")
            else:
                out_lines.append(line)
        assert k == len(urls), f"{name}: 替换 {k} != 图片 {len(urls)}"
        with open(os.path.join(out, name + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(out_lines))
        summary.append((name, k))
    print(f"本地化完成 {len(summary)} 篇 | 缺失图片 {missing} | 总图片 {sum(k for _, k in summary)}")

if __name__ == "__main__":
    main()
