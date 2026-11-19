---
title: 2025理论模拟 职教高考联盟二模 74 do-while中switch贯穿与continue追踪
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/2025年职教高考联盟计算机二模试卷.md"
question_id: "2025理论模拟-职教高考联盟二模-74"
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
  - switch-case贯穿
  - continue作用层级
  - 八进制整型常量
  - 把 int k=3.7 截断为整数
  - 识别 012 是八进制常量
  - 012 当成十进制 12
related_questions: []
---

# 2025理论模拟 · 职教高考联盟二模 74 · do-while中switch贯穿与continue追踪

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：2025年职教高考联盟计算机二模试卷.md
- 题目原文：

74.阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include<stdio.h>
voidmain()
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
计算机专业综合理论试卷 第 9 页 （共15 页）

<!-- page 10 -->

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
    - switch-case贯穿
    - continue作用层级
    - 八进制整型常量
- 解题动作：
    - 把 int k=3.7 截断为整数
    - 识别 012 是八进制常量
    - 按 k-- 进入 switch 分支
    - 判断 continue 作用于 do-while 循环
- 易错点：
    - 012 当成十进制 12
    - default 贯穿漏算
    - continue 跳出层级判断错
- 相似题搜索标签：`switch` `case` `default` `continue` `八进制常量` `do-while`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[2025年职教高考联盟计算机二模试卷]]
- 切片文件：[[2025理论模拟_职教高考联盟二模_74_do-while中switch贯穿与continue追踪]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
