---
title: switch分支执行与格式化输出练习组
type: practice-group
status: draft
created: 2026-06-05
source_question:
  - "07 项目 ing/C/04 data/C/2026 年真题/V3/2026真题_74_switch分支赋值与格式化输出.md"
tags:
  - C语言
  - 练习题组
  - switch-case
  - 程序阅读题
  - 相似题推荐
---

# switch分支执行与格式化输出练习组

1. 题组定位
    a. 起点题是 [[03 Areas/03 C 语言/C/04 data/2026 年真题/V3/2026真题_74_switch分支赋值与格式化输出]]。
    b. 本题组训练学生读懂 **switch 分支执行 + break 终止 + printf 输出格式**。
    c. 题组目标不是讲新知识，而是让学生围绕同一类动作重复练。

2. 核心训练目标
    a. 判断 `switch` 表达式的值。
    b. 找到匹配的 `case` 入口。
    c. 判断 `break` 是否终止 switch。
    d. 追踪变量或字符串的最终值。
    e. 按 `printf` 的格式写出输出结果。

3. 起点题：2026 真题 74
    a. 题目来源
        i. [[03 Areas/03 C 语言/C/04 data/2026 年真题/V3/2026真题_74_switch分支赋值与格式化输出]]。
    b. 相似题角色
        i. 起点题。
        i. 标准样例题。
    c. 答案相关考点
        i. `switch-case`。
        i. `break`。
        i. `printf` 格式化输出。
        i. `%7.2f` 浮点输出。
    d. 核心动作
        i. 判断 `level` 进入 `case 1`。
        i. 根据 `break` 结束 switch。
        i. 确定 `dct=0.7`。
        i. 计算 `r*d*dct`。
        i. 按 `%7.2f` 输出。

4. 相似题 1：2024 真题 74
    a. 题目来源
        i. [[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2024]] 第 74 题。
    b. 相似题类型
        i. 同构题。
        i. 高相似。
    c. 推荐理由
        i. 同样是程序阅读题。
        i. 同样考 `switch-case`。
        i. 同样需要判断 `break`。
        i. 同样需要按 `printf` 格式写输出结果。
        i. 比起 2026 题，多了字符串修改和 case 贯穿，更适合作为第二题。
    d. 题目切片

```c
#include<stdio.h>
int main()
{
    char nums[]="04.951";
    printf("transform\n");
    printf("data:%s\n",nums);
    printf("trans1:%5.1f\n",4.951);
    switch(nums[4])
    {
        case '5':
            if(nums[5]=='0') break;
        case '6':case '7':case '8':case '9':
            nums[3]+=1;
            if(nums[3]>'9') {nums[1]+=1;nums[3]='0';}
            if(nums[1]>'9') {nums[0]+=1;nums[1]='0';}
            break;
    }
    nums[4]='\0';
    printf("trans2:%5s\n",nums);
    return(0);
}
```

    e. 相似度打分
        i. 题型相同：+2。
        i. 答案相关考点相同：+3。
        i. 解题动作相同：+3。
        i. 易错点相近：+1。
        i. 难度略高：+0。
        i. 总分：9/10。
    f. 学生要练的动作
        i. 判断 `nums[4]` 的值。
        i. 判断从 `case '5'` 是否继续贯穿到后续 case。
        i. 判断 `break` 生效位置。
        i. 追踪字符串 `nums` 的修改。
        i. 匹配 `%5.1f` 和 `%5s` 输出格式。

5. 相似题 2：2023 真题 74
    a. 题目来源
        i. [[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2023]] 第 74 题。
    b. 相似题类型
        i. 同考点变式题。
        i. 中高相似。
    c. 推荐理由
        i. 同样是程序阅读题。
        i. 同样考 `switch-case` 和 `break`。
        i. 同样需要写程序输出。
        i. 输出格式比 2026 题简单，但更适合巩固 switch 基础。
    d. 题目切片

```c
#include<stdio.h>
#include<string.h>
int main()
{
    printf("File Edit Help\n");
    char key='F',password[]="123456";
    printf("Option:%c\n",key);
    unsigned int i;
    printf("password:");
    for(i=0;i<strlen(password);i++)
        printf("*");
    printf("\n");
    switch(key)
    {
    case 'F':
        printf("menu:File\n");break;
    case 'E':
        printf("menu:Edit\n");break;
    case 'H':
        printf("menu:Help\n");break;
    default:
        printf("Error.\n");
    }
    return 0;
}
```

    e. 相似度打分
        i. 题型相同：+2。
        i. 答案相关考点部分相同：+2。
        i. 解题动作相同：+3。
        i. 易错点相近：+1。
        i. 难度接近：+1。
        i. 总分：9/10。
    f. 学生要练的动作
        i. 判断 `key` 的值。
        i. 进入对应 `case 'F'`。
        i. 判断 `break` 结束 switch。
        i. 追踪 for 循环输出星号次数。
        i. 按输出顺序写完整结果。

6. 相似题 3：2025 真题 74
    a. 题目来源
        i. [[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2025]] 第 74 题。
    b. 相似题类型
        i. 同动作迁移题。
        i. 中相似。
    c. 推荐理由
        i. 不考 switch，但同样是程序阅读输出题。
        i. 同样训练“判断分支 → 追踪变量 → 按格式输出”。
        i. 适合作为学生从 switch 迁移到 if-else 的第三题。
    d. 题目切片

```c
#include<stdio.h>
int main()
{
    int a=12,b=10,y,t;
    printf("segment:\n");
    printf("a＝%d\n",a);
    t=a;
    a=b;
    b=t;
    printf("a＝%d\tb＝%d\n",a,b);
    if(a>0)y=1;
    else if(b<0)y=-1;
    else b=0;
    printf("y＝%4d\n",y);
    return(0);
}
```

    e. 相似度打分
        i. 题型相同：+2。
        i. 答案相关考点不同：+0。
        i. 解题动作相同：+3。
        i. 易错点部分相同：+1。
        i. 难度接近：+1。
        i. 总分：7/10。
    f. 学生要练的动作
        i. 追踪 `a`、`b` 交换后的值。
        i. 判断 if-else 分支。
        i. 确定 `y` 的最终值。
        i. 匹配 `%d`、`%4d`、`\t` 输出格式。

7. 推荐练习顺序
    a. 第 1 题：2026 真题 74。
        i. 先建立标准动作：switch 入口、break、变量值、格式输出。
    b. 第 2 题：2023 真题 74。
        i. 巩固 switch 菜单输出，难度稳定。
    c. 第 3 题：2024 真题 74。
        i. 增加 case 贯穿和字符串修改，难度提高。
    d. 第 4 题：2025 真题 74。
        i. 迁移到 if-else 分支和格式输出。

8. 教学使用建议
    a. 学生做完 2026 真题 74 后，不要马上讲综合大题。
    b. 先让学生继续做 2023 真题 74，确认 switch 基础稳定。
    c. 再做 2024 真题 74，训练 case 贯穿和字符串修改。
    d. 最后做 2025 真题 74，迁移到 if-else 分支输出。
    e. # 关键判断：这组题练的不是“switch 知识点”，而是“分支执行后写输出”的稳定动作。

9. 后续待办
    a. 后续可以把 2023、2024、2025 的相似题分别拆成 V3 题目卡。
    b. 如果要给学生使用，应补充每题标准答案和学生版讲解。
    c. 如果要做题库系统，应把本题组中的相似度分数结构化。
