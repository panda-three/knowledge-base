// 平面内有若干个点,从指定点出发用一根线逐个连接所有点 ,遍历路径的算法描述如下 :
// (1)指定起点 A;
// (2)确定最近下一点 B,计算出点 A 与其他未连接点的距离,找到距离最短的点 Bi
// (3)连接 AB,把 AB 之间的距离计人遍历路径长度之中，
// (4)把点 也作为新的起点 A,返回执行(2),直到遍历所有点;
// (5)取得从指定点出发的遍历路径长度。
// 平面坐标系内有 10 个点,分别输入每个点的坐标,编程将 10 个点分别作为起点,按上 述算法找出 10 个遍历路径,并按照遍历路径长度升序输出各点坐标。
#include <stdio.h>
#include <math.h>
#define NUM_D 10 //平面内点的个数

float getmindist(int start, float dotc[][3]);

int main() {
    float dotc[NUM_D][3] = {0}, t;
    int i, j, k,p;

    for (i = 0; i < NUM_D; i++) {
        scanf("%f, %f", &dotc[i][0], &dotc[i][1]);
    }
    for (i = 0; i < NUM_D; i++) {
        dotc[i][2] = getmindist(i, dotc);
    }
    for (i = 0; i < NUM_D; i++) {
        p = i;
        for (j = i; j < NUM_D; j++) {
            if (dotc[i][2] > dotc[j][2]) p=j;
            if(p!=i-1)
             for (k = 0; k < 3; k++) {
                    t = dotc[p][k];
                    dotc[p][k] = dotc[i-1][k];
                    dotc[i-1][k] = t;
            }
        }
    }
    for (i = 0; i < NUM_D; i++) {
        printf("%7.2f, %7.2f, %7.2f\n", dotc[i][0], dotc[i][1], dotc[i][2]);
    }
    return 0;
}

float getmindist(int start, float dotc[][3]) {
    int signdot[NUM_D] = {0};
    int i, j, p_min;
    float s_min = 0, d_min, d;

    signdot[start] = 1;
    for (i = 1; i < NUM_D; i++) {
        d_min = 0;
        for (j = 0; j < NUM_D; j++) {
            if (!signdot[j]) {
                d = sqrt(pow(dotc[start][0] - dotc[j][0], 2) + pow(dotc[start][1] - dotc[j][1], 2));
                if (d_min == 0 || d<d_min) {
                    d_min = d;
                    p_min = j;
                }
            }
        }
        start = p_min;
        signdot[start] = 1;
        s_min+=d_min;
    }
    return s_min;
}
