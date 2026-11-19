---
title: 2025理论模拟 校级联盟滨海中专 74 do-while中switch和continue输出追踪
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/2025计算机-校级联盟滨海中专.md"
question_id: "2025理论模拟-校级联盟滨海中专-74"
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
  - switch-case分支执行
  - continue作用于循环
  - do-while循环条件
  - 用 i%2 判断进入 case 分支
  - 追踪 a 和 i 的更新
  - case 0 识别成字母 O 的 OCR 干扰
related_questions: []
---

# 2025理论模拟 · 校级联盟滨海中专 74 · do-while中switch和continue输出追踪

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：2025计算机-校级联盟滨海中专.md
- 题目原文：

74.阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>
int main()
int a=1,i=10;
do
switch (i%2)
case 1:i--;a=a+4;break;
case O:i--;continue;
if (a>10)
break;
i=i-2;
printf("i=%d\n",i) ;
while(i>O) ;
return 0;
```

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - switch-case分支执行
    - continue作用于循环
    - do-while循环条件
- 解题动作：
    - 用 i%2 判断进入 case 分支
    - 追踪 a 和 i 的更新
    - 判断 continue 跳过后续语句
    - 根据 while 条件决定循环是否继续
- 易错点：
    - case 0 识别成字母 O 的 OCR 干扰
    - continue 后仍执行 if 和 printf
    - do-while 至少执行一次漏判
- 相似题搜索标签：`switch` `continue` `do-while` `变量追踪` `OCR待复核`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[2025计算机-校级联盟滨海中专]]
- 切片文件：[[2025理论模拟_校级联盟滨海中专_74_do-while中switch和continue输出追踪]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
