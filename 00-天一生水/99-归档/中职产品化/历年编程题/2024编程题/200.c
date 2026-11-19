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
    int cnt=0;
	for(i=0;str[i];i++){
		if(str[i]=='-'){
			i++;
			int y=0;
			for(;str[i]&&isdigit(str[i]);i++){
				y=y*10+str[i]-'0';
			}
			b[cnt++]=y;
		}
	} 
	return cnt;
/**********  End  **********/
}

int prime_m(int k,int b[],int x[][2])
{
/**********Program**********/
    int i,j,p,n;
    int cnt=0;
    for(i=0;i<k;i++){
    	//求2的m次方-1 
    	int m=b[i];
    	int y=1;
		for(j=0;j<m;j++){
			y=y*2;
		}
		int q=y-1;
		//判断素数 
		int flag=1;
		for(p=2;p<q;p++){
			if(q%p==0){
				flag=0;
				break;
			}   
		}
		if(flag==0)
		   continue; 
		//判断逆序数是奇数；   
	    n=0;
	    int temp=q;
		while(temp){
			n=n*10+temp%10;
			temp=temp/10;
		} 
		if(n%2==0)
		    continue;
		//  2^m -1的十进制表示中包含数字1。   
		int temp1=q;
		int flag1=1;
		while(temp1){
			if(temp1%10==1){
				flag1=0;
				break;
			}
			temp1=temp1/10;
		} 
		if(flag1==1)
		   continue;
		   
		x[cnt][0]=m;
		x[cnt++][1]=q;
	}
  

   return cnt;
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

