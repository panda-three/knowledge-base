// 下列程序的功能为 :输入一个4一6 位的正整数,输出该数各位数字所能组成的最小正整 数,将结果写人文件 data.<C187>.txt。
// 例如:输入 4239,输出 2349;输入 5102 ,输出 125。
// 注意 : 如果输入的数值不在要求范围内,如 432,程序提示重新输入数据,直到输入正确位数的数据 为止。
#include <stdio.h>
#include <stdlib.h>

//输入4-6位的正整数
int input()
{
    int n;
    printf("请输入一个4-6位正整数:\n");
    scanf("%d", &n);
    while( n<1000 || n >= 1000000)
    {
        printf("请重新输入一个4-6位正整数:\n");
        scanf("%d", &n);
    }
    return n;
}

//组成最小正整数
int min(int num)
{
    int d[8], i, j, n = 0, t, s = 0;
    while(num)
    {
        d[n] = num-(num/10)*10;//num%10
        num=num/10;
        n++;
    }
    for(i = 0; i < n - 1; i++)
        for(j = i + 1; j < n; j++)
        {
            if(d[i] > d[j])
            {
                t = d[i];
                d[i] = d[j];
                d[j] = t;
            }
        }
    for(i = 0; i < n; i++)
        s = s * 10 + d[i];
    return s;
}

//保存数据至文件
int savefile(int num)
{
    FILE *p;
    if((p = fopen("data.txt", "w")) == NULL)
    {
        printf("Cannot open this file.\n");
        exit(0);
    }
    fprintf(p, "%d\n", num);
    fclose(p);
    return 0;
}

int main()
{
    int n, minu;
    n = input();
    minu = min(n);
    printf("minu = %d\n", minu);
    savefile(minu);
    return 0;
}
