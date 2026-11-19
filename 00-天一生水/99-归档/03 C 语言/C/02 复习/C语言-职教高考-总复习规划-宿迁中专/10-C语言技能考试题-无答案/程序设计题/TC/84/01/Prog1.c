/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：按条件将数组a中的若干字符存到数组b中，然后将数组b中的数字字符按规律存
      入二维数组ss的左上角三角形区域中。
例如：数组a数据为："#b1C#21H&tC3&2arI44*%nN2wAm$3CA"，则：
      数组b结果为：
      1234CHINA
      数组ss结果为：
      4321     
      321      
      21       
      1

编写函数：
1.函数int conver(char a[],char b[])将数组a中的数字字符和大写字母按顺序取出存
  入数组b中，数字字符在左边，大写字母在右边，且数组b中不能有重复的字符，函数
  返回数组b中数字字符的个数。
2.函数void insert(char b[],char ss[][N])将数组b中的数字字符从后向前取出，沿
  二维数组ss副对角线方向依次存入ss左上角三角形区域中。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define N 80

int conver(char a[],char b[])
{        
/**********Program**********/




/**********  End  **********/
}
void insert(char b[],char ss[][N])
{
/**********Program**********/




/**********  End  **********/
}
int main()
{
    FILE *fp;
    char a[]="#b1C#21H&tC3&2arI44*%nN2wAm$3CA";
    char b[N],ss[N][N]={0};
    int i,j,n;
    if((fp=fopen("DATA.dat","w"))==NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    n=conver(a,b);
    printf("数组b结果为：\n");
    fprintf(fp,"数组b结果为：\n");
    puts(b);
    fputs(b,fp);
    insert(b,ss);
    printf("数组ss结果为：\n");
    fprintf(fp,"\n数组ss结果为：\n");
    for(i=0;i<n;i++)
    {
        puts(ss[i]);
        fputs(ss[i],fp);
        fputs("\n",fp);
    }
    fclose(fp);
    return 0;
}
