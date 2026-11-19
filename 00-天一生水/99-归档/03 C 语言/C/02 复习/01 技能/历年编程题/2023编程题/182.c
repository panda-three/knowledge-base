/*-------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：将字符串s中的连续数字转换为整数依次放入二维数组的第1列中，并分析该整数
      最小可以看成是几进制数，并将该进制值存放该数所在行的第二列。

程序运行结果如下：
原字符串为：  213   87  555  9203

转换成的整数及数制是：
213     4
87      9
555     6
9203    10

原数    数制    十进制整数
213     4       39
87      9       79
555     6       215
9203    10      9203

1.编写函数int abstract(char s[],int num[][3])，将s中各连续数字子串转换为
  正整数依次存放在数组num的第1列中，该数对应的进制存放在num的第2列，函数
  返回数据行数。
2.编写函数 void calc(int num[][3],int n)，将数组num第1列中n个正整数根据
  对应第2列的进制转换为10进制数，将转换后的十进制数存放在num数组的第3列。
  （所有进制不大于10）。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#define N 10  
int abstract(char s[],int num[][3])
{
/**********Program**********/
    int i,t,k=0,p;
	for(i=0;s[i];i++) 
	{
	    if(isdigit(s[i]))
	    {
	        t=0;
	        p=0;
	        for(;s[i]&&isdigit(s[i]);i++)
	        {
	            if(s[i]-48>p)
	                p=s[i]-48;
	            t=t*10+s[i]-48;
	        }
	        num[k][0]=t;
	        num[k][1]=p+1;
	        k++;
	    }
	}
	return k;
/**********  End  **********/
}
void calc(int num[][3],int n)
{
/**********Program**********/
	int i,m,t,p;
	for(i=0;i<n;i++)
	{
	    m=num[i][0];
	    jinzhi=num[i][1]
	    p=1;
	    t=0;
	    while(m)
	    {
	    	int wei=m%10;
	        t=t+wei*p;
	        p*=jinzhi;
	        m/=10;
	    }
	    num[i][2]=t;
	}
/**********  End  **********/
}

int main()
{
    char s[]={"  213   87  555  9203  "};
    int num[N][3],i,j,n;
    FILE *fp;
    if((fp=fopen("DATA.DAT","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    printf("原字符串为：%s\n",s);
    printf("\n转换成的整数及数制是：\n");
    n=abstract(s,num);
        for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
            printf("%d\t",num[i][j]);
        printf("\n");
        }
    for(j=0;j<2;j++)
    {
        for(i=0;i<n;i++)
            fprintf(fp,"%d,",num[i][j]);
        fprintf(fp,"\n");
    }
    calc(num,n);
    printf("\n原数\t数制\t十进制整数\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<3;j++)
            printf("%d\t",num[i][j]);
        printf("\n");
        fprintf(fp,"%d,",num[i][2]);
        }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;
}

