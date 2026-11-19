/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------

题目：程序将字符串开始和末尾的连续空格删除，同时将字符串中间的多个空格
      删减只剩1个空格。
      程序运行结果为：
      "   hello    how are  you    "
      "hello how are you"

------------------------------------------------------------------------
注意：不得增行或删行，也不得更改程序的结构。
----------------------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

void getnewstr(char a[])
{
    int isbegin,front,back;
    isbegin=1; 
    front=0;
/***********FOUND***********/
    back=1;
    for( ; a[back]!= '\0'; )
    {
        if (a[back]!=' ')
        {
            isbegin=0;
            a[front++]=a[back++];
        }
        else
        {
/***********FOUND***********/
            if(isbegin==1)
                a[front++]=a[back++];
            while(a[back]==' ')
                ++back;
        }
    }
/***********FOUND***********/
    if(a[front]==' ')
        --front;
    a[front]='\0';
}
int main()
{
    char a[] = "   hello    how      are you    ";
    printf("\"%s\"\n",a);
    getnewstr(a);
    printf("\"%s\"\n",a);
    return 0;
}
