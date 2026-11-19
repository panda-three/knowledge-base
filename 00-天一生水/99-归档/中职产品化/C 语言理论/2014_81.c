// 下列程序的功能是打印输出杨辉三角(如题81图所示)。请在题81答题处完善程序。

#include <stdio.h>
#define N 7

void main()
{
    int i, j;
    int ① ; // 定义二维数组
    for(i = 0; i < N; i++)
    {
        a[i][0] = a[i][i] = ② ; // 每行首尾赋值
        for(j = 1; j < i; j++)
        {
            a[i][j] = ③ ; // 中间数值计算
        }
    }
    for(i = 0; i < N; i++)
    {
        for(j = 0; j <= i; j++)
        {
            printf("%5d", ④ ); // 打印数组元素
        }
        printf("\n");
    }
}