/*----------------------------------------------------------------------
【程序填空】
------------------------------------------------------------------------
题目：如果字符串s可以通过循环左移或循环右移若干次字符串t获得，则输出True，
      否则输出False。

例如：若s="abcdef"，t="cdefab"时，则可以通过循环左移或循环右移若干次t得到s。
      若t="cdefba"时，则不可以通过循环左移或循环右移t若干次得到s。

本程序采用非循环左移或非循环右移方法判断是否可以由t得到s。

程序运行结果如下：
abcde  abced   False
abcde  deabc   True
abcde  aacde   False
abcde  cdeab   True
abcde  abcdee  False
----------------------------------------------------------------------
注意：在填空标志处填写答案，并删除填空标志，勿改动程序中的其他部分。
--------------------------------------------------------------------*/
#include <stdio.h>
#include <string.h>

int check(char s[],char t[])
{
    int i,flg,pos;
    char tmp[100]="";
    strcpy(tmp,t);
/**************************SPACE******************************/
    【?】;
    if(2*strlen(s)!=strlen(tmp))
        return 0; 
    i=flg=0;
    while(tmp[i]&&flg==0)
    {
        pos=0;         
/**************************SPACE******************************/
        while(【?】) 
            pos++;
        if(s[pos]=='\0') 
            flg=1; 
        i++;              
    }
    return flg;
}

int main(void)
{
    char s[5][10]={"abced","deabc","aacde","cdeab","abcdee"};
    char t[]="abcde";
    int i;
    for(i=0;i<5; ++i)
    {
        printf("%s\t ",t);
        if(check(s[i],t))
            printf("%s\t\tTrue\n",s[i]);
        else
            printf("%s\t\tFalse\n",s[i]);
    }
    return 0;
}