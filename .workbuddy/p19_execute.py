#!/usr/bin/env python3
"""P1-9 待裁决清单 A/C/D/F/G/H 执行脚本。B 项有既有裁决不动，E 降级不动。
策略：先 mv 目录，再对活跃层 md 做精确字符串替换（路径 + URL 编码变体），最后补 H1、验证。"""
import os, re, sys, urllib.parse

ROOT = '/Users/panda/Desktop/knowledge-base'
os.chdir(ROOT)

# ---------- 1. 目录改名 ----------
renames = [
    # D 行动营
    ('01-实事求是/10-个人成长/00 Y 模型实操行动营 重新理解科学理念',
     '01-实事求是/10-个人成长/00-Y模型实操行动营：重新理解科学理念'),
    # A 70 案例库
    ('02-解放思想/70 案例库', '02-解放思想/70-案例库'),
    # C emoji 8 处（含 00 空格前缀修正）
    ('01-实事求是/10-个人成长/00 🎯直播Live第263场：一堂Y模型解读之夜',
     '01-实事求是/10-个人成长/00-直播Live第263场：一堂Y模型解读之夜'),
    ('01-实事求是/10-个人成长/00 🎯一堂Y模型：实操框架篇',
     '01-实事求是/10-个人成长/00-一堂Y模型：实操框架篇'),
    ('01-实事求是/10-个人成长/02 不断提认知/04 思维建模/🎯直播Live第265场：一堂Y模型解读之夜第二场',
     '01-实事求是/10-个人成长/02 不断提认知/04 思维建模/直播Live第265场：一堂Y模型解读之夜第二场'),
    ('01-实事求是/10-个人成长/02 不断提认知/05 调研黑客/🎯直播Live第264场：AI调研实操组合篇',
     '01-实事求是/10-个人成长/02 不断提认知/05 调研黑客/直播Live第264场：AI调研实操组合篇'),
    ('01-实事求是/50-AI技术与应用/AI技能/🎯直播Live第262场：AI场景第一课',
     '01-实事求是/50-AI技术与应用/AI技能/直播Live第262场：AI场景第一课'),
    ('01-实事求是/50-AI技术与应用/🎯特别场：一堂YAI第一课',
     '01-实事求是/50-AI技术与应用/特别场：一堂YAI第一课'),
    ('02-解放思想/50-AI技术与应用/🎯AI落地Live88·YAI新人上手技巧分享',
     '02-解放思想/50-AI技术与应用/AI落地Live88·YAI新人上手技巧分享'),
    ('01-实事求是/40-管理与组织/管理必修/03 管业务/04 提转化/🎯一堂行动营：转化率AI落地篇',
     '01-实事求是/40-管理与组织/管理必修/03 管业务/04 提转化/一堂行动营：转化率AI落地篇'),
    # F 双三角标准写法
    ('01-实事求是/50-AI技术与应用/AI 双三角', '01-实事求是/50-AI技术与应用/AI双三角'),
    ('01-实事求是/60-教育与教学/探月/03_AI 双三角：用AI手搓游戏，如何越做越好玩',
     '01-实事求是/60-教育与教学/探月/03_AI双三角：用AI手搓游戏，如何越做越好玩'),
    # G 09 关于我
    ('00-天一生水/09 关于我', '00-天一生水/09-关于我'),
]
print('== 1. 目录改名 ==')
for old, new in renames:
    if not os.path.exists(old):
        print(f'  [跳过] 不存在: {old}'); continue
    if os.path.exists(new):
        print(f'  [跳过] 目标已存在: {new}'); continue
    os.rename(old, new)
    print(f'  [OK] {os.path.basename(old)} -> {os.path.basename(new)}')

