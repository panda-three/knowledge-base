// ; 整数 0一99 的升序数列 ,要求每隔两个数值取出一个,到末尾时循环至开头继续进行。编程找出被取出数值的序列 ,把该序列存放到文件 sortfile. txt 中。
// ; 以0~4 的升序数列为例:{0,1,2,3,4}0-一1-2(取出)一3一4一0(取出)一1-3一4(取出)
// ; 一1-3-1(取出)一3一3一3(取出) ,形成序列:{2,0,4,1,3)。

#include <stdio.h>
#include <stdlib.h>
#define COUNT_ID 100

int Nodel_id(int group[], int p);

int main() {
    FILE *wrfile;
    int i, j = 0, count = 0;
    int arr[COUNT_ID];
    
    // 初始化数组
    for (i = 0; i < COUNT_ID; i++) {
        arr[i]=i;
    }
    
    if ((wrfile = fopen("sortfile.txt", "w")) == NULL) {
        printf("File not open!\n");
        exit(0);
    }
    
    // 取出并存放前 99 个数值
    while (count < COUNT_ID - 1) {
        for (i = 0; i < 2; i++) {
            j = Nodel_id(arr, j);
            j = (++j) % COUNT_ID;
        }
        j=Nodel_id(arr, j);
        arr[j] = COUNT_ID;
        fprintf(wrfile, "%d,", j);
        ++count;
    }
    
    // 取出最后一个数值
    j = Nodel_id(arr, j);
    fprintf(wrfile, "%d", j);
    fclose(wrfile);
    
    return 0;
}

// 找出数列中下一个未被取出的数值
int Nodel_id(int group[], int p) {
    while (group[p % COUNT_ID] == COUNT_ID) {
        p=p+1;
    }
    return p;
}
