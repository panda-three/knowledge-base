/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符串str中包含若干个由空格隔开的仅包含大小写字母的英文单词，计算
      每个单词中所有字母 ASCII 码值的和，找出这些"和值"中的素数，并将与
      素数“和值”对应的所有单词按照其“和值”升序排序，当单词的“和值”
      相同时，按照单词的字典序排序。最后输出排序后的单词。
      
程序运行结果如下：
初始数据: I used that size prime spank of bread to make a delicious sandwich

有8个符合条件的单词:
I
used
that
size
prime
spank
to
a

排序结果:
I->73
a->97
to->227
that->433
used->433
size->443
prime->541
spank->541
    
1.编写函数int wordsearch( char str[], char words[][N],int sum[]),从字符串
  str中提取符合条件的单词并计算其各字母的ASCII码值之和，若该值是素数则将该
  单词及其和值分别保存在数组words和sum中，函数返回符合条件的单词个数。

2.编写函数void sort(char words[][N],int n,int sum[])，二维数组words每行保
  存的是一个单词，共n个单词。数组sum保存了对应单词中各字母的 ASCII 码值之和。
  对words中保存的单词按照数组sum的值从小到大排序，如果值相同，则按照单词的
  字典序排序。在排序过程中，始终保持数组words与数组sum间的对应关系。 
-----------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
---------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define M 10
#define N 20

int wordsearch(char str[], char words[][N],int sum[]) 
{
/**********Program**********/




/**********  End  **********/
}

void sort(char words[][N],int n,int sum[]) 
{
/**********Program**********/




/**********  End  **********/
}

int main(void) 
{
    char str[]="I used that size prime spank of bread to make a delicious sandwich";
    char words[M][N];
    int i,n,sum[M];
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("File open error\n"), exit(0);
    }
    printf("初始数据: ");
    puts(str);
    n=wordsearch( str , words, sum);
    printf("\n有%d个符合条件的单词: \n",n);
    fprintf(fp,"有%d个符合条件的单词:\n",n);
    for( i = 0 ; i < n ; i ++ ) 
    {
        printf("%s\n",words[i]);
        fprintf(fp,"%s\n",words[i]);
    }
    sort(words,n,sum);
    printf("\n排序结果:\n");
    fprintf(fp,"\n排序结果:\n");
    for( i = 0 ; i < n ; i ++ ) 
    {
        printf("%s->%d\n",words[i],sum[i]);
        fprintf(fp,"%s\n",words[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;
}