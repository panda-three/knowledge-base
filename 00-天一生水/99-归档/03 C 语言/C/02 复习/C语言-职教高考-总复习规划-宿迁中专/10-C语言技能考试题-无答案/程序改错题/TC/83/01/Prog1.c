/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------

题目：用[3,5]、[5,7]作为测试数据，验证任意两个大于
      3的相邻素数的平方之间至少存在4个素数。                
      程序的运行结果为：          
      3的平方与5的平方之间共有5个素数：  11   13   17   19   23
      5的平方与7的平方之间共有6个素数：  29   31   37   41   43   47         
------------------------------------------------------------------------
注意：不得增行或删行，也不得更改程序的结构。
----------------------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define  M 3 
#define  N 9 

int isprime(int n)
{
/***********FOUND***********/
    int i=1;
    while(i<=sqrt(n)&&n%i) i++;
    if(i>sqrt(n))
        return 1;
    else
        return 0;
}

int makeprime(int m,int n, int b[])
{
    int i,k=0;
    if(m>n)
        return 0;
    for(i=m*m; i<n*n; i++)
        if(isprime(i))
/***********FOUND***********/
            b[++k]=i;
    return k;
}

int main()
{
    int a[50]= {0},b[100]= {0},i,m,k,j,n;
    m=0;
    for(i=M; i<=N; i++) 
        if(isprime(i)) 
            a[m++]=i;
               
/***********FOUND***********/
    for(i=0; i<=m-1; i++)
    {
        k=makeprime(a[i],a[i+1],b);        
        if(k<4)
        {
            printf("出现错误！\n");
            break;
        }
        printf("%d的平方与%d的平方之间共有%d个素数：",a[i],a[i+1],k);
        for(j=0; j<k; j++)
        {
            if(j%10==0)
                printf("\n");
            printf("%5d",b[j]);
        }
        printf("\n");
    }
}
