#!/usr/bin/env python3
"""split_long_images.py — 将文件夹中的超长截图按固定高度分段。

背景：课程截图常为超长图（高度 >4000px），直接整图 Read 会漏读/截断。
本脚本将长图切成若干段（默认每段 3800px，可配 --max-height），
输出到 <out_dir>/<stem>_partN.png，供后续逐段 Read。

用法：
    python3 split_long_images.py <input_dir> --out <output_dir> [--max-height 3800] [--min-height 4000]

规则：
- 高度 <= --min-height 的图片不切分，原样复制到输出目录（保留原名，方便统一按文件名排序读取）。
- 高度 > --min-height 的图片按 --max-height 切段；最后一段不足也保留。
- 输出命名：<原文件名去扩展名>_part<两位序号>.<png>，如 07_star.png -> 07_star_part01.png...
- 同时打印切分清单（文件名 + 段数），供读取时逐段核对、防漏读。
"""
import argparse
import shutil
from pathlib import Path

from PIL import Image


def split_image(src: Path, out_dir: Path, max_height: int) -> list[Path]:
    img = Image.open(src)
    w, h = img.size
    stem = src.stem
    parts: list[Path] = []
    n = (h + max_height - 1) // max_height
    for i in range(n):
        top = i * max_height
        bottom = min((i + 1) * max_height, h)
        seg = img.crop((0, top, w, bottom))
        out_path = out_dir / f"{stem}_part{i + 1:02d}.png"
        seg.save(out_path, "PNG")
        parts.append(out_path)
    return parts


def main() -> None:
    ap = argparse.ArgumentParser(description="超长截图按高度分段")
    ap.add_argument("input_dir", help="原始图片文件夹")
    ap.add_argument("--out", required=True, help="分段输出目录")
    ap.add_argument("--max-height", type=int, default=3800, help="每段最大高度 px（默认 3800）")
    ap.add_argument("--min-height", type=int, default=4000, help="超过该高度才切分（默认 4000）")
    args = ap.parse_args()

    in_dir = Path(args.input_dir)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
    images = sorted(
        (p for p in in_dir.iterdir() if p.suffix.lower() in exts),
        key=lambda p: p.name,
    )
    if not images:
        print("NO_IMAGES")
        return

    print("=== 分段计划 ===")
    for src in images:
        with Image.open(src) as img:
            w, h = img.size
        if h > args.min_height:
            parts = split_image(src, out_dir, args.max_height)
            print(f"{src.name}: {w}x{h} -> {len(parts)} 段 ({out_dir.name}/{src.stem}_part01.png ...)")
        else:
            dst = out_dir / src.name
            shutil.copy2(src, dst)
            print(f"{src.name}: {w}x{h} -> 不切分（复制 {dst.name}）")
    print("=== 完成 ===")


if __name__ == "__main__":
    main()
