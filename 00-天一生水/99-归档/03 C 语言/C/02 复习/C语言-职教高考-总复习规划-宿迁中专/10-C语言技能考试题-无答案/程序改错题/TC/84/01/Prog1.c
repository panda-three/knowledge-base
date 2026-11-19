/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：查找介于M与N（0<M<N<32768）之间，且满足下列条件的所有整数：
      1.该数中有且仅有两个相同的数字位；
      2.该数是素数。
      
      测试数据：M=800，N=900 
      运行结果：
　　　　　811   877   881   883   887   899  

------------------------------------------------------------------------
注意：不得增行或删行，也不得更改程序的结构。
----------------------------------------------------------------------*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>

#define M 800
#define N 900 

int validate(int n)
{
    int i,j,k=0,num[5]= {0},size=0;
    do
    {
        num[size]=n%10;
        n=n/10;
        size++;   
/***********FOUND***********/
    }while(n<0);
    for(i=0; i<size-1; i++)
        for(j=i+1; j<size; j++)
            if(num[i]==num[j])
                k=k+1;
/***********FOUND***********/
    if(k>=1)
        return 1;
    else
        return 0;
}
int prime(int n)
{
    int i;
    for(i=2; i<(int)sqrt(n); i++)
        if(n%i==0)
            return 0;
    return 1;
}

int main()
{
    int i,count=0,n1=0,n2=0;
    for(i=M; i<=N; i++)
    { 
/***********FOUND***********/
        if(validate(M)&&prime(N))
        {
            count++;
            printf("%6d",i);
            if(count%8==0)
            printf("\n");
        }
    }
}
