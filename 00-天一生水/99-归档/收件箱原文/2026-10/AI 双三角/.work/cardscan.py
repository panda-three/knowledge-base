#!/usr/bin/env python
"""浅色卡片边界扫描：米色卡片底色 L≈240，>235 所以 (a<235) 抓不到。
改用「该行是否存在非纯白像素（L<250）且连续成片」来定位卡片上下边界。
用法: python cardscan.py <源图> [x_center_frac]
"""
import sys
import gc
import numpy as np
from PIL import Image

BAND = 1000
LO = 250     # 非纯白
MIN_H = 120


def scan(src, frac=0.5):
    im = Image.open(src)
    W, H = im.size
    x0, x1 = int(W * 0.25), int(W * 0.75)
    vals = np.zeros(H, dtype=np.float32)
    y = 0
    while y < H:
        y1 = min(y + BAND, H)
        seg = im.crop((x0, y, x1, y1))
        seg.load()
        a = np.asarray(seg.convert('L'))
        # 中段区域：卡片存在时整行都会被底色填满 -> 接近 1.0；空白 -> 0
        vals[y:y1] = (a < LO).mean(axis=1)
        del seg, a
        y = y1
    im.close()
    runs = []
    y = 0
    while y < H:
        if vals[y] > 0.55:
            s = y
            e = y
            gap = 0
            while e + 1 < H:
                if vals[e + 1] > 0.55:
                    e += 1
                    gap = 0
                else:
                    gap += 1
                    if gap > 20:
                        break
                    e += 1
            if e - s >= MIN_H:
                runs.append((s, e + 1))
            y = e + 1
        else:
            y += 1
    for s, e in runs:
        print(f"★卡片 y=[{s},{e})  h={e-s}")
    if not runs:
        print("(无卡片)")
    gc.collect()


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(f"# {p}")
        scan(p)