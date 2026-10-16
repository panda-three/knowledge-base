#!/bin/zsh
set -e
cd "/Users/panda/Desktop/AI 双三角"
P=/Users/panda/.workbuddy/binaries/python/envs/default/bin/python
O=AI双三角-课程文档/images

# ---- 06 重裁（cardscan 精确定位）----
S6="06 框架-人类竞争力.png"
$P .work/docrop.py "$S6" $O/06-01.png 936 1480
$P .work/docrop.py "$S6" $O/06-03.png 4207 4727
$P .work/docrop.py "$S6" $O/06-06.png 8729 9275

# ---- 07 ----
S7="07 框架-AI 竞争力.png"
$P .work/docrop.py "$S7" $O/07-01.png 394 941
$P .work/docrop.py "$S7" $O/07-02.png 1908 2459
$P .work/docrop.py "$S7" $O/07-03.png 2888 3408
$P .work/docrop.py "$S7" $O/07-04.png 6400 7150
$P .work/docrop.py "$S7" $O/07-05.png 7560 7990
$P .work/docrop.py "$S7" $O/07-06.png 8904 9424

# ---- 08 ----
S8="08 框架-整合在一起.png"
$P .work/docrop.py "$S8" $O/08-01.png 764 1325
$P .work/docrop.py "$S8" $O/08-02.png 2519 2904

# ---- 09 ----
S9="09 框架-形成飞轮.png"
$P .work/docrop.py "$S9" $O/09-01.png 264 784
$P .work/docrop.py "$S9" $O/09-02.png 2192 2759

# ---- 10 ----
S10="10 框架-AI原生.png"
$P .work/docrop.py "$S10" $O/10-01.png 213 532
$P .work/docrop.py "$S10" $O/10-02.png 2814 3036
$P .work/docrop.py "$S10" $O/10-03.png 5714 6688
$P .work/docrop.py "$S10" $O/10-04.png 7572 8125
$P .work/docrop.py "$S10" $O/10-05.png 8424 8670