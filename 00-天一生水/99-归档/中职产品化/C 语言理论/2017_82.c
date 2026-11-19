// ; 文件 datal.txt 中存放了一个升序排列的数据序列 。
// ; 程序功能：从键盘输入一个数，查找该数是否存在，若存在则输出其位置 。
#include <stdio.h>
#include <stdlib.h>

int findnum(int x, int len, int num[]) {
    int low = 0, high = len - 1, m;
    
    while (low <= high) {
        m = (low + high) / 2;
        if (num[m] == x) 
            return (m + 1); // 找到则返回逻辑位置
        if (x > num[m])
            low = m + 1;
        else
            high = m - 1;
    }
    return -1; // 未找到
}

int main() {
    FILE *fp;
    int p, x, len = 0, num[50];
    
    if ((fp = fopen("datal.txt", "r")) == NULL) {
        printf("cannot open file\n");
        return 1;
    }
    
    while (fscanf(fp, "%d", &num[len]) != EOF) {
        len++;
    }
    fclose(fp);
    
    printf("enter a int num: ");
    scanf("%d", &x);
    
    p = findnum(x, len, num);
    if (p != -1) {
        printf("\n%d is found at position: %d\n", x, p);
    } else {
        printf("\n%d is not found\n", x);
    }
    return 0;
}