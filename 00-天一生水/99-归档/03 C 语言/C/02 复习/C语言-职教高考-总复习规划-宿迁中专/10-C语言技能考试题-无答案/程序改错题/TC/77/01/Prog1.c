/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------

题目：用一个8位正整数表示日期，其中前4位表示年，中间2位表示月，最后2位表示日。
例如：20170901表示2017年9月1日
      20200510表示2020年5月10日
      程序计算两个日期之间的天数。 
      程序运行结果为：
      20170901-20200510共有983天

------------------------------------------------------------------------
注意：不得增行或删行，也不得更改程序的结构。
----------------------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

int valid_date(int date)
{
    int year,month,day;
    int mon[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    year=date/10000;
    month=date/100%100;
    day=date%100;
    if(month>12)
        return 2;
/***********FOUND***********/
    mon[1]=(year%4==0 && year%100!=0 && year%400==0);
/***********FOUND***********/
    return day>=mon[month];
}

int main()
{
    int first=20170901,last=20200510,date;
    int year,month,day,val,days;
    for(days=0,date=first;date<=last; )
    {        
        year=date/10000;
        month=date/100%100;
        day=date%100;
        val=valid_date(date);
        if(val==0)
        {
            ++days;
            ++date;
        }
        else if(val==1)
            date=year*10000+(month+1)*100+1;
        else if(val==2)
/***********FOUND***********/
            date=year*10000+101;
    }
    printf("%u-%u共有%d天\n",first,last,days);
    return 0;
}
