#!/usr/bin/env python
"""带 y 刻度的整段预览（内存安全版）。

用法: python preview_scale.py <源图> <y0> <y1> <输出名> [缩放]

原理: 先 crop 再 load —— PNG 只解码被裁剪的区域，峰值内存 ≈ 段大小，
      绝不整图解码（对比 Image.open().convert() 会在超长图上炸内存）。
左侧每 200px 画一条红色刻度线并标注绝对 y 坐标，便于肉眼读出图的上下边界。
"""
import sys
import gc
from PIL import Image, ImageDraw

SCALE = 1.0
TICK = 200


def preview(src, y0, y1, out, scale=1.0, tick=TICK):
    im = Image.open(src)
    W, H = im.size
    y0 = max(0, int(y0))
    y1 = min(H, int(y1))
    seg = im.crop((0, y0, W, y1))          # 先 crop
    seg.load()                              # 只解码这一段
    im.close()
    if scale != 1.0:
        seg = seg.resize((int(W * scale), int((y1 - y0) * scale)), Image.LANCZOS)
    d = ImageDraw.Draw(seg)
    y = (y0 // tick + 1) * tick
    while y < y1:
        yy = int((y - y0) * scale)
        d.line([(0, yy), (W, yy)], fill=(255, 0, 0), width=2)
        d.text((6, yy + 3), str(y), fill=(255, 0, 0))
        y += tick
    seg.save(out)
    print(f"{out}  y=[{y0},{y1})  {seg.size}")
    del seg, d
    gc.collect()


if __name__ == '__main__':
    a = sys.argv[1:]
    preview(a[0], a[1], a[2], a[3],
            float(a[4]) if len(a) > 4 else 1.0,
            int(a[5]) if len(a) > 5 else TICK)