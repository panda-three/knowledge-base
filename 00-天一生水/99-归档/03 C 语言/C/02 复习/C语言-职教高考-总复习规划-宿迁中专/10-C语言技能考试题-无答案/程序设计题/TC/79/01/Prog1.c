/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符串s中包含若干个回文字符子串，找出其中所有长度大于2的回文字符串，
      然后按其长度的降序存放在字符串数组str中，若某个回文字符串已在该数组
      中，则丢弃。

例如：字符串s为："ILoLoL.jiangsu151uhj"；
      其中，回文子串有："LoLoL", "LoL", "oLo", "LoL", "u151u","151"
      在str中存储的字符串为：
      LoLoL
      u151u
      LoL
      oLo
      151

编写程序：
1. 编写函数int GenStr(int start, char s[], char str[][N])，从串s的start
   下标至最后一个字符之间查找回文字符串，若找到则保存到字符串数组str中。
   函数返回找到的回文字符串的个数。

2. 编写函数void InsertStr(char str[][N], char step[][N], int n)，将step[]中
   的n个字符串按其长度的降序插入到字符串数组str中，如果插入的字符串在str中有
   ，则不插入。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

#define  N  255
#define  M  100

int GenStr(int start, char s[], char str[][N]) 
{
/**********Program**********/




/**********  End  **********/
}

void InsertStr(char str[][N], char step[][N], int n) 
{
/**********Program**********/




/**********  End  **********/
}

int main() 
{
    FILE  *fp;
    int  i, n;
    char  s[N]="ILoLoL.jiangsu151uhj";
    char  str[M][N]= {"\0"}, step[M][N];
    fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("Write File Error");
        exit(0);
    }
    for (i=0; i<strlen(s)-2; i++) 
    {
        n=GenStr(i,s,step);
        InsertStr(str,step,n);
    }
    printf("长度大于2的回文字符串有：\n");
    for(i=0; str[i][0]; i++) 
    {
        puts(str[i]);
        fputs(str[i],fp);
    }
    fclose(fp);
    return 0;
}

