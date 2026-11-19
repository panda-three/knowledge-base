---
title: 2026理论模拟 凤凰职教一模 74 switch贯穿continue与循环输出追踪
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2026/凤凰职教一模.md"
question_id: "2026理论模拟-凤凰职教一模-74"
year: 2026
exam_type: 理论模拟题
importance: 重要
question_type: 程序阅读题
difficulty: ⭐⭐⭐⭐
version: V3
tags:
  - C语言
  - 2026理论模拟题
  - 程序阅读题
  - switch-case分支执行
  - continue作用层级
  - 循环变量更新
  - 匹配 switch 入口表达式
  - 判断 break 和 continue 的执行路径
  - continue 后仍执行后续语句
related_questions: []
---

# 2026理论模拟 · 凤凰职教一模 74 · switch贯穿continue与循环输出追踪

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：凤凰职教一模.md
- 题目原文：

74.阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include<stdio.h>
void main()
{ intk=3.7,m=0;
inta=012,b=4;
do
{ switch(k--)
{ case1:
switch(++m)
{ case1:b++;continue;
default:a++;b++;
case0:a+=2;break;
}


case2:a--;
default:a+=2;b++;
}
}while(k>=0);
printf("a=%d,b=%d,m=%d\n",a,b,m);
}
```

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - switch-case分支执行
    - continue作用层级
    - 循环变量更新
- 解题动作：
    - 匹配 switch 入口表达式
    - 判断 break 和 continue 的执行路径
    - 追踪循环变量和输出语句
- 易错点：
    - continue 后仍执行后续语句
    - case 贯穿漏算
    - OCR 中 0 和 O 混淆
- 相似题搜索标签：`switch` `case` `continue` `break` `变量追踪`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[凤凰职教一模]]
- 切片文件：[[2026理论模拟_凤凰职教一模_74_switch贯穿continue与循环输出追踪]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
