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
        i. 题型相同：+1。
        i. 答案相关考点相同：+3。
        i. 解题动作相同：+3。
        i. 易错点相近：+1。
        i. 难度略高：+0。
        i. 总分：8/10。

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
        i. 题型相同：+1。
        i. 答案相关考点部分相同：+2。
        i. 解题动作相同：+3。
        i. 易错点相近：+1。
        i. 难度接近：+1。
        i. 总分：8/10。

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
        i. 题型相同：+1。
        i. 答案相关考点不同：+0。
        i. 解题动作相同：+3。
        i. 易错点部分相同：+1。
        i. 难度接近：+1。
        i. 总分：6/10。


