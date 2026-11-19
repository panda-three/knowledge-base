---
title: 2025理论模拟 镇江一模 80 extern与static变量作用域输出
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/计算机：镇江2023-2024年一模（试卷）.md"
question_id: "2025理论模拟-镇江一模-80"
year: 2025
exam_type: 理论模拟题
importance: 不重要
question_type: 程序阅读题
difficulty: ⭐⭐⭐⭐
version: V3
tags:
  - C语言
  - 2025理论模拟题
  - 程序阅读题
  - extern全局变量引用
  - static局部变量遮蔽
  - 函数实参副作用
  - 区分全局变量和函数内 static 变量
  - 识别 extern 引用外部全局变量
  - OCR 残缺需复核
  - OCR待复核
related_questions: []
---

# 2025理论模拟 · 镇江一模 80 · extern与static变量作用域输出

## 一、题目内容

- 题号：80
- 题型：程序阅读题
- 原始试卷：计算机：镇江2023-2024年一模（试卷）.md
- OCR 状态：OCR待复核，请后续对照原 PDF 人工复核。

- 题目原文：

80、阅读下列程序，并把运行结果填写在题80答题处。

```c
#include"stdio.h"
int y=2;
void fun(int m,int n)
extern int x;
static int y=3;
X=m+n;
m++
幼高考5Szjgk
X =5 0621
void main ()
群432 int i;
for(i=1;i<=3;i+=2){
fun(y=x+5, x) ;
printf("x=%d,y=%d\n",x,y);
‘高
```

## 二、标签

- 重要性：不重要
- 题型：程序阅读题
- 答案相关考点：
    - extern全局变量引用
    - static局部变量遮蔽
    - 函数实参副作用
- 解题动作：
    - 区分全局变量和函数内 static 变量
    - 识别 extern 引用外部全局变量
    - 追踪函数调用实参表达式对变量的影响
    - 按 printf 输出全局 x y
- 易错点：
    - OCR 残缺需复核
    - static y 和全局 y 混淆
    - 实参赋值表达式副作用漏算
- 相似题搜索标签：`extern` `static` `作用域` `实参表达式` `OCR待复核`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[计算机：镇江2023-2024年一模（试卷）]]
- 切片文件：[[2025理论模拟_镇江一模_80_extern与static变量作用域输出]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
