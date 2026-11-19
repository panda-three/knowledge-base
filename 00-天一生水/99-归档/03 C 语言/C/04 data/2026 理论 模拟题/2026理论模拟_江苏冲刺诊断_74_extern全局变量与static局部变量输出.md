---
title: 2026理论模拟 江苏冲刺诊断 74 extern全局变量与static局部变量输出
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2026/江苏省2026年中职职教高考冲刺阶段教学质量诊断分析   计算机试卷.md"
question_id: "2026理论模拟-江苏冲刺诊断-74"
year: 2026
exam_type: 理论模拟题
importance: 重要
question_type: 程序阅读题
difficulty: ⭐⭐⭐
version: V3
tags:
  - C语言
  - 2026理论模拟题
  - 程序阅读题
  - extern全局变量引用
  - static局部变量保值
  - 函数调用中的自增副作用
  - 区分函数内 extern 引用的全局变量
  - 追踪 static i 在两次 fun 调用中的保留值
  - 把 static i 每次调用都重置为 0
related_questions: []
---

# 2026理论模拟 · 江苏冲刺诊断 74 · extern全局变量与static局部变量输出

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：江苏省2026年中职职教高考冲刺阶段教学质量诊断分析   计算机试卷.md
- 题目原文：

74.阅读下列程序、把运行结果填写在答题卡上相应位置。

include<stdio.h>
void fun(int j）
cxtcrn int abi
sttic inti=0
int ci
c=i+j；
a=++i；
b=j++；
prind（"c=%d,i=%d,j=%d\n”，c,i,j）；
int a=0,b=1；
int main()
a=1；b=2；
fun(b）；
fm(a）；
print（"a=%d，b=%d\n",a,b）；
return 0；

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - extern全局变量引用
    - static局部变量保值
    - 函数调用中的自增副作用
- 解题动作：
    - 区分函数内 extern 引用的全局变量
    - 追踪 static i 在两次 fun 调用中的保留值
    - 判断 ++i 与 j++ 的先后效果
    - 按函数调用顺序整理每次 printf 输出
- 易错点：
    - 把 static i 每次调用都重置为 0
    - extern 变量和局部变量混淆
    - 前置自增和后置自增效果看反
- 相似题搜索标签：`extern` `static` `全局变量` `自增` `函数调用`
- 难度：⭐⭐⭐

## 三、来源

- 原始真题：[[江苏省2026年中职职教高考冲刺阶段教学质量诊断分析   计算机试卷]]
- 切片文件：[[2026理论模拟_江苏冲刺诊断_74_extern全局变量与static局部变量输出]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
