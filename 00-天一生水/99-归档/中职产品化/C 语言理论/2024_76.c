// 某课程考分记录表如题 76 表所示 ,存储于文件 student.txt 中。
// 考生可以多次参加该课程考试,取得多个考分,最终成绩按最高考分计。
// 文件中的数据首先按照考生考号升序排序，考号相同时按照考分升序排序。
// 编程实现:输入考号,查找并输出考生姓名和最终成绩。

// 题 76 表
// 考号 | 230201 | 240202 | 240202 | 240203 | 240203 | 240203 | 240205 | 240207
// 名| 孔佳 叶雪 叶雪 张雨 张雨 张雨 谢钧 李形
// 考分 97 89 98 77 88 96 :| .96 95
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct STU_REC {
    char id[9];    //考号
    char name[16]; //姓名
    int grade;     //考分
};

int find_stuid(char findid[], int length, struct STU_REC stuinfo[]);

int main() {
    struct STU_REC stu[100];
    int stu_n;
    char id[9];

    FILE *p_stu;
    if ((p_stu = fopen("student.txt", "r")) == NULL) {
        printf("Can not open file!\n");
        exit(0);
    }

    int n = 0;
    // while (!feof(p_stu)) {
    //     fread(&stu[n],sizeof(struct STU_REC),1,p_stu);
    //     n++;
    // }
     while (fread(&stu[n], sizeof(struct STU_REC), 1, p_stu) == 1) {
        n++;
    }
    fclose(p_stu);

    printf("Please enter student_id:\n");
    scanf("%s", id);
    stu_n = find_stuid(id, n-2, stu);

    if (stu_n !=-1) {
        printf("%s, %d\n", stu[stu_n].name, stu[stu_n].grade);
    } else {
        printf("无该考生信息\n");
    }
    return 0;
}

int find_stuid(char findid[9], int length, struct STU_REC stuinfo[]) {
    int left = 0, right = length, mid, res = -1;
    while (left <= right) {
        mid = (left + right) / 2;
        if (strcmp(stuinfo[mid].id, findid) <0) {
            left=mid+1;
        } else if (strcmp(stuinfo[mid].id, findid) > 0) {
            right = mid - 1;
        } else {
            res=mid;
            // left=mid+1;
            break;
        }
    }
    return res;
}
