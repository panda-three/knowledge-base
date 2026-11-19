// 下列程序旳功能是在键盘上输入学生3 门课旳成绩， 然后查找出平均成绩不及格旳学生并删除。
#include <stdio.h>
#define N 50
void main()
{
    float scores[N][3],avestu[N];
    int i, j, k, mm;
    
    printf("输入成绩：\n");
    for(i=0; i<N; i++)
        for(j=0; j<3; j++)
            scanf("%f", &scores[i][j]);
    
    for(i=0; i<N; i++)
    {
        avestu[i] = 0;
        for(j=0; j<3; j++)
            avestu[i] += scores[i][j];
        avestu[i] /= 3;
    }
    
    printf("学生成绩表：\n");
    for(i=0; i<N; i++)
    {
        for(j=0; j<3; j++)
            printf("%8.2f", scores[i][j]);
        printf("%8.2f\n", avestu[i]);
    }
    
    mm = N-1;
    for(i=mm; i>=0; i--)
        if(avestu[i] < 60)
        {
            mm=mm-1;
            for(j=0; j<=mm; j++)
            {
                for(k=0; k<3; k++)
                    //yo
                    scores[j][k] = scores[j+1][k];
            }

            avestu[j]=avestu[j+1];  
        }
           
    
    
    
    for(i=0; i<=mm; i++)
    {
        for(j=0; j<3; j++)
            printf("%8.2f", scores[i][j]);
        printf("%8.2f\n", avestu[i]);
    }
}

