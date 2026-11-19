// ; 下列程序的功能是将随机生成的20个整数降序排序后写入文件data．txt。请在题82答题处完善程序。
#include <stdio.h>
#include <stdlib.h>
#define N 20

void disp(int[]);
void bsort(int[]);

void main()
{
    FILE ① ; // 定义文件指针
    int i;
    int a[N];

    // 生成随机数
    for(i=0; i<N; i++)
        a[i] = rand() % 1000 + 1;

    printf("排序前的数组为:\n");
    disp(a);

    bsort(a); // 调用排序函数

    printf("排序后的数组为:\n");
    disp(a);

    // 文件操作
    fp = fopen( ② ); 
    for(i=0; i<N; i++)
        fprintf(fp, "%5d", a[i]);
    fclose(fp);
}

// 冒泡法降序排序
void bsort(int a[N])
{
    int i, j, k;
    for(j=0; j<N-1; j++)
        for(i=0; i< ③ ; i++)
            if( ④ )
            {
                k = a[i];
                a[i] = a[i+1];
                a[i+1] = k;
            }
}

// 显示数据
void disp(int b[N])
{
    int i;
    for(i=0; i<N; i++)
    {
        printf("%3d%6d", i+1, b[i]);
        if((i+1) % 5 == 0) printf("\n");
    }
    printf("\n");
}