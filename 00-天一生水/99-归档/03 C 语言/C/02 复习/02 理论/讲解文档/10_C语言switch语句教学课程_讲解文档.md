# C语言 switch 语句教学课程

## 一、课程导入

同学们好。上一节课我们学习了 `if` 语句的嵌套，重点分析了 `if...else` 相互嵌套时的不同结构。

本节课继续学习条件语句，重点内容是 `switch` 语句。`switch` 语句适合处理多分支选择问题，能够让程序根据某个表达式的不同取值，执行不同的语句分支。

本节课学习目标：

1. 掌握 `switch` 语句的一般形式。
2. 理解 `case`、`break`、`default` 的作用。
3. 掌握 `switch` 语句的执行流程。
4. 理解 `switch` 语句中的穿透现象。
5. 能够分析 `switch` 嵌套结构中 `break` 的作用范围。
6. 能够使用 `switch` 编写多分支选择程序。

## 二、switch 语句的一般形式

`switch` 语句的一般形式如下：

```c
switch (表达式)
{
    case 常量表达式1:
        语句组1;
        break;

    case 常量表达式2:
        语句组2;
        break;

    ...

    case 常量表达式n:
        语句组n;
        break;

    default:
        语句组;
}
```

执行时，程序先计算 `switch` 后面括号中表达式的值，然后将这个值依次与各个 `case` 后面的常量表达式进行匹配。

如果表达式的值与某个 `case` 后面的常量表达式相同，就从该 `case` 开始执行后面的语句。

如果执行过程中遇到 `break`，就立即跳出整个 `switch` 语句，继续执行 `switch` 后面的下一条语句。

如果所有 `case` 都不匹配，并且程序中写了 `default`，则执行 `default` 后面的语句。`default` 的作用类似于 `if...else` 结构中的 `else`，表示其他情况。

需要注意，`default` 是可选部分，可以根据题目要求决定是否书写。

## 三、switch 语句的使用规则

第一，`switch` 后面表达式的值通常可以是整型、字符型或枚举型。

例如：

```c
switch (x)
```

如果 `x` 是整型，那么 `case` 后面也应该写与它类型匹配的常量值。

第二，每个 `case` 后面必须是常量表达式，不能是变量或不确定的表达式。

正确写法：

```c
case 1:
case 2:
case 100:
```

错误写法：

```c
case n:
case i + 1:
```

因为 `n` 和 `i + 1` 不是固定常量。

第三，各个 `case` 后面的常量表达式必须互不相同，不能出现重复的 `case` 值。

第四，`case` 后面的常量表达式只起语句标号的作用，不进行条件判断。一旦程序找到匹配入口，就会从该入口开始向下执行。

如果后面没有遇到 `break`，程序会继续执行后面的语句，即使后面的 `case` 并不匹配，也会继续执行。这种现象叫做 `switch` 的穿透性。

因此，在大多数多分支选择程序中，每个分支执行结束后都要加 `break`。

## 四、例题讲解

### 例题 1：用 switch 判断成绩等级

题目：

从键盘输入一个百分制成绩，按照下列规则输出等级：

1. 90 分及以上：A
2. 80 到 89 分：B
3. 70 到 79 分：C
4. 60 到 69 分：D
5. 60 分以下：E

分析：

如果直接用成绩作为 `switch` 的表达式，就需要列出 0 到 100 的所有情况，程序会很长。

因此，可以先让成绩除以 10，把成绩转换成等级段：

```c
95 / 10 = 9
85 / 10 = 8
75 / 10 = 7
45 / 10 = 4
```

这样就可以使用 `switch (score / 10)` 来判断成绩等级。

参考程序：

```c
#include <stdio.h>

int main()
{
    int score;
    char grade;

    printf("请输入0~100之间的分数：");
    scanf("%d", &score);

    switch (score / 10)
    {
        case 10:
        case 9:
            grade = 'A';
            break;
        case 8:
            grade = 'B';
            break;
        case 7:
            grade = 'C';
            break;
        case 6:
            grade = 'D';
            break;
        case 5:
        case 4:
        case 3:
        case 2:
        case 1:
        case 0:
            grade = 'E';
            break;
        default:
            printf("分数超出范围\n");
            return 0;
    }

    printf("grade = %c\n", grade);

    return 0;
}
```

如果输入 `75`，则 `75 / 10` 的结果是 `7`，匹配 `case 7`，输出等级 `C`。

如果输入 `85`，则 `85 / 10` 的结果是 `8`，匹配 `case 8`，输出等级 `B`。

如果输入 `145`，则 `145 / 10` 的结果是 `14`，没有任何 `case` 能匹配，执行 `default`，输出“分数超出范围”。

