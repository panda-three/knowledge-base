// 题目要求从输入的 18 位身份证号码中分别提取性别和出生年份，判断性别并计算年龄（周岁）后输出 。出生年份：身份证号第 $7 \sim 10$ 位 。
// 性别判断：第 17 位数字，奇数表示男性，偶数表示女性 。计算逻辑：以 2019 年为基准计算年龄 。

#include <stdio.h>
#include <string.h>

// 截取子串：从字符串 str1 的第 st 个位置开始截取长度为 len 的子串，结果放到 str2 中
void getstr(char str1[], char str2[], int st, int len) {
    int i, n = 0;
    // 身份证位号对应数组下标需要 -1
    for (i = st - 1; i < st + len - 1; i++) {
        str2[n++] = str1[i];
    }
    str2[n] = '\0'; // 字符串结束符 [cite: 494]
}

// 计算年龄：提取第 7-10 位年份并计算 [cite: 495]
int getage(char str1[]) {
    char year[5];
    int s = 0, i, n;
    getstr(str1, year, 7, 4); // 截取第 7 位开始的 4 个字符 [cite: 500]
    for (i = 0; i < 4; i++) {
        n = year[i] - '0';    // 字符转数字 [cite: 503]
        s = s * 10 + n;       // 累加求年份数值 [cite: 504]
    }
    return 2019 - s;          // 返回周岁 
}

// 判断性别：男返回 1，女返回 0 [cite: 506]
int getsex(char str1[]) {
    char sex[2];
    int sex_n;
    getstr(str1, sex, 17, 1); // 截取第 17 位 [cite: 511]
    sex_n = sex[0] - '0';
    if (sex_n % 2 == 0) 
        return 0;             // 偶数为女 [cite: 513, 516]
    else 
        return 1;             // 奇数为男 [cite: 517]
}

void main() {
    char id_n[19];
    int age;
    printf("Please enter 18 numbers:\n");
    gets(id_n);               // 输入身份证号 [cite: 483]
    
    age = getage(id_n);       // 计算年龄 [cite: 484]
    
    if (getsex(id_n) == 0)    // 判断并输出性别 [cite: 485]
        printf("性别:女");
    else 
        printf("性别:男");
        
    printf("\n年龄: %d\n", age); // 输出年龄 [cite: 488]
}