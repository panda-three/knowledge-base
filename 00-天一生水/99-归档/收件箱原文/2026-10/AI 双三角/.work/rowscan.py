#!/usr/bin/env python
"""行密度扫描（内存安全版）：逐段 crop 后统计每行非白占比，输出候选区块。

只用于「找候选」，边界必须再用 preview_scale.py 带刻度预览确认。
用法: python rowscan.py <源图>
"""
import sys
import gc
import numpy as np
from PIL import Image

BAND = 1200
DIFF = 235          # <235 视为非白
THRESH = 0.012      # 极低阈值，抓浅色图


def scan(src):
    im = Image.open(src)
    W, H = im.size
    print(f"# {src}  {W}x{H}")
    vals = np.zeros(H, dtype=np.float32)
    y = 0
    while y < H:
        y1 = min(y + BAND, H)
        seg = im.crop((0, y, W, y1))
        seg.load()
        a = np.asarray(seg.convert('L'))
        vals[y:y1] = (a < DIFF).mean(axis=1)
        del seg, a
        y = y1
    im.close()
    mask = vals > THRESH
    # 连续超阈行合并（间隔 <28px合并）
    runs = []
    y = 0
    while y < H:
        if mask[y]:
            s = y
            gap = 0
            e = y
            while e + 1 < H:
                if mask[e + 1]:
                    e += 1
                    gap = 0
                else:
                    gap += 1
                    if gap > 28:
                        break
                    e += 1
            runs.append((s, e + 1))
            y = e + 1
        else:
            y += 1
    for s, e in runs:
        pk = vals[s:e].max()
        avg = vals[s:e].mean()
        flag = '★' if e - s >= 160 else ' '
        print(f"{flag} y=[{s},{e})  h={e-s:5d}  峰值={pk:.3f} 均值={avg:.3f}")
    gc.collect()


if __name__ == '__main__':
    for p in sys.argv[1:]:
        scan(p)