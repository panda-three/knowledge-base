/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符串s由若干形如"#2,134"格式的子串组成，首先将s中所有该格式的子串
      转换成整数，存入数组a中，然后将数组a中每个整数转换成九进制数字字符
      串存入二维字符数组nine中。
    
程序运行结果如下：
从串中抽取出的整数有:
2134    -3156   5998    7117    0
它们对应的九进制数字字符串为:
2831    -4286   8204    10677   0

1.编写函数int abstract(char s[],int a[])，按上述规则将字符串s中的子串
  转换成整数，存入数组a中，函数返回整数个数。

2.编写函数void convert(int a[], char nine[][N], int m), 将长度为m的数组a中每个
  整数转换成九进制数字字符串，并存入二维字符数组nine中。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<ctype.h>
#include<math.h>

#define M 50
#define N 50

int abstract(char s[], int a[]) 
{
/**********Program**********/




/**********  End  **********/
}

void convert(int a[], char nine[][N], int m)
{
/**********Program**********/




/**********  End  **********/
}

int main() 
{
    char  s[M]="#2,134#-31,56#5,998#711,7,#0", nine[M][N];
    int  i,n, a[M];
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("File open error\n"), exit(0);
    }   
    n=abstract(s,a);
    printf("从串中抽取出的整数有:\n");
    for(i=0; i<n; i++)
    {
        printf("%d\t",a[i]);
        fprintf(fp,"%o ",a[i]);
    }
    printf("\n");
    convert(a,nine,n);
    printf("它们对应的九进制数字字符串为:\n");
    for(i=0; i<n; i++)
    {
        printf("%s\t",nine[i]);
        fprintf(fp,"%s\\",nine[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;
}