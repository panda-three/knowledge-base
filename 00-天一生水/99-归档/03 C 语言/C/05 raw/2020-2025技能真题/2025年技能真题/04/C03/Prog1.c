/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：为每个字符设定一个“能量值”，能量值的设定规则为：小写字母a到z的能量值
      分别为26到1；大写字母A到Z的能量值分别为52到27；空格字符的能量值
      为-1；其他字符的能量值为0。
      设二维字符数组sen中存放了若干字符串，编写程序，计算sen中每个字符串的
      总能量值，存入数组energy，并按照各字符串的总能量值按升序将所有字符串排序，
      输出排序后的字符串及其对应的总能量值。

程序运行结果示例：
原始字符串及能量值：
Hello World      =>197
C Programming    =>241
I Love coding    =>232
Python is fun!   =>154
Good Morning     =>217
 
排序后的字符串及能量值：
Python is fun!   =>154
Hello World      =>197
Good Morning     =>217
I Love coding    =>232
C Programming    =>241

1.编写函数 int calculate_energy(char sen[])，计算字符串 sen 的总能量值，
  并作为函数的返回值。

2.编写函数 void sort(char sen[][100], int energy[], int n)，根据字符数组
  sen中n个字符串的能量值energy，按升序将sen数组的字符串排序。
-----------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
---------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define N 5

int calculate_energy(char sen[]) 
{
/**********Program**********/




/**********  End  **********/
}

void sort(char sen[][100], int energy[], int n) 
{
/**********Program**********/




/**********  End  **********/
}

int main() 
{
    char sen[N][100] = {"Hello World",
                        "C Programming",
                        "I Love coding",
                        "Python is fun!",
                        "Good Morning"};
    int energy[N], i;
    FILE *fp;
    if ((fp = fopen("DATA.dat", "w")) == NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    for (i = 0; i < N; i++)
        energy[i] = calculate_energy(sen[i]);

    printf("原始字符串及能量值：\n");
    for (i = 0; i < N; i++)
        printf("%s\t=>%d\n", sen[i], energy[i]);

    sort(sen, energy, N);

    printf("\n排序后的字符串及能量值：\n");
    for (i = 0; i < N; i++) 
    {
        printf("%s\t=>%d\n", sen[i], energy[i]);
        fprintf(fp, "%s->%d\n", sen[i], energy[i]);
    }
    fclose(fp);
    return 0;
}