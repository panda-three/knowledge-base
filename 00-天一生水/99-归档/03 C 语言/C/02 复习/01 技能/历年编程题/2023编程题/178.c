/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：二维字符型数组str[N][20]中存放了N个全部由小写字母组成的字符串。程序计算
      每个字符串的最大字符间距，并依据每个字符串的最大字符间距对字符串进行排序。
      所谓字符串的最大字符间距，指一个字符串中最大字母与最小字母的ASCII码的差。
例如，字符串"warning"的最大字符间距是'w'-'a'。

程序运行结果如下：
22  13  20  14  16
22    warning
20    undeclared
16    identifier
14    printf
13    error

1.编写函数void max_dis(char str[][20],int dis[])，对str中N个字符串，计算每个
  字符串的最大字符串间距，保存在一维数组dis中。
2.编写函数void sort(char str[][20],int dis[])，依据一维数组dis中保存的最大
  字符间距，对str中的N个字符串进行降序排序。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define N 5
void max_dis(char str[][20],int dis[])
{
/**********Program**********/




/**********  End  **********/
}
void sort(char str[][20],int dis[])
{
/**********Program**********/
    



/**********  End  **********/
}

int main()
{
    char str[N][20]={"warning","error","undeclared","printf","identifier"};
    int dis[N],i;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    max_dis(str,dis);
    for(i=0;i<N;++i)
    {
        printf("%d ",dis[i]);
        fprintf(fp,"%d,",dis[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    sort(str,dis);
    for(i=0;i<N;++i)
    {
        printf("%d\t%s\n",dis[i],str[i]);
        fprintf(fp,"%s\t%d\n",str[i],dis[i]);
    }
    fclose(fp);
    return 0;
}

