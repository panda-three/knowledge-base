// 下列程序的功能是：输入地区名称进行顺序查找；学生信息记录表的格式如32(87)所示，每条记录包含姓名、性别、身高（性别字段为0表示女，1表示男）。
// 程序需对学生信息按性别列队，规则为：女生在前（身高升序）、男生在后（身高降序），输出排队结果。
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N_MAX 5

// 交换学生信息（姓名、性别、身高）
void swap_data(int p1, int p2, char name[N_MAX][20], int sex[N_MAX], int height[N_MAX]);

int main() {
    FILE *infile;
    char name[N_MAX][20];   // 姓名数组
    int sex[N_MAX];        // 性别数组（0女，1男）
    int high[N_MAX];      // 身高数组
    int i, front = 0, last = N_MAX - 1,p ; // 队列头尾指针
     // 读取学生信息（假设文件格式：姓名 性别 身高）
    if ((infile = fopen("student.txt", "r")) == NULL) {
        printf("Cannot open file!\n");
        exit(0);
    }
      
    for (i = 0; i < N_MAX; i++) {
        fscanf(infile, "%s %d %d", name[i], &sex[i], &high[i]);
    }
    fclose(infile);
    
    while (front <= last)
    {
        p=front;
        for (i = front+1; i <= last; i++) {
            if ( sex[i] == sex[p] && high[p]>high[i]) {  // 女生（性别0）
                p=i;
            } 
        }
        if(sex[p]==0) {swap_data(front,p,name,sex,high);front++;}
        else  {swap_data(last,p,name,sex,high);(4);}
    }

    // 输出排队结果
    for (i = 0; i < N_MAX; i++) {
        printf("%s %d %d\n", name[i], sex[i], high[i]);
    }
    
    return 0;
}

// 交换两个学生的信息
void swap_data(int p1, int p2, char name[N_MAX][20], int sex[N_MAX], int height[N_MAX]) {
    char temp_name[20];
    int temp_sex, temp_height;
    
    // 保存p1的信息
    strcpy(temp_name, name[p1]);
    temp_sex = sex[p1];
    temp_height = height[p1];
    
    // 将p2的信息赋给p1
    strcpy(name[p1], name[p2]);
    sex[p1] = sex[p2];
    height[p1] = height[p2];
    
    // 将p1的原信息赋给p2
    strcpy(name[p2], temp_name);
    sex[p2] = temp_sex;
    height[p2] = temp_height;
}
