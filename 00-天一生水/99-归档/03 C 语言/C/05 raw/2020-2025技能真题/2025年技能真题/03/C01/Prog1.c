/*----------------------------------------------------------------------
【程序填空】
------------------------------------------------------------------------
题目：给定一个整型数组 nums和一个滑动窗口的大小k，找出所有滑动窗口中k个
      元素的最大值,存入数组result，再对数组result中的值降序排序，输出排序
      结果。 

测试数据：4, 3, -1, -3, 5, 3, 6, 7
滑动窗口长度：k=3

   滑动窗口的位置               最大值
-------------------------       -----
[4  3  -1] -3  5  3  6  7       4
 4 [3  -1  -3] 5  3  6  7       3
 4  3 [-1  -3  5] 3  6  7       5
 4  3  -1 [-3  5  3] 6  7       5
 4  3  -1  -3 [5  3  6] 7       6
 4  3  -1  -3  5 [3  6  7]      7
          
 
程序运行结果如下：
原数组：
 4  3 -1 -3  5  3  6  7
滑动窗口最大值数组：
 4  3  5  5  6  7
排序后的数组：
 7  6  5  5  4  3
-----------------------------------------------------------------------
注意：在填空标志处填写答案，并删除填空标志，勿改动程序中的其他部分。
----------------------------------------------------------------------*/
#include <stdio.h>

#define N 100

int result[100]={0};
int maxSliding(int nums[], int n, int k)
{
    int i,j,max,index = 0;
    for (i = 0; i <= n - k; i++) 
    {  
        max = nums[i];
/**************************SPACE******************************/
        for ( j = i + 1; j <=【?】; j++)
            if (nums[j] > max) 
                max = nums[j];
        result[index++] = max; 
    }
    return index;
}

void sort(int result[],int index)
{ 
    int i,j,k;
    int b[N];
    for(i=0;i<index;i++)
    { 
        k=0;
        for(j=0;j<index;j++)
            if(result[i]>result[j]||(result[i]==result[j]&&i>j) ) 
                k++;
/**************************SPACE******************************/
        【?】;
    }
    for(i=0;i<index;i++)
        result[i]=b[i];
}

int main() 
{
    int nums[] = {4, 3, -1, -3, 5, 3, 6, 7};
    int m,n = sizeof(nums) / sizeof(nums[0]);
    int i,k = 3;
    printf("原数组：\n");
    for (i = 0; i < n; i++) 
        printf("%2d ", nums[i]);
    printf("\n");
    m=maxSliding(nums, n, k);
    printf("滑动窗口最大值数组：\n");    
    for (i = 0; i < m; i++) 
        printf("%2d ", result[i]);
    printf("\n");
    sort(result,m);
    printf("排序后的数组：\n");  
    for (i = 0; i < m; i++) 
        printf("%2d ", result[i]);
    printf("\n");
    return 0;
}