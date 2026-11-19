/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：按照从大到小的顺序对数组p中的数据进行排名，结果存入rule数组。
      主函数中的各行字符串根据rule数组中对应的值进行循环左、右移动。
   
程序运行结果如下：
数值:  85  95  60  60  50
排名:   2   1   3   3   5
移动前:  SUJIANG   NIVERSITYU  FO  HNOLOGYTEC
移动后:  JIANGSU   UNIVERSITY  OF  TECHNOLOGY

编写函数
1.编写函数void sort(int p[],int n,int rule[])按照从大到小的顺序对数组p中的
  n个数据进行排名，结果存入rule数组中（相同数值名次相同）。 

2.编写函数void move(char mm[][COL],int rule[])，将二维数组mm中各行字符串
  循环左、右移动，行下标为偶数循环左移，行下标为奇数循环右移，移动位数为
  数组rule中的数值。数值超过字符串长度则按求余字符串长度结果移动。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#define ROW 4
#define COL 20
#define N 5
void sort(int p[],int n,int rule[])
{
/**********Program**********/





/**********  End  **********/
}
void move(char mm[][COL],int rule[])
{
/**********Program**********/






/**********  End  **********/
}
int main()
{
    int rule[N]={0};
    int p[N]={85,95,60,60,50};
    int i,j;
    char mm[ROW][COL]={"SUJIANG","NIVERSITYU","FO","HNOLOGYTEC"};
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    sort(p,N,rule);
    printf("数值:");
    for(i=0;i<N;i++)
        printf("%4d",p[i]);
    printf("\n排名:");
    for(i=0;i<N;i++)
        printf("%4d",rule[i]);
    printf("\n移动前:");
    fputs("移动前:",fp);
    for(i=0;i<ROW;i++)
    {
        printf("  %s  ",mm[i]);
        fprintf(fp,"%s,",mm[i]);
    }
    move(mm,rule);
    printf("\n移动后:");
    fputs("移动后:\n",fp);
    for(i=0;i<ROW;i++)
    {
        printf("  %s  ",mm[i]);
        fprintf(fp,"%s,",mm[i]);
    }
    fclose(fp);
    return 0;
}

