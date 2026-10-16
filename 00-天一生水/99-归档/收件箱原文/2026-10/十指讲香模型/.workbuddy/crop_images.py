#!/usr/bin/env python3
"""从课程长截图中裁剪嵌入的图片区块（金句横幅、案例封面、欢迎卡片等）。"""
import os
import sys
import numpy as np
from PIL import Image

SRC_DIR = "/Users/panda/Desktop/十指讲香模型"
OUT_DIR = os.path.join(SRC_DIR, "images")
os.makedirs(OUT_DIR, exist_ok=True)

# 可调参数
NONWHITE_DIFF = 22      # 像素与白色的最小差异
ROW_RATIO = 0.62        # 一行中非白像素比例超过此值视为"图片行"
MIN_H = 110             # 图片区块最小高度（px）
GAP = 6                 # 合并连续行时允许的空隙
PAD = 3                 # 裁剪边距

def page_key(name: str) -> str:
    """'00 开场.png' -> '00'；'12-场景化.png' -> '12'"""
    digits = ""
    for ch in name:
        if ch.isdigit():
            digits += ch
        elif digits:
            break
    return digits or name

def nonwhite_mask(arr: np.ndarray) -> np.ndarray:
    diff = 255 - arr.min(axis=2)  # 与白色距离的粗略度量
    return diff > NONWHITE_DIFF

def crop_images(path: str):
    im = Image.open(path).convert("RGB")
    arr = np.asarray(im)
    mask = nonwhite_mask(arr)
    ratios = mask.mean(axis=1)

    rows = ratios > ROW_RATIO
    # 合并连续行
    blocks = []
    start = None
    gap = 0
    for i, r in enumerate(rows):
        if r:
            if start is None:
                start = i
            gap = 0
        else:
            if start is not None:
                gap += 1
                if gap > GAP:
                    end = i - gap
                    blocks.append((start, end))
                    start = None
                    gap = 0
    if start is not None:
        blocks.append((start, len(rows) - 1 - gap))

    results = []
    for (y0, y1) in blocks:
        if y1 - y0 < MIN_H:
            continue
        # 左右收缩到内容边界
        col_ratio = mask[y0:y1 + 1].mean(axis=0)
        cols = np.where(col_ratio > 0.5)[0]
        if len(cols) == 0:
            continue
        x0, x1 = int(cols[0]), int(cols[-1])
        if x1 - x0 < 200:  # 太窄不是横幅图
            continue
        box = (max(x0 - PAD, 0), max(y0 - PAD, 0), min(x1 + PAD, im.width), min(y1 + PAD, im.height))
        crop = im.crop(box)
        results.append((box, crop))

    return im, results

def main():
    files = sorted(f for f in os.listdir(SRC_DIR) if f.endswith(".png"))
    total = 0
    for f in files:
        im, results = crop_images(os.path.join(SRC_DIR, f))
        key = page_key(f)
        for idx, (box, crop) in enumerate(results, 1):
            out = os.path.join(OUT_DIR, f"{key}-{idx:02d}.png")
            crop.save(out)
            # 采样平均色帮助核对
            small = np.asarray(crop.resize((8, 8)))
            avg = small.reshape(-1, 3).mean(axis=0).astype(int)
            print(f"{f}: 区块{idx} box={box} size={crop.size} avgRGB={tuple(avg)} -> {os.path.basename(out)}")
            total += 1
    print(f"\n共裁剪 {total} 个图片区块 -> {OUT_DIR}")

if __name__ == "__main__":
    main()
