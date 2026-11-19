/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：str是由数字字符和字母字符组成的字符串，程序功能是取出str中的连续数
      字串，如果连续数字串的各位数字之和为奇数，则将其存于数组b中。 
      将数组b视为首尾相连的循环数列，求出数列中相邻两个元素的最大公约数。

程序运行结果如下：
原始字符串为：
BD27HC45S135QA120LN82WPV
数字之和为奇数的连续数字串有：
27      45      135     120
上述数列中相邻两元素的最大公约数分别是:
9       45      15      3
--------------------------------------------------------- 
注意：不得增行或删行，不得更改程序的结构      
-------------------------------------------------------*/  
#include <stdio.h>
#include <ctype.h>

#define N 80

int trans(char str[],int b[])
{
    int i=0,num=0,p,s,x;
    while(str[i])
    {
        if(isdigit(str[i]))
        {
            s=0;
/***********FOUND***********/
            while(str[i])
                s=s*10+str[i++]-'0';
            x=s;
            p=0;
            while(x)
            {
                p=p+x%10;
                x/=10; 
            }
            if(p%2)    
/***********FOUND***********/
                b[i++]=p;
            
        }
        else i++;
    }
    return num;
}
int gcd(int d[],int b[],int num)
{
    int i,x,y,n=0;
    for(i=0;i<num;i++)
    {
        x=b[i];
        y=b[(i+1)%num];
        while(x!=y)
        {
            if(x>y) x=x-y;
            if(y>x) y=y-x;
        }
        d[n++]=x;
    }
    return n;
}

int main(void)
{
    char str[N]="BD27HC45S135QA120LN82WPV";
    int b[N],d[N];
    int i,num,n;
    printf("原始字符串为：\n");
    puts(str);
    num=trans(str,b);
    printf("数字之和为奇数的连续数字串有：\n");
    for(i=0;i<num;i++)
        printf("%d\t",b[i]);
/***********FOUND***********/
    gcd(b,d,num);
    printf("\n上述数列中相邻两元素的最大公约数分别是:\n");
    for(i=0;i<n;i++)
        printf("%d\t",d[i]);
    return 0;
}
