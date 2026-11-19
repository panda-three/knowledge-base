---
title: 2026理论模拟 职教高考联盟2026一模 73 switch贯穿continue与循环输出追踪
type: question-card-v3
status: draft
created: 2026-06-09
source:
  - "07 项目 ing/C/03 刻意练习/理论/模拟/2026/2026年职教高考联盟计算机一模试卷.md"
question_id: "2026理论模拟-职教高考联盟2026一模-73"
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

# 2026理论模拟 · 职教高考联盟2026一模 73 · switch贯穿continue与循环输出追踪

## 一、题目内容

- 题号：73
- 题型：程序阅读题
- 原始试卷：2026年职教高考联盟计算机一模试卷.md
- 题目原文：

73.阅读下列程序，请将①～④表示的内容填写在答题卡上相应位置。

(1） #include <stdio.h>
(2）int main(void)
(3){char s[ ]="This is a C pro\0gram.";
(4) int k;
(5) char c;
(6) s[8]='\0' ;
（7) puts(s) ;
(8） for(k=2;k<6;k++)
（9) {switch(c=s[k])
(10) { case'i': printf("%s","FIL");
(11) case 's' : ++k;break;
(12) default : puts("Users");
(13) case'r': puts("include") ;
(14) continue;
(15) }
(16) printf("%8s\n","Files") ;
(17) }

(18) return 0;
(19)}

上述程序中，第（3）行中数组s在内存中的占用空间为①字节；第（6）行中的字符串结束符'\0'属于\_②字符；第（14）行continue;语句执行结束后，程序将继续执行第③行内容；第（16）行中“%8s”中的8用于指定输出数据的④

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

- 原始真题：[[2026年职教高考联盟计算机一模试卷]]
- 切片文件：[[2026理论模拟_职教高考联盟2026一模_73_switch贯穿continue与循环输出追踪]]
- 校准人：
- 校准日期：

## 质量检查

- [ ] 不看原卷只看题目卡，能做这道题
- [ ] 答案相关考点 1–3 个，不是所有出现的知识点
- [ ] 解题动作用动词开头
- [ ] 易错点能反向生成练习题
- [ ] 相似题搜索标签从答案相关考点反推
- [ ] 难度基于学生实际错误率，不是感觉
