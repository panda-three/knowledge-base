/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：已知char str[]=" 78+55*3  82*6+25 81*4/36 63-49/7 "中存放
      有四则运算表达式，程序首先将其中的表达式和运算符取出按
      顺序将操作数放入zs数组中，操作符按顺序放在zf数组中。
      然后根据四则运算规则，计算各表达式的值存入zs二维数组中
      的第四列。(仅限2个运算符)

程序运行结果如下：
    78+55*3=243
    82*6+25=517
    81*4/36=9
    63-49/7=56

1. 编写函数int zfcfj(char str[],int zs[][4],char zf[][2])，
   实现将字符串str中的表达式，数字字符转换成整数放入zs，
   运算符放入zf二维数组中，函数返回表达式的个数。 
2. 编写函数void qz(int zs[][4],char zf[][2])，根据zs和zf两个
   二维数组中的值及四则运算规则，调用ys函数，求出表达式的值
   存入zs数组的第四列。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

int ys(int x,char fh,int y)
{
    switch(fh) 
    {
        case '+':return x+y;
        case '-':return x-y;
        case '*':return x*y;
        case '/':return x/y;
    }
}
int zfcfj(char str[],int zs[][4],char zf[][2])
{
/**********Program**********/




        
/**********  End  **********/
} 
void qz(int zs[][4],char zf[][2],int n)
{
/**********Program**********/






/**********  End  **********/
}
int main()
{
    char str[]=" 78+55*3  82*6+25 81*4/36  63-49/7",zf[4][2];
    int zs[4][4],i,j,k;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    k=zfcfj(str,zs,zf);
    qz(zs,zf,k);
    for(i=0;i<4;i++)
    {
    fprintf(fp,"%d.",i+1);
        for(j=0;j<4;j++)
        {
            if(j<2)
            {
                printf("%d%c",zs[i][j],zf[i][j]);
                fprintf(fp,"%d%c",zs[i][j],zf[i][j]);
            }
            else if(j==2)
            {
                printf("%d=",zs[i][j]);
                fprintf(fp,"%d=",zs[i][j]);
            }
            else if(j==3)
            {
                printf("%d\n",zs[i][j]);
                fprintf(fp,"%d\n",zs[i][j]);
            }
       }
    }
    fclose(fp);
    return 0;
}

