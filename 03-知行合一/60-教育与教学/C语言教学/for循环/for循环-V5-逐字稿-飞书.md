---
title: for 循环学生讲义 V4
type: 学生讲义
course_type: 实操课
version: 4.0
source:
  - 02 process/备课与复盘/for循环-V3.md
created: 2026-06-11
updated: 2026-06-11
tags:
  - C语言
  - for循环
  - 实操课
  - 学生讲义
status: draft
---
# 开始上课

  

Hello，大家好啊，

  

我是panda，许久未见~~

  

欢迎大家回来继续(来到)上课，进入**本周末的成长加速时间。**

  

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=MGQwN2NlMmI2Mjc0OGQ4NTY3ZDY0YWM2ZTM1MDk0MzVfOFFvTkM2a3YwazNzUmp1TzJMY1oyODRJcjdaMmNRb2RfVG9rZW46Q2FwUGJNOTRCb3o5TGd4Vmx1VmNBbTJobm9lXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

  

这是我的介绍，如果直播间有新人的话，自己读一下吧:

> 1. 传智学院讲师:2021 年年加入传智教育，现为专业课讲师。
>     
> 2. 前格家网络技术专家:擅长从0到1业务探索、产品快速起盘、商业分析。
>     
> 3. 中职课程总设计师:研发100节职教高考课程，收到50万份作业。
>     
> 4. 搭建系统：成绩分析系统
>     

  

【热场】来来来，我们热个身吧，如果让之前的学长和学姐，推荐 C 语言课程最难理解的知识点，大家猜下，他们会推荐哪个？

  

  

没错，就是循环，特别是分析循环代码的时候，简直就是一个噩梦，也是很多同学的一个分水岭，希望大家一定加油。

  

我曾经无数次说过一句话:只要方法对，得 C 语言者得专业课，得循环者得 C 语言。

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=YjBiOTk5NWE1NmZjZDRjOWQxMTRhOWVmYjZjZjRjYjBfa090UDZhSVM2dk11OWlWbnJQcGtJbTZqd2NtWFd4UEtfVG9rZW46RG5kcmJFdnQ2b2R4UlF4SFdTMmMxV0hxbkpuXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

## 快速回顾

- 选择语句：`if` / `switch`
    

```C
#include <stdio.h>
int main() {
    int x=1;
    switch(x)
    {
            case 1:case 2:printf("%d",x++);
            case 3:printf("%d",x++);
            default:printf("%d",x++);
    }
    return 0;    
}
```

  

【提醒】听这节课的前提是，我们默认大家已经学会了选择语句，也就是 if 和 switch。后面的循环经常结合选择语句来考，如果你对选择语句还不太熟悉的话，一定要花时间将它啃掉。

  

接下来，我们讲循环，看看循环到底是个什么东西？为什么这么难呢？?这就是我们这节课要研究的问题。

  

  

## 为什么要学？

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=NDM5MGJmNWI5MjY0MDhlNjIzNDhmZTRhNjUwZDlkZjFfQ2k2dFhlRGl3T3pXbk9KcTFWMjFFU0hjaU8yWUR5TUVfVG9rZW46SU40OWJaaDI3b1hFQ1d4TEs4T2NRTVkybkhoXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

1. 高考重点：题量多，专业课就靠 C 语言拉开差距
    
2. 系列课：循环决定后面所有内容！
    

  

  

## 预热思考题

来来，照例，给大家一个预热思考题吧

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=NzhkOWIzYjQ3NmVhNzhiOTI0ZjUxYjJmZmM5ZTFhZjVfVUV2Vk1ocUVGTVFjeDFrOWVRMXZHcXhTTG5meFJIUTVfVG9rZW46Q1lmbWJWUklzb3NNQ3V4VVZlaWM5UjRublp6XzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

  

  

> 上次做的计算器代码，每计算一次都要重新运行程序，有没有啥办法，我可以实现重复计算呢？

  

## 提前划重点

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=OTBjMGY3OWYyNDBlYTM5YzkwMDBhZWM2OWYzNWZhY2FfRGZPazVwNEtNZ3FjV3hZNFJWaG5ZWVZMSTNoTkNiVUpfVG9rZW46SDBBdGJ2dE5rb0ZsMmV4MTR0b2NiS2FqblJoXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

提前划一下重点，大家不要迷路，今天我会讲2个话题:

第一步，初步体感。我会通过一个案例的困扰，引出循环。

第二步，开始理解。我会给大家讲循环的类型，以及循环具体的结构，如何编写。

第三步，执行流程。总结成一个模型，就是如何去写循环的代码。

