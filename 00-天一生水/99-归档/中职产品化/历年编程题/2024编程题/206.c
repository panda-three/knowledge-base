/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：从给定的字符串中依次取出前k个数字字符组成一个整数(不考虑正负号)，
      并判断该整数是否为幻方数，如果是则输出yes，否则输出no。
      幻方数是指：整数至少由三位数字组成，且整数的最高位+最低位数字之和
      等于次高位+次低位数字之和，依次类推，如果整数是奇数位数，
      则中间数的2倍等于最高位+最低位数字之和。

例如：8536974：8+4等于5+7等于3+9等于6*2，因此8536974是幻方数。
      14285：1+5不等于4+8，因此14285不是幻方数。

程序运行结果如下：
字符串为：Fei5-6abo45%6,$458@x
k=4,the number     5645 is yes
k=5,the number    56456 is no
k=6,the number   564564 is no
k=7,the number  5645645 is yes
k=8,the number 56456458 is no
k=9,the number 56456458 is no

1、编写函数int take(char a[],int k)，功能是从a字符串中取出前k个数字字符，
   转换为一个正整数并返回。如果字符串中不足k个数字则最多取k数字组成整数返回。
2、编写函数int check(int n)判断多位整数n是不是幻方数，如果是幻方数函数
   返回1，否则返回0。
--------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int take(char a[],int k)
{  
/**********Program**********/
    int i;
    int s=0;
    int j=0;
    for(i=0;a[i];i++){
    	if(isdigit(a[i])){
    		s=s*10+a[i]-'0';
    		j++;
		}
		if(j==k){
			break;
		}
	}
    return s;
/**********  End  **********/  
}
int check(int n)
{  
/**********Program**********/
    int temp=n;
    int a[10]={0};
    int k=0;
    while(temp){
    	a[k++]=temp%10;
    	temp=temp/10;
	}
     int i=0,j=k-1;
     int flag=1;
     while(i<j){
     	 if( (a[i]+a[j]) != (a[i+1]+a[j-1]) ){
     	 	 flag=0;
     	 	 break;
		 }
		 i++;
		 j--;
	 }
     return flag;
/**********  End  **********/  
}
int main(void)
{ 
    FILE *fp ;
    int k,n; 
    char a[50]={"Fei5-6abo45%6,$458@x"};
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    printf("字符串为：%s\n", a) ; 
    for(k=4;k<10;k++)
    {
        printf("k=%d,",k); 
        n=take(a,k);
        printf("the number %9d is %s\n", n, check(n)?"yes": "no") ;
        fprintf(fp,"%d%s\n", n, check(n)?"yes": "no") ;
    }
    fclose(fp);
    return 0;
}
