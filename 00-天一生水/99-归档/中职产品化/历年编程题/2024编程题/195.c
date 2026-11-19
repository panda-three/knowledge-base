/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：下列程序将字符串中数字字符子串转换为整数，不考虑正负号，然后找出
      其中的最小数和最大数之间，满足下列条件的整数对（m,n）：
      (1) m小于n；
      (2) f(m)=f(n)=m+n+1，其中f(m)表示m的所有因子和(包括1和m)，
          f(n)表示n的所有因子和(包括1和n)。
例如：f(48)=1+2+3+4+6+8+12+16+24+48=124,f(75)=1+3+5+15+25+75=124，48+75+1=124，
      因此（48,75）是满足条件的整数对。
 
测试数据：
ASDB3yH15JIANG112SU*@#5+eH89rTR200HY117 

程序运行结果如下：    
M=3,N=200
(48,75) 
(140,195) 
 
1．编写函数void abstract(char str[],int b[])，将字符串str中的数字字符子
   串转换为整数，并将最小数和最大数分别存入b[0]和b[1]中。

2．编写函数int fun(int m,int n,int a[][2])，在[m,n]中查找满足上述条件的
   整数对保存到a数组中，函数返回找到的整数对个数。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/ 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

void abstract(char str[],int b[])
{
/**********Program**********/
    int i;
    int cnt=0;
	for(i=0;str[i];i++){
		if(isdigit(str[i])){
			int y=0;
			for(;str[i]&&isdigit(str[i]);i++){
				y=y*10+str[i]-'0';
			}
			b[cnt++]=y;
		}
	} 
    int max=b[0];
    int min=b[0];
    int j;
    for(j=0;j<cnt;j++){
    	if(b[j]>max){
    		max=b[j];
		}
		if(b[j]<min){
    		min=b[j];
		}
	}
    b[0]=min;
    b[1]=max;

/**********  End  **********/
}

int fun(int m,int n,int a[][2])
{
/**********Program**********/
    int i,j;
    int num=0;
    for(i=m;i<=n;i++){
    	int sum1=0;
    	for(j=1;j<=i;j++){
    		if(i%j==0)
    		  sum1=sum1+j;
		}
		
		for(j=i+1;j<=n;j++){
			int sum2=0;
			int k;
			for(k=1;k<=j;k++){
				if(j%k==0){
					sum2=sum2+k;
				}
			}
			if(sum1==sum2&&sum1==i+j+1){
				a[num][0]=i;
				a[num++][1]=j;
		    }
		}
		
	}
    
    return num;
       
/**********  End  **********/
}

int main(void)
{
    char str[]={"ASDB3yH15JIANG112SU*@#5+eH89rTR200HY117"};
    int i,num=0,m,n,b[100],a[100][2];
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    abstract(str,b);
    m=b[0];
    n=b[1];
    printf("M=%d,N=%d\n",m,n);
    fprintf(fp,"m=%d,n=%d\n",m,n);
    num=fun(m,n,a);
    for(i=0;i<num;i++)
    {
        printf("(%d,%d)\n",a[i][0],a[i][1]);
        fprintf(fp,"(%d,%d)\n",a[i][0],a[i][1]);
    }
    fclose(fp);
    return 0;
}
