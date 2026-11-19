---
title: 2025理论模拟 高三校际联考 73 进制格式输出转义字符sizeof与strlen
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2025/2024-2025高三校际联考   计算机专业综合试卷.md"
question_id: "2025理论模拟-高三校际联考-73"
year: 2025
exam_type: 理论模拟题
importance: 重要
question_type: 程序阅读题
difficulty: ⭐⭐⭐
version: V3
tags:
  - C语言
  - 2025理论模拟题
  - 程序阅读题
  - printf进制格式输出
  - 转义字符识别
  - sizeof与strlen区别
  - 把十进制数按 %#o 和 %#x 输出
  - 识别八进制和十六进制转义字符
  - %#o %#x 前缀漏写
  - OCR待复核
related_questions: []
---

# 2025理论模拟 · 高三校际联考 73 · 进制格式输出转义字符sizeof与strlen

## 一、题目内容

- 题号：73
- 题型：程序阅读题
- 原始试卷：2024-2025高三校际联考   计算机专业综合试卷.md
- OCR 状态：OCR待复核，请后续对照原 PDF 人工复核。

- 题目原文：

73.阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include"stdio.h"
#include"string.h"
voidmain()
{ intx=79,y=0x1a3;
doublea=0.031345623,b=5.8912345;
chars[]="\116\x61tional\t\x44\141y.\n";
printf("%#o,%#x\n",x,x);
printf("%d,%o\n",y,y);
printf("a=%e,b=%lf\n",a,b);
printf("size=%d,len=%d\n",sizeof(s),strlen(s));
}
第 6 页 共 12 页

<!-- page 7 -->

更多资讯请关注微信公众号: JSSzjgk（江苏省职教高考） 最新资料下载: QQ群432590621
```

## 二、标签

- 重要性：重要
- 题型：程序阅读题
- 答案相关考点：
    - printf进制格式输出
    - 转义字符识别
    - sizeof与strlen区别
- 解题动作：
    - 把十进制数按 %#o 和 %#x 输出
    - 识别八进制和十六进制转义字符
    - 区分 sizeof 数组大小和 strlen 字符串长度
    - 按格式控制符写出输出
- 易错点：
    - %#o %#x 前缀漏写
    - 转义字符算错
    - 把 sizeof 和 strlen 混为一谈
- 相似题搜索标签：`printf` `%#o` `%#x` `转义字符` `sizeof` `strlen`
- 难度：⭐⭐⭐

## 三、来源

- 原始真题：[[2024-2025高三校际联考   计算机专业综合试卷]]
- 切片文件：[[2025理论模拟_高三校际联考_73_进制格式输出转义字符sizeof与strlen]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
