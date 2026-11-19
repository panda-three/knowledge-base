/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：求字符串s中所有相邻两个字符的ASCII值之和，可将每个和值看作最小进制
      表示的数，然后将该进制数转换为十进制数。最后，从这些十进制数中找出互
      质数对。
      例如：相邻两个字符为'c'和'1'，其ASCII值之和为148,可将该值看作的最
      小进制为9进制数，将该9进制数148转换成十进制数为125，然后，保存
      到数组a中。
      互质数对是指最大公约数为1的一对数。

例如：字符串s为："c1F2k"；
      数组a的值为：125  119  15  111
      互质的数对：
                125 119
                125 111
                119  15
                119 111

编写程序：
1. 编写函数int GenStr(char s[],int a[])，求字符串s中所有相邻两个字符
   的ASCII值之和，将每个和值看作最小进制表示的数，然后将该进制数转换为
   十进制数保存到数组a中。函数返回a中保存的数的个数。

2. 编写函数int Calculate(int a[], int n,int b[][2])， 从a数组的n个
   数中找出互质数对保存到数组b中, 并返回互质数对的个数。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define N 80

int GenStr(char s[],int a[]) 
{
/**********Program**********/




/**********  End  **********/
}

int Calculate(int a[], int n,int b[][2])
{
/**********Program**********/




/**********  End  **********/
}

int main() 
{
    char s[]="c1F2k";
    int a[N]= {0},b[N][2]= {0};
    int num=0,i=0,n;

    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    num=GenStr(s,a);
    printf("The string s is: %s\n",s);
    fprintf(fp,"The string s is: %s\n",s);
    for(i=0; i<num; i++)
        printf("%d  ",a[i]);
    printf("\n");
    n= Calculate(a,num,b);
    for(i=0; i<n; i++) 
    {
        printf("%3d  %3d\n",b[i][0],b[i][1]);
        fprintf(fp,"%3d  %3d\n",b[i][0],b[i][1]);        
    }
    fclose(fp);
    return 0;
}
