/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：在写日期时，人们往往会用不同的格式书写，有使用年/月/日的，有使用
      月/日/年的，有使用日/月/年的。在写年份时，也往往省略前两位，这使
      得一个日期，存在多种解读，比如 02/03/04，可能是指2002年03月04日、
      2004年02月03日或2004年03月02日。已知日期的范围在1960年1月1日至
      2059年12月31日之间。
      当输入一个日期时，判断这个日期可能指的日期有哪些。

   输入的日期格式是 "AA/BB/CC" (0≤A,B,C≤9)，输出若干个不相同的日期，每个
   日期占一行，格式是 "yyyy-MM-dd"。多个日期按从早到晚排列。
   
例如：输入：02/03/04
      输出
      2002-03-04
      2004-02-03
      2004-03-02

-----------------------------------------------------------------------
注意：不得增行或删行，不得更改程序的结构
----------------------------------------------------------------------*/
#include <stdio.h>
#include <string.h>

int month[13]= {0,31,28,31,30,31,30,31,31,30,31,30,31};

int check(int y,int m, int d) 
{
    if(m<1 || m>12)
        return 0;    
    month[2]=28+((y%4==0 && y%100)||(y%400==0));
/***********FOUND***********/
    if(d<0 || d>month[m]) 
        return 0;
    return 1;
}

int insert(char buf[][12], int jsq)
{
    int i;
    char date[12];
    for (i = 0; i < jsq; i++)
        if (!strcmp(buf[i], buf[jsq])) return 0;
    strcpy(date,buf[jsq]);
    for (i = jsq; i>0; --i)
/***********FOUND***********/
        if (strcmp(buf[i], date) > 0)
            strcpy(buf[i],buf[i-1]);
        else break;
    strcpy(buf[i],date);
    return 1;
}

int main(void) 
{
    int a,b,c,i;
    int y,jsq=0;
    char buf[3][12];
    printf("请按指定格式输入日期[XX/XX/XX]\n");
    scanf("%2d/%2d/%2d",&a,&b,&c);   
/***********FOUND***********/
    y=(a<60)?2000:1900;    
    if(check(y,b,c)) 
    {
        /* 发送格式化输出到 buf 所指向的字符串 */
        sprintf(buf[jsq], "%4d-%02d-%02d",y,b,c);
        jsq++;
    }    
    y = 1900 + c;
    if(c<60) y += 100;     
    if(check(y,a,b)) 
    { 
        sprintf(buf[jsq], "%4d-%02d-%02d",y,a,b);       
        jsq += insert(buf, jsq);
    }
    if(check(y,b,a))
    {  
        sprintf(buf[jsq], "%4d-%02d-%02d",y,b,a);      
        jsq +=insert(buf, jsq);
    }
    for(i=0; i<jsq; ++i)
    {
        printf("%s\n",buf[i]);
    }
    if(jsq==0) printf("输入的日期非法。\n");
    return 0;
}