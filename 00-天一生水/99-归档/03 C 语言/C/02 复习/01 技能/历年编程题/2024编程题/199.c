/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：主函数main()中的字符数组s为测试数据，首先将字符串s中的连续八进制数
      字字符子串，转换成十进制正整数，保存到数组t中，然后对数组t中的所有
      素数进行升序排序，其他非素数位置保持不变。
      
      已给出函数int prime(int x)的功能：判断x是否为素数，是返回1，否返回0。 

测试数据为："ab15cgs11#6&&3?w21*su10hang17cv31x27dk02"
程序运行结果如下：
提取后：  13   9   6   3  17   8  15  25  23   2
排序后：   2   9   6   3  13   8  15  25  17  23
      
1.编写函数int abstract(char s[],int t[])，提取出字符数组s中连续的八进制
  数字字符子串，转换成十进制正整数，保存到数组t中，函数返回正整数个数。
2.编写函数void primesort(int t[], int n)，数组t中有n个元素，对其中的素数
  进行升序排序，数组中其他非素数位置保持不变。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int prime(int x)
{
    int i;
    for(i=2;i<=x/2;i++)
        if(x%i==0)
            return 0;
    return 1;
}

int abstract(char s[],int t[])
{
/**********Program**********/
    int i;
    int cnt=0;
	for(i=0;s[i];i++){
		if(isdigit(s[i])){
			int y=0;
			for(;s[i]&&isdigit(s[i]);i++){
				y=y*8+s[i]-'0';
			}
			t[cnt++]=y;
		}
	} 
   return cnt;

/**********  End  **********/
}

void primesort(int t[], int n)
{
/**********Program**********/
    int i,j,k;
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(t[i]>t[j]&&prime(t[i])&&prime(t[j]))
            {
                k=t[i];
                t[i]=t[j];
                t[j]=k;
            }
         }
    }   



/**********  End  **********/
}

int main(void)
{
    char s[]={"ab15cgs11#6&&3?w21*su10hang17cv31x27dk02"};
    int t[20],i,n;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    n=abstract(s,t);
    printf("提取后：");
    for(i=0;i<n;i++)
    {
        printf("%4d",t[i]);
        fprintf(fp,"%d\t",t[i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    primesort(t,n);
    printf("排序后：");
    for(i=0;i<n;i++)
    {
        printf("%4d",t[i]);
        fprintf(fp,"%d\t",t[i]);
    }
    fclose(fp);
    return 0;
}

