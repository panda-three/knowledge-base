// 从文件 goods.txt 中读取商品信息（编号和好评数），根据好评数从高到低进行排序 。
// 若总数超过 10 条，输出前十条记录的编号 。
// 若总数不超过 10 条，输出全部编号 。
#include <stdio.h>
#include <stdlib.h>

#define G_MAX 100 // 定义最大商品数 [cite: 528]

// 从文件中读取数据，返回商品总数 [cite: 554]
int readfile(int good[][2]) {
    FILE *fp;
    int id, g, i = 0;
    if ((fp = fopen("goods.txt", "r")) == NULL) { // 打开文件 [cite: 559, 560]
        printf("无法打开此文件\n");
        exit(0);
    }
    while (!feof(fp)) {
        if (fscanf(fp, "%d,%d", &id, &g) == 2) { // 格式化读取 [cite: 565]
            good[i][0] = id;
            good[i][1] = g;
            i++;
        }
    }
    fclose(fp);
    return i; // 返回读取到的总条数 [cite: 570]
}

void main() {
    int goods[G_MAX][2];
    int t0, t1, i, p, file_n;
    
    file_n = readfile(goods); // 获取商品数据 [cite: 531]
    
    // 插入法排序（降序） 
    for (i = 0; i < file_n - 1; i++) {
        p = i;                // 记录当前位置 [cite: 535]
        t0 = goods[i + 1][0]; // 待插入的编号 [cite: 536]
        t1 = goods[i + 1][1]; // 待插入的好评数 [cite: 537]
        
        // 寻找插入位置
        while (p >= 0 && t1 > goods[p][1]) { // 降序判定 [cite: 538, 539]
            goods[p + 1][0] = goods[p][0];
            goods[p + 1][1] = goods[p][1];
            p = p - 1;        // 向前回溯 [cite: 543]
        }
        goods[p + 1][0] = t0; // 插入正确位置 [cite: 546]
        goods[p + 1][1] = t1; //
    }
    
    // 按要求输出商品信息 [cite: 551]
    printf("排名 商品编号\n");
    int limit = (file_n < 10) ? file_n : 10; // 取最小值 [cite: 552]
    for (i = 0; i < limit; i++) {
        printf("%d %d\n", i + 1, goods[i][0]); // 输出排名和编号 [cite: 553]
    }
}