第四步，**作业和 candy**。

  

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjc4OTQwZTA0NmQyNDU2OGM0ODY4MzAzOWRjMmU3YzVfQ1p3Tk5uYmNRQk1LME1MUzJORm5CVUc3Q3ZtZGlkVjFfVG9rZW46QjdiZ2JFMm5sbzBUQ0l4Z3gydGNuWjE2bkdnXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

  

【毛遂自荐】欢迎大家主动报名"学习委员"，谁愿意?在评论区扣一个:我愿意 请大家积极报名学习委员，提升上课质量。

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=OThiYTIyZjcwY2M4ODQwMDBiYjkzYjg2NTc2ZDlkOTVfNmN5SXozYzN5bEJ2bExPbVE5ZkRTdkNuVXlQZVpDc1RfVG9rZW46RkpTamJFZklCb1J6azN4QThlVWNhWHFyblB1XzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

**"认真用一个晚上写作业，换来未来1年的更好水平+持续做事****复利****"**

欢迎大家勇敢一点，把旗子插到山上，把自己的鞋子扔到墙对面去~!

  

来来来，希望大家一起立一个Flag(承诺)，认真听课吸收，最后完成这次训练作业。

扣一句话吧:一定作业!!

  

OK，进入第一个话题。

  

# 体感:为何需要循环

如果要打印 5 遍“我爱 C 语言”，可以这样写：

```C
#include <stdio.h>

int main() {
    printf("我爱 C 语言!\n");
    printf("我爱 C 语言!\n");
    printf("我爱 C 语言!\n");
    printf("我爱 C 语言!\n");
    printf("我爱 C 语言!\n");
    return 0;
}
```

这段代码结果是对的，但问题很明显：

- 代码太重复
    

由于重复，就引出下面三个问题：

1. 太麻烦
    
2. 如果次数变成 50 次、100 次，代码会很长
    
3. 修改内容时，每一行都要跟着改
    

```C++
#include <stdio.h>
  int main() {
      double num1, num2, result;   
      char operator;

      printf("请输入第一个数字：");
      scanf("%lf", &num1);
      printf("请输入运算符(+, -, *, /)：");
      scanf(" %c", &operator);
      printf("请输入第二个数字：");
      scanf("%lf", &num2);

      if (operator == '+') {
          result = num1 + num2;
          printf("%.2f + %.2f = %.2f\n", num1, num2, result);
      } else if (operator == '-') {
          result = num1 - num2;
          printf("%.2f - %.2f = %.2f\n", num1, num2, result);
      } else if (operator == '*') {
          result = num1 * num2;
          printf("%.2f * %.2f = %.2f\n", num1, num2, result);
      } else if (operator == '/') {
          if (num2 != 0) {
              result = num1 / num2;
              printf("%.2f / %.2f = %.2f\n", num1, num2, result);
          } else {
              printf("错误：除数不能为0！\n");
          }
      } else {
          printf("错误：无效的运算符！\n");
      }

      return 0;
  }
```

问题也很明显：

每次都要手动重复运行

  

![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2E0MzM4MDgxZTEzNTY5MmI1ZDkzOWQwYzk4MWVlNGNfUjNYVDRuZFdEbU8xaTVTWlBJVnVDYUZzdHpHc3A2a2ZfVG9rZW46TkxQSWJrdGNpb0RqQ1p4Rnp5b2N1UElFbjNkXzE3ODE1MDQwNjM6MTc4MTUwNzY2M19WNA&add_watermark=true&scene_type=CCM)

它在提醒你：这里有结构，可以交给循环。

# 理解:循环写法

  

在 C 语言中，循环有三种写法，需要懂其中一种，剩下的俩种只是形式不同。

> 1. for
>     
> 2. while
>     
> 3. do...while
>     

  

## for 循环的基本结构：

```C
int i;
for (初始化语句; 条件判断语句; 条件控制语句) {
    循环体语句;
}
```

哈哈，咱们先看个视频

  

## 如何实现循环代码？

括号里有三个位置，还有两个分号，可能有点乱。不要先死背格式，先记住四个问题：

```Plain
写 for 循环，先问四句话：

1. 从哪开始？
2. 到哪结束？
3. 每次怎么变？
4. 重复做什么？
```

  

对应到代码：

```C
for (从哪开始; 到哪结束; 每次怎么变) {
    重复做什么;
}
```

  

### 四问解释表

|   |   |   |   |
|---|---|---|---|
|四问|for 中的位置|例子1：安娜|例子 2:循环打印 5 次 C语言|
|从哪开始？|初始化语句|||
|到哪结束？|条件判断语句|||
|每次怎么变？|条件控制语句|||
|重复做什么？|循环体|||

  

### 口诀