这里还要注意：

```c
case 10:
case 9:
    grade = 'A';
    break;
```

`case 10` 后面没有单独的执行语句，会继续向下执行 `case 9` 后面的语句。因此 100 分和 90 到 99 分可以共用一组处理语句。

### 例题 2：分析没有 break 的 switch 程序

程序：

```c
switch (x)
{
    case 5:
        printf("very good\n");
    case 4:
        printf("good\n");
    case 3:
        printf("pass\n");
    case 2:
        printf("for\n");
    default:
        printf("data error\n");
}
```

如果 `x` 的值为 `3`，程序先找到 `case 3`，输出：

```text
pass
```

但是由于 `case 3` 后面没有 `break`，程序会继续向下执行：

```text
for
data error
```

最终输出结果为：

```text
pass
for
data error
```

原因是：`case` 只是入口标号，不是条件判断。一旦进入某个 `case`，如果后面没有 `break`，程序就会继续向下执行。

如果想让每种情况独立执行，应该写成：

```c
switch (x)
{
    case 5:
        printf("very good\n");
        break;
    case 4:
        printf("good\n");
        break;
    case 3:
        printf("pass\n");
        break;
    case 2:
        printf("for\n");
        break;
    default:
        printf("data error\n");
}
```

此时如果 `x` 等于 `3`，只会输出：

```text
pass
```

然后遇到 `break`，直接跳出整个 `switch`。

### 例题 3：没有 break 时的累加问题

程序：

```c
int i = 6, a = 0;

switch (i % 2)
{
    case 1:
        a += 7;
    case 0:
        a += 4;
    case 2:
    case 3:
        a += 3;
}

printf("a = %d\n", a);
```

分析：

`i = 6`，所以：

```c
i % 2 = 0
```

程序匹配 `case 0`，执行：

```c
a += 4;
```

此时 `a = 4`。

由于 `case 0` 后面没有 `break`，继续向下执行：

```c
a += 3;
```

此时 `a = 7`。

做这类题时要注意：先找到入口，再从入口开始向下执行，直到遇到 `break` 或整个 `switch` 结束。

### 例题 4：switch 语句的嵌套

程序：

```c
switch (x)
{
    case 1:
        switch (y)
        {
            case 0:
                printf("**1\n");
                break;
            case 1:
                printf("**2\n");
                break;
        }
    case 2:
        printf("***3\n");
        break;
}
```

这里外层 `switch` 判断 `x`，内层 `switch` 判断 `y`。

如果 `x = 1`，`y = 0`，执行过程如下：

先进入外层 `case 1`，再进入内层 `switch (y)`。

因为 `y = 0`，所以执行内层 `case 0`，输出：

```text
**1
```

然后遇到内层的 `break`。

需要特别注意：这个 `break` 只跳出当前包含它的那个 `switch`，也就是内层 `switch`，不会跳出外层 `switch`。

如果外层 `case 1` 后面没有自己的 `break`，程序还会继续执行外层 `case 2`，输出：

```text
***3
```

因此，在 `switch` 嵌套结构中，必须分清楚 `break` 属于哪一层 `switch`。

### 例题 5：用 switch 实现四则运算

题目：

输入 `+`、`-`、`*`、`/` 四种运算符，实现两个数的四则运算。

参考程序：

```c
#include <stdio.h>

int main()
{
    int a = 20, b = 10, d;
    char c;

    printf("请输入运算符：");
    c = getchar();

    switch (c)
    {
        case '+':
            d = a + b;
            break;
        case '-':
            d = a - b;
            break;
        case '*':
            d = a * b;
            break;
        case '/':
            d = a / b;
            break;
        default:
            printf("运算符输入错误\n");
            return 0;
    }

    printf("%d %c %d = %d\n", a, c, b, d);

    return 0;
}
```

这里要注意，`c` 是字符型变量，所以 `case` 后面的加、减、乘、除运算符都要用单引号括起来：

```c
case '+':
case '-':
case '*':
case '/':
```

每一种运算完成后都要加 `break`。否则如果输入 `+`，程序会从加法分支开始继续向下穿透，导致后面的运算也被执行。

### 例题 6：输入小于 1000 的正整数并逆序输出

题目：

输入一个小于 1000 的正整数，完成三个任务：

1. 判断它是几位数。
2. 分别输出它的每一位数字。
3. 按逆序输出这个数。

参考程序：

