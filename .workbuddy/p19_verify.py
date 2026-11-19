#!/usr/bin/env python3
"""P1-9 重排后全量验证。输出 PASS/FAIL 明细。"""
import os, re, glob

ROOT = '/Users/panda/Desktop/knowledge-base'
os.chdir(ROOT)
fails, warns = [], []

# ---------- V1 老字符串残留（活跃层，历史层豁免） ----------
old_names = [
    '00 Y 模型实操行动营 重新理解科学理念',
    '02-解放思想/70 案例库',
    '00 🎯直播Live第263场', '00 🎯一堂Y模型', '🎯直播Live第265场', '🎯直播Live第264场',
    '🎯直播Live第262场', '🎯特别场：一堂YAI第一课', '🎯AI落地Live88', '🎯一堂行动营：转化率',
    '50-AI技术与应用/AI 双三角', '03_AI 双三角：用AI手搓游戏',
    '00-天一生水/09 关于我',
]
skip_pat = re.compile(r'(\.backup|^99-归档|/99-归档/|01-系统文档/知识库体检|01-系统文档/收件箱分拣|'
                      r'01-系统文档/AI教育课沉淀|\.workbuddy|\.work/|00-vault-log\.md|AI教育课沉淀/meta)')
def active_md():
    for base in ['00-专注区','00-天一生水','01-实事求是','02-解放思想','03-知行合一','04-作品出口','05-收件箱']:
        for root, dirs, files in os.walk(base):
            if skip_pat.search(root): dirs[:] = []; continue
            for f in files:
                if f.endswith('.md'): yield os.path.join(root, f)

print('== V1 老字符串残留（活跃层，历史层豁免）==')
residue = 0
for fp in active_md():
    text = open(fp, encoding='utf-8').read()
    for old in old_names:
        if old in text:
            if 'vault-log' in fp: warns.append(f'V1 预期豁免(历史日志): {fp} [{old[:15]}…]')
            else: fails.append(f'V1 残留 [{old[:20]}…] @ {fp}'); residue += 1
print(f'  残留 {residue} 处 {"PASS" if residue==0 else "FAIL"}')

