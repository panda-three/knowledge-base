/*----------------------------------------------------------------------
【程序填空】
------------------------------------------------------------------------
题目：已知字符串subStr为str的子串，在母串str中找出subStr，在其前面插入一
      个'@'字符,需保持子串内容完整性。
例如：在"Goqqqq;Comeqqq.com"中找到"qq"后，将字符串改变为：
     "Go@qq@qq;Come@qqq.com"

------------------------------------------------------------------------
注意：除要求填空的位置之外，请勿改动程序中的其他部分。
----------------------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

void changeStr(char str[],char subStr[])
{
    int i=0,j,k,pop,len,lenSub;
    len=strlen(str);
    lenSub=strlen(subStr);
    while(str[i]!=0)
    {
        j=0;
        k=i;
/******************SPACE******************/
        while(【?】&&subStr[j]!=0)
        {
            k++;
            j++;
            if(subStr[j]=='\0')
            {
                for(pop=len;pop>i;pop--)
                {                                        
                    str[pop]=str[pop-1];                                        
                }                        
                str[pop]='@';
/******************SPACE******************/
                【?】;
                len++;              
            }         
        }
        i++;
    }
}
int main()
{
    char str[100]="Goqqqq;Comeqqq.com", subStr[10]="qq";
    changeStr(str,subStr);
    puts(str);
    return 0;
}