```c
#include <stdio.h>

int main()
{
    int n, num;
    int hundreds, tens, ones;
    int digits = 3;
    int reverse;

    printf("请输入一个小于1000的正整数：");
    scanf("%d", &n);

    num = n;

    hundreds = n / 100;
    tens = n % 100 / 10;
    ones = n % 10;

    if (hundreds == 0)
    {
        digits = 2;
        if (tens == 0)
        {
            digits = 1;
        }
    }

    printf("%d 是 %d 位数\n", num, digits);

    printf("该数的每一位数字分别是：");

    switch (digits)
    {
        case 3:
            printf("%d %d %d\n", hundreds, tens, ones);
            break;
        case 2:
            printf("%d %d\n", tens, ones);
            break;
        case 1:
            printf("%d\n", ones);
            break;
    }

    switch (digits)
    {
        case 3:
            reverse = ones * 100 + tens * 10 + hundreds;
            break;
        case 2:
            reverse = ones * 10 + tens;
            break;
        case 1:
            reverse = ones;
            break;
    }

    printf("逆序数是：%d\n", reverse);

    return 0;
}
```

分析：

以 `65` 为例：

```c
65 / 100 = 0
65 % 100 / 10 = 6
65 % 10 = 5
```

因此 `65` 是两位数，每一位数字分别是 `6` 和 `5`，逆序数是 `56`。

以 `365` 为例：

```c
hundreds = 3
tens = 6
ones = 5
```

逆序数为：

```c
5 * 100 + 6 * 10 + 3 = 563
```

本题用了两次 `switch`。

第一次 `switch` 根据位数决定输出几位数字。

第二次 `switch` 根据位数决定如何组合逆序数。

每个 `case` 后面都要加 `break`，否则会发生穿透，导致输出重复或结果错误。

## 五、易错点

1. 忘记写 `break`。

   `case` 只表示入口，如果没有 `break`，程序会继续向下执行后面的语句。

2. 误以为 `case` 会持续判断。

   `case` 不是条件判断语句。一旦找到匹配入口，后面的 `case` 标签不会再起判断作用。

3. `case` 后面写变量。

   `case` 后面必须是常量表达式，不能写普通变量。

4. 多个 `case` 值重复。

   各个 `case` 后面的常量表达式必须互不相同。

5. 字符常量没有加单引号。

   判断字符型变量时，`case` 后面应写字符常量，例如 `case '+':`。

6. 嵌套 `switch` 中误判 `break` 的作用范围。

   `break` 只跳出当前包含它的 `switch`，不会自动跳出外层 `switch`。

## 六、课堂练习

### 练习 1

题目：

```c
int x = 3;

switch (x)
{
    case 1:
        printf("A");
    case 2:
        printf("B");
    case 3:
        printf("C");
    default:
        printf("D");
}
```

程序输出结果是什么？

答案：

```text
CD
```

解析：

`x = 3`，程序从 `case 3` 进入，输出 `C`。由于 `case 3` 后面没有 `break`，继续执行 `default`，输出 `D`。

### 练习 2

题目：

```c
int x = 2;

switch (x)
{
    case 1:
        printf("A");
        break;
    case 2:
        printf("B");
        break;
    case 3:
        printf("C");
        break;
    default:
        printf("D");
}
```

程序输出结果是什么？

答案：

```text
B
```

解析：

`x = 2`，匹配 `case 2`，输出 `B`，随后遇到 `break`，跳出整个 `switch`。

### 练习 3

题目：

```c
char op = '*';

switch (op)
{
    case '+':
        printf("加法");
        break;
    case '-':
        printf("减法");
        break;
    case '*':
        printf("乘法");
        break;
    case '/':
        printf("除法");
        break;
}
```

程序输出结果是什么？

答案：

```text
乘法
```

解析：

`op` 是字符变量，值为 `'*'`，匹配 `case '*':`，输出“乘法”。

## 七、本讲小结

本节课主要学习了 `switch` 语句。

`switch` 语句适合处理多分支选择问题。程序会先计算 `switch` 后面表达式的值，再与各个 `case` 后面的常量表达式进行匹配。

需要重点掌握以下内容：

1. `switch` 后面的表达式通常可以是整型、字符型或枚举型。
2. `case` 后面必须是常量表达式，并且各个 `case` 的值不能重复。
3. `case` 只起入口标号作用，不持续进行条件判断。
4. `break` 用于跳出当前 `switch` 语句。
5. 如果没有 `break`，程序会发生穿透，继续向下执行。
6. `default` 表示其他情况，可以根据需要选择是否书写。
7. 在 `switch` 嵌套中，`break` 只跳出当前包含它的那个 `switch`。

做 `switch` 相关题目时，要特别关注两个问题：

1. 每个 `case` 后面有没有 `break`。
2. 如果存在 `switch` 嵌套，要看清楚 `break` 属于哪一层 `switch`。

本节课内容到这里结束。