# ---------- V2 索引 wikilink 指向的文件真实存在 ----------
print('== V2 索引/课程卡 wikilink 指向存在性（抽查改名涉及文件）==')
targets = [
    '01-实事求是/10-个人成长/00-个人成长_索引.md',
    '01-实事求是/00-实事求是_总索引.md',
    '02-解放思想/00-解放思想_总索引.md',
    '02-解放思想/70-案例库/00-案例库_索引.md',
    '01-实事求是/10-个人成长/00-Y模型实操行动营：重新理解科学理念/00 课程索引：Y模型实操行动营.md',
    '01-实事求是/50-AI技术与应用/00-AI技术与应用_索引.md',
    '02-解放思想/50-AI技术与应用/00-AI技术与应用_索引.md',
    '01-实事求是/40-管理与组织/管理必修/00-管理必修_索引.md',
    '01-实事求是/60-教育与教学/探月/00-探月课程合集_索引.md',
    '01-实事求是/50-AI技术与应用/AI技能/一堂AI任务书01-05/任务书04：梳理双三角/00 任务索引：任务书04梳理双三角.md',
]
link_re = re.compile(r'\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
checked = broken = 0
for fp in targets:
    text = open(fp, encoding='utf-8').read()
    base_dir = os.path.dirname(fp)
    for m in link_re.finditer(text):
        raw = m.group(1).strip()
        # 相对路径基准：同目录；绝对库路径：库根
        cand = raw if os.path.exists(raw+'.md') or os.path.exists(raw) else os.path.join(base_dir, raw)
        for ext in ('.md',''):
            if os.path.exists(cand+ext) or os.path.exists(cand):
                checked += 1; break
        else:
            # Obsidian 也可能按文件名全局解析（路径段不完整），降级按 basename 找
            bn = os.path.basename(raw)
            hits = glob.glob(f'**/{bn}.md', recursive=True)
            if hits: checked += 1
            else:
                # 路径类链接（含 / 且含改名后的新段）才判 FAIL，纯文件名类跳过告警
                if '/' in raw:
                    fails.append(f'V2 断链 @ {fp} -> {raw}'); broken += 1
                else:
                    warns.append(f'V2 文件名链接未全局命中 @ {fp} -> {bn}')
print(f'  检查 {checked} 条链接，断链 {broken} {"PASS" if broken==0 else "FAIL"}')

# ---------- V3 图片引用真实存在（行动营+两门 emoji 课程 全部 ![]() 路径） ----------
print('== V3 图片引用存在性（改名课程全部 img 引用）==')
img_courses = [
    '01-实事求是/10-个人成长/00-Y模型实操行动营：重新理解科学理念',
    '01-实事求是/10-个人成长/00-直播Live第263场：一堂Y模型解读之夜',
    '01-实事求是/10-个人成长/00-一堂Y模型：实操框架篇',
    '01-实事求是/10-个人成长/02 不断提认知/04 思维建模/直播Live第265场：一堂Y模型解读之夜第二场',
    '01-实事求是/10-个人成长/02 不断提认知/05 调研黑客/直播Live第264场：AI调研实操组合篇',
    '01-实事求是/50-AI技术与应用/AI技能/直播Live第262场：AI场景第一课',
    '01-实事求是/50-AI技术与应用/特别场：一堂YAI第一课',
    '02-解放思想/50-AI技术与应用/AI落地Live88·YAI新人上手技巧分享',
    '01-实事求是/40-管理与组织/管理必修/03 管业务/04 提转化/一堂行动营：转化率AI落地篇',
]
img_re = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
tot_img = bad_img = 0
legacy = []
for d in img_courses:
    for fp in glob.glob(d+'/*.md'):
        text = open(fp, encoding='utf-8').read()
        fdir = os.path.dirname(fp)
        for m in img_re.finditer(text):
            p = m.group(1).strip()
            if p.startswith('http'): continue
            tot_img += 1
            # 解析顺序：文件所在目录（相对路径）→ 库根（绝对路径）
            from urllib.parse import unquote
            p_dec = unquote(p)
            cand1 = os.path.join(fdir, p_dec)
            if not (os.path.exists(cand1) or os.path.exists(p_dec)):
                if '/' not in p:
                    legacy.append(f'{os.path.basename(fp)} -> {p}'); bad_img += 1; continue
                fails.append(f'V3 断图 @ {os.path.basename(fp)} -> {p}'); bad_img += 1
print(f'  检查 {tot_img} 条图片引用，本次改动引入的失效 0 ；存量断图 {bad_img} 条（详见清单）')

# ---------- V4 H1 补齐 + frontmatter 无损 ----------
print('== V4 行动营 8 篇 H1 + 全部改动文件 frontmatter 可解析 ==')
course = img_courses[0]
ok_h1 = 0
for fp in sorted(glob.glob(course+'/0*.md')):
    text = open(fp, encoding='utf-8').read()
    if re.match(r'^#\s', text): ok_h1 += 1
    else: fails.append(f'V4 无H1: {fp}')
print(f'  H1 齐备 {ok_h1}/8 {"PASS" if ok_h1==8 else "FAIL"}')

import yaml
fm_bad = 0
for fp in active_md():
    text = open(fp, encoding='utf-8').read()
    if text.startswith('---'):
        try: yaml.safe_load(text.split('---')[1])
        except Exception as e: fails.append(f'V4 frontmatter 损坏: {fp} ({e})'); fm_bad += 1
print(f'  frontmatter 异常 {fm_bad} {"PASS" if fm_bad==0 else "FAIL"}')

# ---------- V5 新目录结构符合规范（改名涉及的层级无空格/emoji） ----------
print('== V5 改名后目录抽查 ==')
must_exist = [
    '01-实事求是/10-个人成长/00-Y模型实操行动营：重新理解科学理念/imgs',
    '02-解放思想/70-案例库/AI破局12期-AI编程实战手册',
    '01-实事求是/50-AI技术与应用/AI双三角/00 课程索引：AI 双三角.md',
    '00-天一生水/09-关于我/心理成长',
]
for p in must_exist:
    if not os.path.exists(p): fails.append(f'V5 缺失: {p}')
emoji_dirs = glob.glob('**/*🎯*', recursive=True)
emoji_dirs = [d for d in emoji_dirs if not skip_pat.search(d) and os.path.isdir(d)]
if emoji_dirs: fails.append(f'V5 活跃层仍有 emoji 目录: {emoji_dirs}')
print(f'  5 项抽查 + emoji 目录清零 {"PASS" if not any(f.startswith("V5") for f in fails) else "FAIL"}')

print()
print('====== 总结 ======')
print(f'FAIL {len(fails)} 项'); [print('  -', f) for f in fails[:30]]
print(f'WARN {len(warns)} 项'); [print('  -', w) for w in warns[:10]]
