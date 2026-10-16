#!/usr/bin/env python
"""按坐标裁图（内存安全：先 crop 再 load），列方向自动收缩到内容边界。

用法: python docrop.py <源图> <out> <y0> <y1> [x0] [x1] [pad]
若不给 x0/x1，则在 [0,W) 内按列收缩。
"""
import sys
import gc
import numpy as np
from PIL import Image

PAD = 6
COL_DIFF = 245


def docrop(src, out, y0, y1, x0=None, x1=None, pad=PAD):
    im = Image.open(src)
    W, H = im.size
    y0 = max(0, int(y0))
    y1 = min(H, int(y1))
    seg = im.crop((0, y0, W, y1))
    seg.load()
    a = np.asarray(seg.convert('L'))
    col = (a < COL_DIFF).mean(axis=0)
    nz = np.nonzero(col > 0.004)[0]
    if len(nz) == 0:
        raise SystemExit(f'{out}: 该区间无内容')
    cx0 = max(0, int(x0) if x0 is not None else nz[0])
    cx1 = min(W, int(x1) if x1 is not None else nz[-1] + 1)
    del a, col
    im.close()
    seg2 = im.crop((max(0, cx0 - pad), y0, min(W, cx1 + pad), y1)) if False else None
    # 重新打开取子区（保持内存安全）
    im2 = Image.open(src)
    seg2 = im2.crop((max(0, cx0 - pad), max(0, y0 - pad),
                      min(W, cx1 + pad), min(H, y1 + pad)))
    seg2.load()
    im2.close()
    seg2.save(out)
    print(f'{out}  y=[{y0},{y1})  x=[{cx0},{cx1})  size={seg2.size}')
    del seg, seg2
    gc.collect()


if __name__ == '__main__':
    a = sys.argv[1:]
    docrop(a[0], a[1], a[2], a[3],
           *( [int(a[4]), int(a[5])] if len(a) > 5 else [] ))