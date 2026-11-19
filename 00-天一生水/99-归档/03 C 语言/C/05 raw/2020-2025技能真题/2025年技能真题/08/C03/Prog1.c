/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：二维字符数组 str[M][N]中存在 M 行字符串，每行字符串中存在多个降序
      子串，找出每行的最长降序子串存入二维数组b，并对数组b中的字符串
      按大小升序排序。 
 
"降序子串"指该串中字符 ASCII 码值依次递减 1。如：字符串"edadg543rsigfea" 
 中可找出的降序子串为："ed"、" 543 "、"gfe",只放入字串"gfe" 

程序运行结果如下：
每行字符串中最长的降序子串为:
srqp
edcba
gfe
76543

子串升序排序后:
76543
edcba
gfe
srqp

1.函数void trans(char str[],char a[])的功能是：将一维字符数组str中的最长 
降序子串找出，并放入数组a,若一行字符串中最长降序子串存在多个，只放入最后一个。

2.函数 void sort(char b[][N])中实现二维数组b中字符串升序排序。
------------------------------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
------------------------------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define M 4
#define N 50

void trans(char str[],char a[])
{ 
/**********Program**********/




/**********  End  **********/

}
void sort(char b[][N])
{
/**********Program**********/




/**********  End  **********/

}

int main(void)
{ 
    char str[M][N]={"hi432srqpa98wa","7azyxr3wedcbaaa","edadg543rsigfea","exit76543efgh"};
    char a[N],b[M][N];
    int i;
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL)
    {
        printf("File open error\n"), exit(0);
    }   
    for(i=0;i<M;i++)
    { 
        trans(str[i],a);
        strcpy(b[i],a);
    }
    printf("每行字符串中最长的降序子串为:\n");
    for(i=0;i<M;i++) 
    {        
        puts(b[i]);
        fprintf(fp,"[%s|\n",b[i]);
    }
    printf("\n\n子串升序排序后:\n");
    sort(b);
    for(i=0;i<M;i++) 
    {
        puts(b[i]);
        fprintf(fp,"%s|\n",b[i]);
    }
    fclose(fp);
    return 0;
} 