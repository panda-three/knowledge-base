// Fibonacci 数列特点：第 1、2 个数分别是 1、1，从第 3 个数开始，每个数均为前两个数之和 。
// 程序要求求出前 $n$ 项之和 $sum$ 不超过 1000 时 $n$ 的最大值 。
#include <stdio.h>

int main() {
    int f1 = 1, f2 = 1, f3, sum, n = 2;
    sum = f1 + f2;

    do {
        f3 = f1 + f2;   
        sum = sum + f3;
        f1 = f2;        
        f2 = f3;        
        n++;            
    } while (sum <= 1000); 

    // 退出时 sum > 1000，所以最大项数是 n-1
    printf("前n项和不超过1000的最大项数:%d\n", n - 1); 
    return 0;
}