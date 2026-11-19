/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：小明最近迷上了回文字符串，他有一个只包含小写字母且长度不超过100的
      字符串s，小明可以往字符串s的开头处加入任意数目个指定字符：'l'、'q'
      或'b'。小明想要知道他是否能通过这种方式把字符串s转化为一个回文字符串。

例1：若s="asalqb", 则小明可以在s的开头处加入'b'、'q'和'l'将字符串转换为
     回文字符串。程序运行结果为Yes。

例2：若s="qasalqb", 则小明无法在s的开头处加入'b'、'q'或'l'将字符串转换为
     回文字符串。程序运行结果为No。

-----------------------------------------------------------------------
注意：不得增行或删行，不得更改程序的结构
----------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isPalindrome(char str[], int start, int end) 
{
    while(start<end)
    {
        if (str[start] != str[end]) 
        {
            return 0;
        }
        ++start, --end;
    }
    return 1;
}

int change(char s[])
{ 
    int i, len = strlen(s);    
    int idx_font=0, idx_back=0;        
    if(isPalindrome(s,0,len-1))
    {
        return 1;
    }    
    for(i=0; i<len; i++) 
    {
        if(s[i]!='l' && s[i]!='q' && s[i]!='b')
        {
            idx_font = i;
            break;
        }
    }        
    for(i=len-1; i>= 0; i--)
    {
        if(s[i]!='l' && s[i]!='q' && s[i]!='b')
        {
            idx_back=i;
            break;
        }
    } 
/***********FOUND***********/
    if(idx_font == idx_back)
    {  
        return 1;
    }
/***********FOUND***********/
    if(idx_font > len-idx_back) 
    {  
        return 0;
    }
/***********FOUND***********/
    return isPalindrome(s,idx_font,idx_back+idx_font);  
}

int main(void) 
{
    int num, i;
    char s[200];
    scanf("\n%s",s);
    if(change(s)) 
    {
        printf("Yes\n");
    } else 
    {
        printf("No\n");
    }
    return 0;
}