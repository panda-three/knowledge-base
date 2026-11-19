// 文件 student’. txt 中存放某班级学生信息记录,每条记录包含学生姓名和身高数据。下列程序的功能是:
// 从该班选两名身高最相近的学生作为国旗护旗手,输出护旗手的姓名。
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STU_MAX 100

int main() {
    FILE *in;
    int i, j, t, min, height[STU_MAX], stu_num = 0;
    char name[STU_MAX][20], str_temp[20];
    
    if ((in = fopen("student.txt", "r")) == NULL) {
        printf("Can not open file!\n");
        exit(0);
    }
    
    // 从文件中读取姓名和身高数据
    while (!feof(in)) {
        fscanf(in, "%s %d", name[stu_num], &height[stu_num]);
        stu_num++;
    }
    fclose(in);
    
    if (stu_num < 2) {
        printf("The number of student error!\n");
        return -1;
    }
    
    // 按照身高排序
    for (i = 1; i < stu_num; i++) {
        t = height[i];
        strcpy(str_temp, name[i]);
        j = i - 1;
        while (j >= 0 && height[j] > t) {
            height[j + 1] = height[j];
            strcpy(name[j + 1], name[j]);
            j--;
        }
        height[j + 1] = t;
        strcpy(name[j + 1], str_temp);
        if((j+1)!=i){
            height[j+1]=t;
             strcpy(name[j + 1], str_temp);
        }
    }
    
    t = height[1] - height[0];
    min = 1;
    
    // 找出身高最相近的数组元素下标
    for (i = 2; i < stu_num; i++) {
        if (t > height[i] - height[i - 1]) {
            t = height[i] - height[i - 1];
            min = i;
        }
    }
    
    printf("护旗手姓名: %s %s\n", name[min], name[min-1]);
    
    return 0;
}
