/*----------------------------------------------------------------------
【程序改错】
------------------------------------------------------------------------
题目：一维数组orig中有N个互不相同的无序整数，在保持其余整数顺序不变的前提下，
      将最小整数移动到a[0],最大整数移动到a[N-1],并输出移动后的orig数组。

程序运行结果如下：
原始数据为：
    4   52    7   81   -6  -12    1    9   10   32

处理结果为：
  -12    4   52    7   -6    1    9   10   32   81

---------------------------------------------------------
注意：不得增行或删行，不得更改程序的结构
-------------------------------------------------------*/
#include <stdio.h>

#define N 10

void movesort(int orig[])
{
    int i,pmax,pmin,p;
/***********FOUND***********/
    pmax=pmin=0;
    for(i=0;i<N-1;i++)
    {
        if(orig[i]>orig[pmax]) 
            pmax=i;
        if(orig[i]<orig[pmin]) 
            pmin=i;
    }
    p=orig[pmin];
    for(i=pmin-1;i>=0;i--)
       orig[i+1]=orig[i];
    orig[0]=p;
/***********FOUND***********/
    if(pmax<pmin)  pmax=pmin;
    p=orig[pmax];
    for(i=pmax;i<N-1;i++)
/***********FOUND***********/ 
       orig[i-1]=orig[i];
    orig[N-1]=p; 
}

int main()
{
    int orig[N]={ 4,52,7,81,-6,-12,1,9,10,32};
    int i;
    printf("原始数据为：\n");
    for(i=0;i<N;i++)
        printf("%5d", orig[i]);
    printf("\n");
    movesort(orig);
    printf("\n处理结果为：\n");
    for(i=0;i<N;i++)
        printf("%5d", orig[i]);
    printf("\n");
    return 0;
}