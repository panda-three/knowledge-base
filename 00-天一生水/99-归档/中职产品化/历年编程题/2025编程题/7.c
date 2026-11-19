/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：已知m的范围 m>=2000,m<10000,在此范围内寻找满足以下条件的最小整数m的值：    
      m的各位数字之和分别等于其十六进制数和十二进制数的各位数字之和；若找到
      这样的m，则求2000年1月1日之后第m天的日期，若未找到这样的m，则输出
      “没有找到满足条件的整数”。 

例如：整数2992的各位数字之和为2+9+9+2=22，其十六进制数0xBB0之和为11+11+0=22， 
      十二进制数1894之和为1+8+9+4=22， 所以2992是满足条件的m的值。
      那么2000年1月1日之后第2992天的日期是2008年3月11日。 

程序运行结果如下：
满足条件的最小整数是2992
2000年1月1日之后第2992天的日期是2008年03月11日

1.编写函数int isEqual(int num)，判断num是否满足题目所要求的条件，满足，
  则函数返回1，否则返回0。

2.编写函数void calculateDate(int m,int date[]) ，计算从日期2000年1月1日之后第
  m天的日期，其年、月、日依次保存在date中，即date[0]存放年，date[1]存放月，
  date[2]存放日。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int Month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int isEqual(int num) 
{
/**********Program**********/
  //1.10、12、16进制的各位和 
    int s10=0;
    int temp1=num;
    while(temp1){
    	int wei=temp1%10;
    	s10=s10+wei;
    	temp1=temp1/10;
	}
	
	int s12=0;
	int temp2=num;
	while(temp2){
		int wei=temp2%12;
		s12=s12+wei;
		temp2=temp2/12;
	} 
	
    int s16=0;
	int temp3=num;
	while(temp3){
		int wei=temp3%16;
		s16=s16+wei;
		temp3=temp3/16;
	} 

    if(s10==s12&&s10==s16)
       return 1;
    else
       return 0;
   
/**********  End  **********/
}

void calculateDate(int m,int date[]) 
{
/**********Program**********/
  //思路：m总天数 加m天 day>30 month++ month>12 year++;       
  int year=2000;
  int month=1;
  int day=1;
  int i;
  for(i=0;i<m;i++){
  	  day++;
  	  int days=Month[month];
  	  if(month==2){
  	  	 if( (year%400==0) || (year%4==0&&year%100!=0) ){
  	  	 	days=days+1;
		 }
	  }
  	  if(day>days){
  	  	 month++;
  	  	 day=1;
	  }
	  if(month>12){
	  	 year++;
	  	 month=1;
	  }
  } 
date[0]=year;
date[1]=month;
date[2]=day;
/**********  End  **********/
}

int main() 
{
    int n=2000, m;
    int date[3];
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("File open error\n"), exit(0);
    }
    for (m = n; m < 10000; m++) 
    {
        if (isEqual(m)) break;
    }
    if(m<10000) 
    {
        printf("满足条件的最小整数是%d\n", m);
        calculateDate(m,date);
        printf("2000年1月1日之后第%d天的日期是",m);
        fprintf(fp,"2000/01/01之后第[%d]天的日期是：",m);
        printf("%4d年%02d月%02d日\n", date[0],date[1], date[2]);
        fprintf(fp,"%02d/%02d/%4d\n", date[2],date[1], date[0]);
    } 
    else 
    {
        printf("没有找到满足条件的整数\n");
    }
    fclose(fp);
    return 0;
}