> **先定起点，再定终点；每轮变一次，身体做重复。**

---

## 案例 1：打印 1 到 5

### 需求

打印 1 到 5。

### 先写四问

|   |   |
|---|---|
|四问|本题答案|
|从哪开始？||
|到哪结束？||
|每次怎么变？||
|重复做什么？||

  

### 对答案

|   |   |
|---|---|
|四问|本题答案|
|从哪开始？|从 1 开始，所以 i = 1|
|到哪结束？|到 5 结束，而且 5 要打印，所以 i <= 5|
|每次怎么变？|每次加 1，所以 i++|
|重复做什么？|打印当前的 i|

  

---写代码-------

### 对代码

```C
#include <stdio.h>

int main() {
    int i;

    for (i = 1; i <= 5; i++) {
        printf("%d\n", i);
    }

    return 0;
}
```

### 代码理解

- `int i;`：定义循环变量，负责一轮一轮地走。
    
- `i = 1`：从 1 开始。
    
- `i <= 5`：只要 i 没有超过 5，就继续执行。
    
- `i++`：每一轮结束后，i 往前走一步。
    
- `{ printf("%d\n", i); }`：每一轮都打印当前的 i。
    

### 想一想

如果把：

```C
i <= 5
```

改成：

```C
i < 5
```

输出会少哪个数？

答案：会少 `5`。

  

### 小结

循环里最容易出错的地方，经常不是语法，而是边界。

一个等号，就可能少处理一个数据。

  

# 循环执行流程

for 循环不是“从左到右走一遍”，而是反复经历：判断、执行、变化。

### 代码

```C
#include <stdio.h>

int main() {
    int i;

    for (i = 1; i <= 3; i++) {
        printf("i = %d\n", i);
    }

    printf("结束时 i = %d\n", i);
    return 0;
}
```

### 运行前先猜

这段代码会打印几行？最后 `i` 是几？

### 预期输出

```Plain
i = 1
i = 2
i = 3
结束时 i = 4
```

### 执行流程

```Plain
① 执行 i = 1        只执行一次
② 判断 i <= 3       成立，进入循环体
③ 执行 printf
④ 执行 i++          i 变成 2
⑤ 回到②继续判断

当 i 变成 4 时：
判断 i <= 3 不成立，循环结束。
```

最容易忽略的是最后的 `4`。 因为 i 打印完 3 以后，还会先执行一次 `i++`，变成 4，再去判断。判断不成立，循环才结束。

### 小结

for 的执行顺序是：

```Plain
起点一次
判断多次
身体多次
变化多次
```

---

## 课堂练习：反向输出 5 到 1

### 需求

打印 5 到 1。

### 先写四问

|   |   |
|---|---|
|四问|本题答案|
|从哪开始？|从 5 开始，所以 i = 5|
|到哪结束？|到 1 结束，而且 1 要打印，所以 i >= 1|
|每次怎么变？|每次减 1，所以 i--|
|重复做什么？|打印当前的 i|

### 完整代码

```C
#include <stdio.h>

int main() {
    int i;

    for (i = 5; i >= 1; i--) {
        printf("%d ", i);
    }

    return 0;
}
```

### 预期输出

```Plain
5 4 3 2 1
```

### 代码理解

这题没有新语法，只有方向变了。

- 正向走：从小到大，通常用 `i++`
    
- 反向走：从大到小，通常用 `i--`
    
- 条件也要跟着方向变，不能再写 `i <= 5`
    

### 常见错误

错误写法：

```C
for (i = 5; i <= 1; i--)
```

这个循环不会执行。因为一开始 `5 <= 1` 就不成立。

### 小结

写循环时，起点、终点、变化方向必须是一套。

如果方向反了，循环要么不走，要么走不出去。

  

本节总结

写 for 循环时，不要只背格式，先问四句话：

```Plain
1. 从哪开始？
2. 到哪结束？
3. 每次怎么变？
4. 重复做什么？
```

# 作业和 candy

## 练习题

1. 键盘录入一个正整数 `n`，求 1 到 n 之间所有奇数的和。
    
2. 发挥想象力，你觉得循环应该怎么使用？最小公倍数，按权展开这些用 C 语言代码怎么写？
    

  

## candy

1. 讲解的文稿，打印版
    
2. 前三名：奖励体质能量一瓶
    
3. 技能真题/理论真题
    

  

## 限时检测

循环四问是哪四问？

|   |   |
|---|---|
|四问|提示|
|从哪开始？|i = 1|
|到哪结束？|i <= n|
|每次怎么变？|可以 i++ 后用 if 判断，也可以 i += 2|
|重复做什么？|把奇数加到 sum 里|