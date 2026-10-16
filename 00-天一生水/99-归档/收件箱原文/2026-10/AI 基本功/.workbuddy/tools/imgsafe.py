#!/usr/bin/env python3
"""
超长截图处理：内存安全工具集

背景：WorkBuddy（Electron 5.7.7）在处理本课程素材时反复崩溃。
     崩溃报告的决定性证据：
         Kernel Trace: VM - Fault hit memory shortage
         Exception:      EXC_CRASH (SIGABRT)
         Time Awake Since Boot: 1600 seconds（长时间连续运行后出现）

实测数据（本课程 10 号截图 1936x22695）：
  ❌ Image.open(p).convert('RGB')  → 整图解码，**125.7 MB/次**
     反复打开十几次即累积上 GB → 内存耗尽崩溃
  ✅ Image.open(p).crop(box) 后 load() → 惰性解码，**1.9 MB**
     **省 66 倍**

原理：PNG 是无损压缩格式，PIL 的 Image.open() 默认**不解码**，
      只有对某区域调用 .load() / .convert() / .resize() 时才解码**该区域**。
      所以只要**先 crop 再 load**，就永远不会把整张超长图读进内存。

用法
----
  from imgsafe import safe_crop, safe_seg, safe_preview, cleanup, warn
  safe_crop(src, out, y0=16400, y1=18100)          # 裁一段
  safe_seg(src, out_dir, step=1500, upscale=1.4)   # 切阅读段
  safe_preview(src, 16400, 18100, 'p.png')         # 带y刻度预览
  warn(src)                                         # 内存预警

铁律
----
  1. **永远不要对整图调用 .convert() / .resize() / .thumbnail()** —— 那会解码整图
  2. 先 crop → 再 load/convert → 立刻 close + gc.collect()
  3. 分段步长 step 建议 <= 2000px；放大倍率 <= 1.4（每段仍可控）
"""

from PIL import Image, ImageDraw
import gc
import glob
import os
import shutil

Image.MAX_IMAGE_PIXELS = None
MB = 1024 * 1024


def warn(src):
    """打印该图解码后的内存占用，超过 80MB 给出警告。"""
    w, h = Image.open(src).size
    mb = w * h * 3 / MB
    flag = '  ⚠️ 超过 80MB，务必用 safe_crop 不要整图解码' if mb > 80 else ''
    print(f'  [warn] {os.path.basename(src)[:36]:38s} {w}x{h} = {mb:6.1f} MB{flag}')
    return mb


def safe_crop(src, out, y0, y1, x0=0, x1=None, mode='RGB'):
    """
    内存安全的区域裁剪（核心函数）。

    关键：**先 crop 再 load**，全程不解码整图。实测 1.9MB 而非 125.7MB。
    """
    im = Image.open(src)# 惰性，不解码
    W, H = im.size
    x1 = x1 or W
    y0, y1 = max(0, y0), min(H, y1)
    if y1 <= y0:
        im.close()
        raise ValueError(f'区间无效 y0={y0} y1={y1} (图高 {H})')

    seg = im.crop((x0, y0, x1, y1))       # 仍不解码
    if mode:
        seg = seg.convert(mode)           # 只解码这一块
    seg.save(out)

    size = seg.size
    seg.close()
    del seg, im
    gc.collect()
    print(f'  [crop] {os.path.basename(out)}  y={y0}-{y1}  -> {size}')
    return out


def safe_seg(src, out_dir, step=1500, upscale=1.4, prefix=None, fmt='PNG'):
    """
    把超长图切成阅读段。每段独立解码，内存与总图长度无关。

    step<=2000；upscale<=1.4（再大每段内存线性上升，易触发崩溃）。
    """
    os.makedirs(out_dir, exist_ok=True)
    im = Image.open(src)
    W, H = im.size
    base = prefix or os.path.basename(src).split()[0]
    n = (H + step - 1) // step
    made = []
    for i in range(n):
        y0, y1 = i * step, min(H, i * step + step)
        seg = im.crop((0, y0, W, y1))
        if upscale != 1.0:
            w = int(W * upscale)
            h = int((y1 - y0) * upscale)
            seg = seg.resize((w, h), Image.LANCZOS)
        p = os.path.join(out_dir, f'{base}-{i + 1:02d}.{fmt.lower()}')
        seg.save(p, optimize=False)       # optimize=False 省内存
        made.append(p)
        seg.close()
        del seg
    im.close()
    gc.collect()
    print(f'  [seg] {base}: {n} 段 -> {out_dir}')
    return made


def safe_preview(src, y0, y1, out, scale=0.62, tick=200):
    """
    带 y 刻度的整段预览（V3.3 推荐方法：一次定准坐标，避免反复返工）。

    scale 默认压到 0.62 —— 预览只需看清结构，无需看清小字；
    1920px 宽的原图缩到 0.62 仅 1190px，内存极低。
    """
    im = Image.open(src)
    H = im.size[1]
    y0, y1 = max(0, y0), min(H, y1)
    seg = im.crop((0, y0, im.size[0], y1)).convert('RGB')

    w, h = int(seg.width * scale), int(seg.height * scale)
    seg = seg.resize((w, h), Image.LANCZOS)

    bar = 56
    canvas = Image.new('RGB', (w + bar, h), 'white')
    canvas.paste(seg, (bar, 0))
    d = ImageDraw.Draw(canvas)
    y = (y0 // tick) * tick
    while y < y1:
        py = int((y - y0) * scale)
        if 0 <= py < h:
            d.line([(0, py), (bar - 8, py)], fill='red', width=1)
            d.text((4, max(0, py - 11)), str(y), fill='red')
        y += tick
    canvas.save(out)

    canvas.close()
    seg.close()
    del canvas, seg, im
    gc.collect()
    print(f'  [preview] {out}  y={y0}-{y1}')
    return out


def cleanup(*patterns):
    """清理临时文件。**源图务必留在工作目录，不要放/tmp。**"""
    total = 0
    for pat in patterns:
        for p in glob.glob(pat):
            if os.path.isdir(p):
                for f in os.listdir(p):
                    fp = os.path.join(p, f)
                    if os.path.isfile(fp):
                        total += os.path.getsize(fp)
                shutil.rmtree(p, ignore_errors=True)
            elif os.path.isfile(p):
                total += os.path.getsize(p)
                os.remove(p)
    if total:
        print(f'  [cleanup] 释放 {total / MB:.1f} MB')
    return total


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    for f in sys.argv[1:]:
        warn(f)
