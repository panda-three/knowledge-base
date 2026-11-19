---
title: switch分支执行与格式化输出练习组
type: 练习题组
source_question: "[[03 Areas/03 C 语言/C/04 data/2026 年真题/V3/2026真题_74_switch分支赋值与格式化输出]]"
created: 2026-06-08
status: 已校准
version: V2
based_on: "[[31 相似题练习组模板-V3]]"
from: "[[03 Areas/03 C 语言/C/04 data/练习题组/V1/switch分支执行与格式化输出练习组-人工改]]"
tags:
  - C语言
  - 练习题组
  - switch-case
  - break贯穿
  - printf格式化输出
  - 变量追踪
  - 分支匹配
---

# switch 分支执行与格式化输出 练习组 · 2026 起点

## 一、起点题

- 题目卡：[[03 Areas/03 C 语言/C/04 data/2026 年真题/V3/2026真题_74_switch分支赋值与格式化输出]]
- 题型：程序阅读题 / 输出结果题 / 分支执行题
- 答案相关考点：`switch-case`、`break`、`printf` 格式化输出、`%7.2f` 浮点输出
- 解题动作：判断 `level` 初值 → 匹配 `case 1` → 确认 `break` 终止 switch → 追踪 `dct=0.7` → 计算 `r*d*dct` → 按 `%7.2f` 写出输出
- 易错点：选错 switch 入口、漏看 `break`、`dct` 最终值判断错、小数位数或输出宽度写错
- 难度：⭐⭐

## 二、练习路径（按顺序推送）

### 第一题 · 同构题（高相似 8 分）

- 题目来源：2024 年真题 · 第 74 题
- 切片文件：[[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2024]] 第 74 题
- 相似度：8 分
- 各项得分：
    - 题型相同：是，都是程序阅读输出题 (+1)
    - 考点相同：`switch-case`、`break`、`printf` 格式化输出 (+3)
    - 动作相同：判断 switch 入口 → 判断是否被 `break` 截断 → 追踪变量变化 → 按格式写输出 (+3)
    - 易错点相同：是，都会错在 switch 入口、`break` 和格式输出 (+1)
    - 难度接近：否，本题多了字符数组下标、进位和字符串截断，明显更高 (+0)
- 推荐理由：这题和起点题同样围绕 switch 入口、break 终止、格式输出展开，但复杂度略高，适合作为第一道巩固后的加压同构题。
- 题目切片：

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

### 第二题 · 变式题（中相似 7 分）

- 题目来源：2023 年真题 · 第 74 题
- 切片文件：[[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2023]] 第 74 题
- 相似度：7 分
- 各项得分：
    - 题型相同：是，都是程序阅读输出题 (+1)
    - 考点相同：`switch-case` 与 `break` 相同，但不再考浮点格式化输出 (+3)
    - 动作相同：追踪变量初值 → 匹配 case 入口 → 确认 `break` → 按 printf 顺序写输出 (+3)
    - 易错点相同：否，本题更容易错在 `for` 循环输出星号和输出顺序，不是 `%7.2f` 宽度 (+0)
    - 难度接近：否，本题混入 `strlen` 循环输出，步骤更多 (+0)
- 与起点题差异：起点题是 switch 后进行数值计算和浮点格式输出；本题先用循环输出密码遮挡，再用字符变量 `key` 进入 switch 输出菜单项。
- 推荐理由：同样要用 switch 分支追踪，但外面加了一段循环输出，能测试学生是否只会看 switch，还是能按程序执行顺序完整写输出。
- 题目切片：

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

### 第三题 · 迁移题（5 分）

- 题目来源：2025 年真题 · 第 74 题
- 切片文件：[[03 Areas/03 C 语言/C/03 刻意练习/理论/真题/2026-05-18-真题-2025]] 第 74 题
- 相似度：5 分
- 各项得分：
    - 题型相同：是，都是程序阅读输出题 (+1)
    - 考点相同：否，考点从 `switch-case` 换成变量交换和 `if-else` 多分支 (+0)
    - 动作相同：追踪变量变化 → 判断分支入口 → 按 `printf` 格式写输出 (+3)
    - 易错点相同：否，本题没有 `switch` 入口和 `break`，主要错在变量交换后再判断条件 (+0)
    - 难度接近：是，都是短程序输出题，追踪量不大 (+1)
- 推荐理由：表面上不再考 switch，但仍然要求学生完成“逐行追踪变量 → 判断进入哪个分支 → 按格式写输出”的通用动作，适合作为从 switch 分支迁移到 if-else 分支的第三题。
- 题目切片：

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

## 三、组内信息

- 总题数：3
- 覆盖考点：`switch-case`、`break`、`printf` 格式化输出、字符数组下标、`for` 循环输出、`if-else` 多分支、变量交换
- 覆盖动作：变量追踪、分支匹配、判断 `break`、按程序顺序写输出、按格式控制输出
- 难度跨度：⭐⭐ → ⭐⭐⭐
- 推送节奏：先巩固 switch 同构动作，再加入循环输出干扰，最后迁移到 if-else 分支判断

## 四、使用记录

- 首次使用日期：待填写
- 学生完成情况：待填写
- 学生反馈：待填写
- 回流标记：待填写

## 五、质量检查（生成后逐条过）

- [x] 三道题按同构 → 变式 → 迁移顺序排列
- [x] 每道题有完整的各项得分拆解（五项，逐项标 +1/+3）
- [x] 第一题相似度 ≥ 8 分
- [x] 第三题相似度 4–5 分，考点不同但解题动作相同
- [x] 不在练习组中写完整学生版讲解
- [x] 第一题：有题目来源、切片文件、各项得分拆解、推荐理由
- [x] 第二题：有题目来源、切片文件、各项得分拆解、与起点题差异、推荐理由
- [x] 第三题：有题目来源、切片文件、各项得分拆解、推荐理由（含迁移说明）
