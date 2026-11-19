/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：数组ss中存储了若干字符串，先在每个字符串最前面插入该字符串的长度，
      然后删除ss中长度超过原始字符串长度平均值的字符串。
例如：数组ss原始值为：
     "Manufacturing","History","Trade","Construction","Administrative",
     "Policies","Spotrs","Infrastruct","EconnomyOA","DeliciousFoods"
      处理后结果：
      5Trade
      6Spotrs
      7History
      8Policies

编写函数：
1.函数int insert(char  ss[][M])将数组ss中每个字符串最前面插入该字符串的长度，
  函数返回所有原始字符串的平均长度（平均长度取整）。
2.函数int delstr(char ss[][M],int k)先将数组ss中字符串长度大于k的字符串删除，
  然后将剩余字符串按长度升序排序，函数返回剩余字符串的个数。
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define   N   10
#define   M   80

int insert(char  ss[][M])
{
/**********Program**********/




/**********  End  **********/
}
int delstr(char ss[][M],int k)
{
/**********Program**********/





/**********  End  **********/
}
int main()
{
    FILE *fp;
    char  ss[N][M]={"Manufacturing","History","Trade","Construction","Administrative","Policies","Spotrs","Infrastruct","EconnomyOA","DeliciousFoods"};
    int  i,k,p;
    if((fp=fopen("DATA.dat","w"))==NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    k=insert(ss);
    p=delstr(ss,k);
    printf("处理后结果:\n");
    fprintf(fp,"处理后结果:\n");
    for(i=0; i<p; i++)
    {
        puts(ss[i]);
        fputs(ss[i],fp);
        fprintf(fp,"\n");        
    }
    fclose(fp);
    return 0; 
}
