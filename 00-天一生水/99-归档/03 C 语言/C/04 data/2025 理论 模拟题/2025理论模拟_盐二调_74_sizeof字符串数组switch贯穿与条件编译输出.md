---
title: 2025理论模拟 盐二调 74 sizeof字符串数组switch贯穿与条件编译输出
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/2025盐二调计算机专业试卷.md"
question_id: "2025理论模拟-盐二调-74"
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
  - sizeof与字符串结束符
  - switch无break贯穿计数
  - 条件编译分支
  - 计算字符数组总容量 sizeof
  - 遍历到第一个 \0 前统计字符
  - 把 sizeof 当 strlen
related_questions: []
---

# 2025理论模拟 · 盐二调 74 · sizeof字符串数组switch贯穿与条件编译输出

## 一、题目内容

- 题号：74
- 题型：程序阅读题
- 原始试卷：2025盐二调计算机专业试卷.md
- 题目原文：

74．阅读下列程序，写出程序运行结果。

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define flag 1
int main()
{char str[30]="2025 We meet\0every where!",c;//词之间空格仅一个
int i=0,num=0,other=0,size;
size=sizeof(str);
printf("size=%d\n",size);
for(i=0;str[i];i++)
switch(isdigit(str[i]))
{case 1:num++;
case 0:other++;
}
printf("num=%d\nother=%d\n",num,other);
i=0;
while((c=str[i])!='\0')
{ i++;
#if flag
if(c>='a'&&c<='z') c=c-32;
#else
if(c>='A'&&c<='Z') c=c+32;
#endif
printf("%c",c);
}
printf("\n");
}
```

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - sizeof与字符串结束符
    - switch无break贯穿计数
    - 条件编译分支
- 解题动作：
    - 计算字符数组总容量 sizeof
    - 遍历到第一个 \0 前统计字符
    - 判断 switch(isdigit()) 无 break 的贯穿效果
    - 根据 #if flag 选择大小写转换分支
- 易错点：
    - 把 sizeof 当 strlen
    - case 1 没有 break 导致 other 也增加
    - 忽略 \0 后 every where 不输出
- 相似题搜索标签：`sizeof` `字符串结束符` `switch贯穿` `isdigit` `条件编译`
- 难度：⭐⭐⭐⭐

## 三、来源

- 原始真题：[[2025盐二调计算机专业试卷]]
- 切片文件：[[2025理论模拟_盐二调_74_sizeof字符串数组switch贯穿与条件编译输出]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
