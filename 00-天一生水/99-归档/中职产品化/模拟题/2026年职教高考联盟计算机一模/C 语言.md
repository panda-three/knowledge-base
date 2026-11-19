计算机专业综合理论C语言程序填空习题

### 73题

阅读下列程序，请将①~④表示的内容填写在答题卡上相应位置。

```c
#include <stdio.h>
int main(void)
{
    char s[ ]="This is a C pro\0gram.";
    int k;
    char c;
    s[8]='\0';
    puts(s);
    for(k=2;k<6;k++)
    {
        switch(c=s[k])
        {
            case 'i': printf("%s","Fil");
            case 's': ++k;break;
            default : puts("Users");
            case 'r': puts("include");
            continue;
        }
        printf("%8s\n","Files");
    }
    return 0;
}
```

计算机专业综合理论试卷 第 8 页 (共 16 页)

## 上述程序中，第 (3) 行中数组 s 在内存中的占用空间为 **①** 字节；第 (6) 行中的字符串结束符'\0'属于 **②** 字符；第 (14) 行 continue;语句执行结束后，程序将继续执行第 **③** 行；第 (16) 行中 `%8s` 中的 8 用于指定输出数据的 **④**。

### 74题

阅读下列程序，请将运行结果填写在答题卡上相应位置。

````c
#include <stdio.h>
int main(void)
{
    int i, j, arr1[8]={2,4,6,8,10},arr2[8]={1,3,4,6,9,10,12};
    for(i=0;i<5;i++)
        printf("%-3d",arr1[i]);
    printf("\n");
    for(j=0;j<7;j++)
        printf("%-3d",arr2[j]);
    printf("\n");
    i=j=0;
    while(i<5 && j<7)
    {
        if(arr1[i]==arr2[j])
            printf("%-3d",arr1[i++]);
        else if(arr1[i]>arr2[j])
            j++;
        else
            i++,j++;
    }
    while(i<5)
        printf("%-3d",arr1[i++]);
    printf("\n");
    return 0;
}
```---
### 75题

阅读下列程序，请将运行结果填写在答题卡上相应位置。
```c
#include <stdio.h>
int a-3;
int fun(int a, int b)
{
    static int c;
    a=a+b;
    c+=b*a;
    b=a+c;
    return b;
}
````

````c
int main(void)
{
    int c=5,d;
    d=fun(a++,fun(--a,c));
    printf("%d %d %d",a,c,d);
    return 0;
}
```---
### 76题

给定若干仅由字符A和B组成的字符串（长度为1~80），计算对应串的积分。请在答题卡上写出①~④表示的内容以完善程序。

积分规则如下：每个字符A的得分为目前连续出现A的个数；每个字符B的得分为1分（多个连续出现的B仅积1分）。

例如：`AMBBABAAA`的积分为：1+2+(1)+(1)+1+2+3=12

程序运行结果为：
`AMBBABAAA的积分为：12`
`BAA的积分为：7`
`AAMBBABB的积分为：6`
```c
#include <stdio.h>
int count(char str[])
{
    int i=0,sum=0,t=1;
    while(str[i])
    {
        while(str[i]=='A')
        {
            ①;
            t++;
            i++;
        }
        if(str[i++] == 'B')
        {
            sum = sum + 1;
            while(②);
        }
        ③;
    }
    return sum;
}
int main(void)
{
    int i ;
    char str[3][80]={"AABBBABAAA","BAAA","AABBBABB"};
    for(i=0;i<3;i++)
        printf("%s的积分为： %d\n",str[i],④);
    return 0;
}
````

## 计算机专业综合理论试卷 第 10 页 (共 16 页)

### 77题

程序功能：从键盘输入N个学生的姓名和语文、数学、英语三门课程成绩，求出三门课程的均分，并按均分降序排序后，将成绩表写入二进制文件`fd.dat`。请在答题卡上写出①~④表示的内容以完善程序。

```c
#include <stdio.h>
#include <string.h>
#define N 3
#define LEN sizeof(STU)
typedef struct node
{
    char nam[10];
    int sc[3];
    float av;
}STU;
// 按均分降序排序
void sort(STU s[], int n)
{
    int i, j;
    ①;
    for(i=0; i<n-1;i++)
        for(j=0; j< ② ;j++)
            if(s[j].av<s[j+1].av)
            {
                temp=s[j];s[j]=s[j+1];s[j+1]=temp;
            }
}
int main(void)
{
    int i,j;
    FILE *fout;
    STU s[N];
    //输入学生信息并计算均分
    printf("请输入%d 个学生的姓名和语文、数学、英语三门课程成绩：\n", N);
    for(i=0;i<N;i++)
    {
        scanf("%s", s[i].nam);
        s[i].av=0;
        for(j=0;j<3;j++)
        {
            scanf("%d",&s[i].sc[j]);
            s[i].av+= ③;
        }
    }
    printf("\nbefore sort Data: \n");
    for(i=0;i<N;i++)
        printf("%s:%3d, %3d, %3d,%5.1f\n", s[i].nam, s[i].sc[0], s[i].sc[1], s[i].sc[2], s[i].av);
```

计算机专业综合理论试卷 第 11 页 (共 16 页)

```c
    //按均分降序排序
    sort(s,N);
    //显示排序后的结果
    printf("\nafter sort Data: \n");
    for(i=0;i<N;i++)
        printf("%s:%3d, %3d, %3d,%5.1f\n", s[i].nam, s[i].sc[0], s[i].sc[1], s[i].sc[2], s[i].av);
    //写入二进制文件
    fout=fopen("fd.dat","wb");
    for(i=0;i<N;i++)
        fwrite(  ④  );
    fclose(fout);
    return 0;
}
```

