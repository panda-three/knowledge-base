/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：提取出字符串a中连续的十进制数字字符（含前面的负号）转换为整数存入到
      整型数组b中，并按要求排序。

程序运行结果如下：
初始数据: "-11a0bD22Fcd34,l33k9F6jk.@s-88dD9&kj-54k%11SD-57n--S"
数据个数: n=12 
 -11   0  22  34   33  9   6  -88  9 -54  11 -57 
排序结果: 
 -11   0  22 -88   6   9  33  34   9 -54  11 -57

1.编写函数int count(char a[],int b[]),提取一维字符数组a中连续的十进制数字字符
  转换为整数（含前面的负号），保存在一维数组b中。函数返回b数组中元素的个数。
2.编写函数void sort(int n,int b[]),找出数组b中最大元素的下标x,最小元素的下标y，
  将数组b中下标x和下标y之间的元素按升序排列。b数组中有n个元素。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#define N 100

int count(char a[],int b[])
{
/**********Program**********/







/**********  End  **********/
}
void sort(int n,int b[])
{
/**********Program**********/







/**********  End  **********/
}

int main(void)
{
    char a[N]={"-11a0bD22Fcd34,l33k9F6jk.@s-88dD9&kj-54k%11SD-57n--S"};
    int b[N];
    int i,n;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    printf("初始数据: %s",a); 
    printf("\n");
    n=count(a,b);
    printf("数据个数: n=%d\n",n); 
    for(i=0;i<n;i++)
        printf("%4d",b[i]);
    printf("\n");
    sort(n,b);
    printf("排序结果: "); 
    printf("\n");
    for(i=0;i<n;i++)
    {
        printf("%4d",b[i]);
        fprintf(fp,"%4d,",b[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;
}

