/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：将字符串str中负整数字符串转换为正整数保存到一维数组中，然后将该
      数组中符合以下条件的整数m及整数2^m -1，保存到二维数组中。
      条件是：
              1. 2^m -1是素数；
              2. 2^m -1的逆序数是奇数；
              3. 2^m -1的十进制表示中包含数字1。
      注意，题中的2^m表示2的m次方。 

测试数据：  
"&&B3yh-5AS-12HJ*@#35+eH-7pTR-15HY-17"

程序运行结果如下：         
5    12    7   15   17
5                   31
7                  127
17              131071

1.编写函数int abstract(char str[],int b[])，将字符串str中负整数字符串转换 
  为正整数保存在数组b中，函数返回b中元素个数。

2.编写函数int prime_m(int k,int b[],int x[][2])，将b数组中符合上述条件的
  所有整数m和2^m -1保存到二维数组中，函数返回二维数组的行数。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/ 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

int abstract(char str[],int b[])
{
/**********Program**********/
     int i;
     int k=0;
     for(i=0;str[i];i++){
     	  if(str[i]=='-'){
     	  	   int y=0;
     	  	   for(;str[i]&&isdigit(str[i]);i++){
     	  	   	   y=y*10+str[i]-'0';
			   }
			   b[k++]=y;
		  }
	 }
     return k;
/**********  End  **********/
}

int prime_m(int k,int b[],int x[][2])
{
/**********Program**********/
   
   
   
/**********  End  **********/
}

int main(void)
{
    char str[]={"&&B3yh-5AS-12HJ*@#35+eH-7pTR-15HY-17"};
    int i,n,k,b[10],x[10][2];
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    k=abstract(str,b);
    for(i=0;i<k;i++)
    {
        printf("%-4d",b[i]);
        fprintf(fp,"-%4d",b[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    n=prime_m(k,b,x);
    for(i=0;i<n;i++)
    {
        printf("%-4d\t%10d\n",x[i][0],x[i][1]);
        fprintf(fp,"-%4d\t%10d\n",x[i][0],x[i][1]);
    }
    printf("\n");
    fprintf(fp,"\n");

    fclose(fp);
    return 0;
}

