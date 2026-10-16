#!/usr/bin/env python3
"""
带刻度的整段预览图生成器 —— 解决"裁剪反复返工"的根因。

问题：自动密度扫描给的是"有颜色的行区间"，无法区分
  · 图与正文之间的渐变/淡色底纹边界
  · 图内部白色空隙会把一张图切成多个 run
  · 正文密集区密度与图接近
导致 "裁→看→错→再裁" 的循环，单张图返工 4 次以上。

方法：先输出整段预览，左侧带绝对 y 刻度，肉眼一次看清结构，
     直接读出每张图的准确上下边界，再一次性裁剪。

用法：
  python preview_with_scale.py <源图> <y0> <y1> [输出名] [缩放]
  例：
  python preview_with_scale.py 10.png 16400 18100 p10-f 0.62
"""
from PIL import Image, ImageDraw
import sys

Image.MAX_IMAGE_PIXELS = None


def make_preview(src, y0, y1, out, scale=0.62, tick=200):
    im = Image.open(src).convert('RGB')
    H = im.height
    y0 = max(0, y0)
    y1 = min(H, y1)
    if y1 <= y0:
        raise SystemExit(f'区间无效: y0={y0} y1={y1} (图高{H})')

    seg = im.crop((0, y0, im.width, y1))
    w = int(seg.width * scale)
    h = int(seg.height * scale)
    seg = seg.resize((w, h), Image.LANCZOS)

    bar = 56# 左侧刻度栏宽度
    canvas = Image.new('RGB', (w + bar, h), 'white')
    canvas.paste(seg, (bar, 0))
    d = ImageDraw.Draw(canvas)

    y = (y0 // tick) * tick          # 刻度对齐到整百
    while y < y1:
        py = int((y - y0) * scale)
        if 0 <= py < h:
            d.line([(0, py), (bar - 8, py)], fill='red', width=1)
            d.text((4, max(0, py - 11)), str(y), fill='red')
        y += tick

    canvas.save(out)
    print(f'{out}  y={y0}-{y1}  size={canvas.size}')
    return out


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    src, y0, y1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    out = sys.argv[4] if len(sys.argv) > 4 else 'preview.png'
    sc = float(sys.argv[5]) if len(sys.argv) > 5 else 0.62
    make_preview(src, y0, y1, out, sc)