# ---------- 2. 文本替换映射（活跃层） ----------
# 精确路径字符串；URL 编码变体（空格→%20）单独列
sub_map = [
    # D 行动营：普通路径 + wikilink + URL编码图片路径
    ('00 Y 模型实操行动营 重新理解科学理念', '00-Y模型实操行动营：重新理解科学理念'),
    ('00%20Y%20模型实操行动营%20重新理解科学理念', '00-Y模型实操行动营：重新理解科学理念'),
    ('00【Y 模型实操行动营】重新理解科学理念', '00-Y模型实操行动营：重新理解科学理念'),
    # A 70 案例库（带父路径，防误伤正文表述）
    ('02-解放思想/70 案例库', '02-解放思想/70-案例库'),
    # C emoji 目录名（含 00 前缀空格修正）
    ('00 🎯直播Live第263场：一堂Y模型解读之夜', '00-直播Live第263场：一堂Y模型解读之夜'),
    ('00 🎯一堂Y模型：实操框架篇', '00-一堂Y模型：实操框架篇'),
    ('00%20🎯直播Live第263场：一堂Y模型解读之夜', '00-直播Live第263场：一堂Y模型解读之夜'),
    ('00%20🎯一堂Y模型：实操框架篇', '00-一堂Y模型：实操框架篇'),
    ('🎯直播Live第265场：一堂Y模型解读之夜第二场', '直播Live第265场：一堂Y模型解读之夜第二场'),
    ('🎯直播Live第264场：AI调研实操组合篇', '直播Live第264场：AI调研实操组合篇'),
    ('🎯直播Live第262场：AI场景第一课', '直播Live第262场：AI场景第一课'),
    ('🎯特别场：一堂YAI第一课', '特别场：一堂YAI第一课'),
    ('🎯AI落地Live88·YAI新人上手技巧分享', 'AI落地Live88·YAI新人上手技巧分享'),
    ('🎯一堂行动营：转化率AI落地篇', '一堂行动营：转化率AI落地篇'),
    # F 双三角（路径限定）
    ('50-AI技术与应用/AI 双三角', '50-AI技术与应用/AI双三角'),
    ('03_AI 双三角：用AI手搓游戏，如何越做越好玩', '03_AI双三角：用AI手搓游戏，如何越做越好玩'),
    # G 路径 + 简称文本
    ('00-天一生水/09 关于我', '00-天一生水/09-关于我'),
    ('/ 09 关于我', '/ 09-关于我'),   # 目录清单式写法
]
# 活跃层（历史层：99-归档 / 01-系统文档/知识库体检+收件箱分拣 / .backup / vault-log 均不动）
ACTIVE = ['00-专注区', '00-天一生水/02-工具标准', '00-天一生水/03-基本法',
          '00-天一生水/04-灵魂校准', '00-天一生水/05-架构设计', '00-天一生水/06-评估报告',
          '00-天一生水/00-vault-log.md', '01-实事求是', '02-解放思想',
          '03-知行合一', '04-作品出口', '05-收件箱']
# vault-log 与评估报告属留痕，只改路径引用（wikilink/代码），简化：全部替换但不改历史叙事正文
# ——保守起见 vault-log 不动（历史操作日志），体检报告/分拣清单不动。
SCAN = [p for p in ACTIVE if not p.endswith('vault-log.md')]

changed = {}
def walk_md(path):
    if os.path.isfile(path) and path.endswith('.md'):
        yield path
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            if any(x in root for x in ['.backup', '/meta/', '99-归档', '.work']):
                dirs[:] = []; continue
            for f in files:
                if f.endswith('.md'):
                    yield os.path.join(root, f)

print('== 2. 活跃层文本替换 ==')
total = 0
for base in SCAN:
    for fp in walk_md(base):
        with open(fp, encoding='utf-8') as fh: text = fh.read()
        orig = text
        for old, new in sub_map:
            text = text.replace(old, new)
        if text != orig:
            with open(fp, 'w', encoding='utf-8') as fh: fh.write(text)
            n = sum(orig.count(o) for o, _ in sub_map)
            changed[fp] = n; total += n
for fp, n in sorted(changed.items()):
    print(f'  [OK] {fp} ({n} 处)')
print(f'  合计 {len(changed)} 个文件 / {total} 处替换')

# ---------- 3. H：行动营 8 篇补 H1 ----------
print('== 3. 行动营补 H1 ==')
course = '01-实事求是/10-个人成长/00-Y模型实操行动营：重新理解科学理念'
titles = ['开篇：开始上课', '60分 体感：基本认识', '70分 统一：科学框架',
          '80分 理解：全面认识', '90分 追求：主动修炼', '100分：唯一道路',
          '作业与Candy', '一堂活动信息']
for i, t in enumerate(titles, 1):
    fp = os.path.join(course, f'{i:02d}-{t}.md')
    with open(fp, encoding='utf-8') as fh: text = fh.read()
    if re.search(r'^# ', text, flags=re.M):
        print(f'  [跳过] 已有 H1: {os.path.basename(fp)}'); continue
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(f'# {t}\n\n' + text)
    print(f'  [OK] +H1: {i:02d}-{t}.md')
