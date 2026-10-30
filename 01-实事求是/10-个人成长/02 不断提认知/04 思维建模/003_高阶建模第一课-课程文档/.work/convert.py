import os, gc
from PIL import Image

BASE = "/Users/panda/Desktop/03 一堂课程/高阶建模第一课"
OUT = "/Users/panda/Desktop/knowledge-base/05-收件箱/003_高阶建模第一课-课程文档"
IMGDIR = os.path.join(OUT, "images")

# (folder, page_prefix, count)
plan = [
    ("01 复盘的不同段位", "15", 5),
    ("02 before...after对比", "16", 5),
    ("03 AI 拉满建模", "17", 10),
    ("04 战略", "18", 3),
    ("05 本质", "19", 2),
    ("06 如何练习", "20", 3),
]

rows = []
for folder, prefix, n in plan:
    for i in range(1, n + 1):
        src = os.path.join(BASE, folder, f"{i}.webp")
        outname = f"{prefix}-{i:02d}.png"
        dst = os.path.join(IMGDIR, outname)
        # one at a time: open -> convert -> save -> close
        im = Image.open(src)
        w, h = im.size
        rgb = im.convert("RGB")
        rgb.save(dst, "PNG")
        rgb.close()
        im.close()
        del im, rgb
        gc.collect()
        rows.append((outname, f"{folder}/{i}.webp", w, h))
        print(f"{outname}\t{w}x{h}\t<- {folder}/{i}.webp")

print("TOTAL", len(rows))
