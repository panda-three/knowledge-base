/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：删除给定字符串中的所有非字母字符，并将串中的大写字母转换为小写，再
      判断处理后的字符串是否为回文，若为回文，则统计每个字母出现的次数。

1.函数int process(char s[])对字符串s进行处理，先删除串中的所有非字母字符，
  并将串中的大写字母转换为小写；然后判断处理后的字符串是否为回文，若为
  回文，则返回1，否则返回0；

2.函数int count_chars(char s[],int a[][2])统计字符串s中每个字母的出现次数，
  将统计结果记录在二维数组a中，其中，字母及其出现的次数分别存放在a[i][0]
  和a[i][1]中。函数返回s中不同字母的个数。

程序运行结果如下：
初始数据: A man, 2 plan a 0 canal: P56nama
处理后：amanplanacanalpnama
是回文。a出现8次，c出现1次，l出现2次，m出现2次，n出现4次，p出现2次。

-----------------------------------------------------------------------
注意：不得增行或删行，不得更改程序的结构
----------------------------------------------------------------------*/
#include <stdio.h>
#include <ctype.h>

#define N 26

int  process(char s[])
{
    int i , k = 0 , f , r ;
    for( i = 0; s[i]; i++ ) 
        if (isalpha(s[i])) 
            s[k++] = tolower(s[i]);
    s[k] = '\0';     
    f=0,r=k-1;
    while(f < r)
/***********FOUND***********/
        if(s[f]==s[r])         
           return 0;
    return 1;      
}

int count_chars(char s[],int a[][2]) 
{
    int i , k = 0 , cnt[26] = {0};
    for ( i = 0; s[i]; i++)
/***********FOUND***********/
        cnt[i]++;              
    for ( i = 0; i < 26; i++)
        if (cnt[i])
        {
            a[k][0] = 'a' + i;
            a[k++][1] = cnt[i];
        }
    return k;  
}

int main(void)
{
    char s[ ]="A man, 2 plan a 0 canal: P56nama";
    int i , n , a[N][2];   
    printf("初始数据: "); 
    puts(s);
    n=process(s);
    printf("处理后：%s\n", s);   
    if (n) 
    {
        printf("是回文。");
/***********FOUND***********/               
        count_chars(a,s);         
        for( i = 0 ; i < n-1 ; i ++ )
            printf("%c出现%d次，", a[i][0],a[i][1]);
        printf("%c出现%d次。", a[n-1][0],a[n-1][1]);    
    }
    else
        printf("不是回文！");
    printf("\n");   
    return 0;
}