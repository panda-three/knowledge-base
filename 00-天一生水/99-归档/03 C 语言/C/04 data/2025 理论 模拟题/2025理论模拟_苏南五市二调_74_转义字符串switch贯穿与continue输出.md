---
title: 2025理论模拟 苏南五市二调 74 转义字符串switch贯穿与continue输出
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/2025年苏南五市职业学校职教高考第二次调研性统测 计算机应用专业综合理论试卷.md"
question_id: "2025理论模拟-苏南五市二调-74"
year: 2025
exam_type: 理论模拟题
importance: 重要
question_type: 程序阅读题
difficulty: ⭐⭐⭐⭐
version: V3
tags:
  - C语言
  - 2025理论模拟题
  - 程序阅读题
  - 转义字符与字符串截断
  - switch-case贯穿
  - continue与break输出路径
  - 识别字符串中的转义字符和 \0 截断位置
  - 按 k=k+2 取字符
  - 忽略 \0 后内容不参与遍历
related_questions: []
---

# 2025理论模拟 · 苏南五市二调 74 · 转义字符串switch贯穿与continue输出

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：2025年苏南五市职业学校职教高考第二次调研性统测 计算机应用专业综合理论试卷.md
- 题目原文：

74.阅读下列程序，请将运行结果填写在相应位置。

```c
#include<stdio.h>
main江( )
{char s[]="\\BAD\x43!$DA@C&DI\0*ABD"; int k; char c;
for(k=1 ;(c=s[k])!='\0';k=k+2)
{ switch(c) 74. 运行结果为：
{
case 'A':putchar('%');continue;
case 'B':++k;break;
default:putchar('*');
case 'D':putchar('&');continue;
}
putchar('#');
}}
职教高考第二次调研性统测试卷《计算机应用专业综合理论》 第10页 共20页

<!-- page 11 -->

```

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - 转义字符与字符串截断
    - switch-case贯穿
    - continue与break输出路径
- 解题动作：
    - 识别字符串中的转义字符和 \0 截断位置
    - 按 k=k+2 取字符
    - 匹配 switch 分支并判断贯穿
    - 区分 break 后的 putchar 和 continue 跳过
- 易错点：
    - 忽略 \0 后内容不参与遍历
    - default 贯穿到 case D 漏算
    - break 与 continue 后续输出路径混淆
- 相似题搜索标签：`转义字符` `字符串结束符` `switch贯穿` `continue` `putchar`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[2025年苏南五市职业学校职教高考第二次调研性统测 计算机应用专业综合理论试卷]]
- 切片文件：[[2025理论模拟_苏南五市二调_74_转义字符串switch贯穿与continue输出]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
