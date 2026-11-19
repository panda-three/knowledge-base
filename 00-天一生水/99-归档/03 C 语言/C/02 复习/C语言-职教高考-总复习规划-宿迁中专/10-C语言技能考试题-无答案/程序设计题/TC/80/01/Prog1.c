/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：程序根据二维数组n[ROW][COL]行号的奇偶性，找出每行的极值，存入二维数
      组c的第一行。再计算c数组第一行各元素被该行其他元素末尾包含的次数
      （末尾包含的含义举例：4被4314末尾包含,31不被4314末尾包含）。
      程序运行结果如下：
       n数组的初始数据
       4    17    5   10
       3  4314    7    6
      59    60   31   32
      14     6    7    0
       各行极值为
       4  4314   31   14   
       各极值被包含的次数为
       2     0    0    1

1.编写函数void max_min(int n[][COL],c[][COL)，找出二维数组n每行元素的极
  值：偶数行找最小元素值,奇数行找最大元素值,存放数组c的第一行，列号为行
  号的位置处。
2.int contain(int c[],int col)，计算一维数组c的col列元素被c数组其他元素
  (不包括自身)末尾包含的次数。函数返回被包含的次数。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define ROW 4
#define COL 4

void max_min(int n[][COL],int c[][COL])
{
/**********Program**********/




/**********  End  **********/
}
int contain(int c[],int col)
{
/**********Program**********/





/**********  End  **********/
}
int main()
{
    int n[ROW][COL]={{4,17,5,10},{3,4314,7,6},{59,60,31,32},{14,6,7,0}};
    int c[2][COL]={0};
    int i,j;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    printf("n数组的初始数据\n");
    for(i=0;i<ROW;++i)
    {        
        for(j=0;j<COL;++j)
        {
            printf("%5d",n[i][j]);
            fprintf(fp,"%5d",n[i][j]);
        }
        printf("\n");
        fprintf(fp,"\n");
     }
    max_min(n,c);
    printf("各行极值为\n");
    for(j=0;j<COL;++j)
    {        
        printf("%5d",c[0][j]);
        fprintf(fp,"%5d",c[0][j]);
    }
    printf("\n");
    fprintf(fp,"\n");
    printf("各极值被包含的次数为\n");
    for(i=0;i<4;++i)
        c[1][i]=contain(c[0],i);
    for(i=0;i<COL;++i)
    {
        printf("%5d",c[1][i]);
        fprintf(fp,"%5d",c[1][i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;
}


