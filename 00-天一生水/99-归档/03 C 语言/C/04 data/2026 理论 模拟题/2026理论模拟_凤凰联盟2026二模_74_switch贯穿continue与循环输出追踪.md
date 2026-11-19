---
title: 2026理论模拟 凤凰联盟2026二模 74 switch贯穿continue与循环输出追踪
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2026/凤凰职教高考联盟2026届二轮复习调研测试  计算机二模试卷 .md"
question_id: "2026理论模拟-凤凰联盟2026二模-74"
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

# 2026理论模拟 · 凤凰联盟2026二模 74 · switch贯穿continue与循环输出追踪

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：凤凰职教高考联盟2026届二轮复习调研测试  计算机二模试卷 .md
- 题目原文：

74. 阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char a[][20] = {"sysTem", "forEver", "byte", "viSual"};
    int i, j, s, n = sizeof(a) / sizeof(a[0]), b[10];

    for (i = 0; i < n; i++)
    {
        s = 0;
        for (j = 0; a[i][j]; j++)
        {
            if (!islower(a[i][j]))  // islower(ch) 判断字符 ch 是否为小写字母
                continue;
            switch (a[i][j])
            {
                default: s = s + 1;
                case 'a': case 'b': case 'c': s = s + 2; break;
                case 'h': case 'i': case 'j': s = s + 3; continue;
                case 'r': case 's': case 't': s = 4; break;
            }
        }
        b[i] = s;
    }

    for (i = 0; i < n; i++)
        printf("%5d", b[i]);
    return 0;
}
```

- 作答要求：写出程序运行结果。

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

- 原始真题：[[凤凰职教高考联盟2026届二轮复习调研测试  计算机二模试卷 ]]
- 切片文件：[[2026理论模拟_凤凰联盟2026二模_74_switch贯穿continue与循环输出追踪]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
