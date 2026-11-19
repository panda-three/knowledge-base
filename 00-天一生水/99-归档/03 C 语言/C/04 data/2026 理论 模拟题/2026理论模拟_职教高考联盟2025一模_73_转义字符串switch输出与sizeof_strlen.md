---
title: 2026理论模拟 职教高考联盟2025一模 73 转义字符串switch输出与sizeof_strlen
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2026/15-计算机专业-2025年职教高考联盟计算机一模试卷.md"
question_id: "2026理论模拟-职教高考联盟2025一模-73"
year: 2026
exam_type: 理论模拟题
importance: 重要
question_type: 综合理论题
difficulty: ⭐⭐⭐
version: V3
tags:
  - C语言
  - 2026理论模拟题
  - 综合理论题
  - 转义字符与字符串结束符
  - switch-case分支执行
  - sizeof与strlen区别
  - 识别转义字符和 \0 截断位置
  - 逐字符匹配 switch 分支
  - 忽略 \0 后内容不参与 strlen
related_questions: []
---

# 2026理论模拟 · 职教高考联盟2025一模 73 · 转义字符串switch输出与sizeof_strlen

## 一、题目内容

- 题号：73
- 题型：综合理论题
- 原始试卷：15-计算机专业-2025年职教高考联盟计算机一模试卷.md
- 题目原文：

73.阅读下列程序，请将①\~④表示的内容填写在答题卡中的相应位置：

(1） #include <stdio.h>

(2） #include <string.h>

(3) #define N 18

(4) void main(

(5）{char a[N]="\\AB\103%D\66\0BCA";

（6） char c;

（7) int i;

```c
(8） for(i=1;a[i];i++)
（9） { c=a[i];
(10) switch(c)
(11) {
(12) case 'A' :putchar(c+1) ;break;
(13) case 'B' :putchar(c-1) ;i++;continue;
(14) case 'C' :putchar(c+1) ;break;
(15) default:putchar('#'） ;break;
(16) }
(17) putchar(' @）;
(18) }
(19) printf("\nsize=%d,len=%d\n",sizeof(a),strlen(a));
(20)}
```

上述程序中：第（3）行定义的N是一个 ①▲ \_；本程序中使用到的库函数有 ② \_；在 Dev C++ 编程环境中，sizeof 的功能是 ③此题中字符‘%’对应的输出是 ④ 。

## 二、标签

- 重要性：重要
- 题型：综合理论题
- 答案相关考点：
    - 转义字符与字符串结束符
    - switch-case分支执行
    - sizeof与strlen区别
- 解题动作：
    - 识别转义字符和 \0 截断位置
    - 逐字符匹配 switch 分支
    - 区分数组容量和字符串长度
- 易错点：
    - 忽略 \0 后内容不参与 strlen
    - 把 sizeof 当 strlen
    - continue 后续执行位置判断错
- 相似题搜索标签：`转义字符` `字符串结束符` `switch` `sizeof` `strlen`
- 难度：⭐⭐⭐

## 三、来源

- 原始真题：[[15-计算机专业-2025年职教高考联盟计算机一模试卷]]
- 切片文件：[[2026理论模拟_职教高考联盟2025一模_73_转义字符串switch输出与sizeof_strlen]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
