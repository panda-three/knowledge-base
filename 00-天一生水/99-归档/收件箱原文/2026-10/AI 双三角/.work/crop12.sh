#!/bin/zsh
set -e
cd "/Users/panda/Desktop/AI 双三角"
P=/Users/panda/.workbuddy/binaries/python/envs/default/bin/python
O=AI双三角-课程文档/images
S="12 实操-入门场景.png"

$P .work/docrop.py "$S" $O/12-01.png 1105 1665    # 条件反射测试卡
$P .work/docrop.py "$S" $O/12-02.png 3028 3445    # 我曾拆解过的一些双三角（4张）
$P .work/docrop.py "$S" $O/12-03.png 3650 3852    # 马拉松拆解第一排（8张）
$P .work/docrop.py "$S" $O/12-04.png 3918 4120    # 马拉松拆解第二排（8张）
$P .work/docrop.py "$S" $O/12-05.png 4548 4940    # 自己的优秀表现横幅
$P .work/docrop.py "$S" $O/12-06.png 5105 5435    # YAI 复盘报告长图
$P .work/docrop.py "$S" $O/12-07.png 7570 8465    # 打字vs口喷 VS 图
$P .work/docrop.py "$S" $O/12-08.png 8930 9485    # 口喷的本质卡
$P .work/docrop.py "$S" $O/12-09.png 9790 10720   # 口喷示意图
$P .work/docrop.py "$S" $O/12-10.png 13420 14340  # 每周双三角指数