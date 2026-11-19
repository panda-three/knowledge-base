# C语言题目汇总

## 真题

### 真题2021

78．阅读下列程序，将有关问题的答案填写在题 78 答题处。
```c
(1)#include<stdio. h>
(2)main(void)
(3){
(4)  int m ， n：
(5)  printf(" 请输入年份： ");
(6)  scanf(" %d" ， &m);
(7)  if(m%4==0)
(8)  {
(9)    if(m%100==0)
(10)   {
(11)     if(m%400==0)
(12)       n=1;
(13)     else1(14)       n=0
(15)   }
(16)  else
(17)       n=1；
(18) }
(19) else
(20)    n=0
(21) if(n)
(22)    printf("%d 是",m);
(23) else
(24)    printf( "%d 不是",m) ;
(25) printf( "闰年\n");
```
上述程序中，第 2 行是函数首部，其中 void 表达函数没有参数，故该行又可以表达为：__①__，与第 7 行 中的 if 语句相匹配的是第__②__ 行的 else 语句。此程序的功能是__③__，程序运营后，若输入数字“ ”，则输出成果是__④__ 。

---
79．阅读下列程序，将运营成果填写在题 79 答题处。
```c
# include<stdio. h>
void main( )
{
  int i=7;
  do
  {
    switch(i%2)
    {
      case 1: i+ + ; break;
      case 0: i- - ; continue;
    }
    i=i- 2 ;
    printf( "i= %d\n" ,i) ;
  } while(i>0) ;
}
```
---
80．阅读下列程序，将运营成果填写在 80 答题处。
```c
# include<stdio. h>
# define  strc  '$'
void prn(char cc)
{
  int n;
  for(n=1;n<=5;n+ +)
    printf( "%c" ,cc) ;
}
void main( )
{
  int i,j;
  char ss;
  ss=strc ;
  for(i=1;i<=3;i+ +)
  {
    printf( " ") ;
    prn(ss) ;
    printf( "\n") ;
  }
  for(i=3;i>1;i- -)
  {
    for(j=i;j>=1;j- -)
      printf( " ") ;
      prn(ss) ;
      printf( "\n") ;
  }
  printf( "\n") ;
}
```
---
81．下列程序的功能是在键盘上输入学生 3 门课的成绩，然后查找出平均成绩不及格的学生并删除。在题 81 答题处填写合适的内容以完善程序。
```c
# include <stdio. h>
# define N 50
void main()
{
  float scores[N][3],avestu[N];
  int i，j，k，mm;
  /*1--输入学生成绩*/
  printf(" 输入成绩： \n ");
  for (i=0；i<N；i+ +)
    for(j=0;  ①  ；j++)
      scanf(" %f",&scores[i][j]);

  /*2——计算学生平均成绩*/
  for(i=0；i<N；i+ +)
  {
    avestu[i]=  ②  ；
    for(j=0；j<3；j++)
      avestu[i]+=scores[i][j];
    avestu[i]/=3；
  }
  /*3——显示学生单科及平均成绩*/
  printf("学生成绩表：\n");
  for（i=0；i<N；i++）
  {
    for(j=0；j<3；j++)
      printf（" %8. 2f" ，  ③  ）;
    printf(" %8. 2f\n" ,avestu[i]);
  }
  printf("\\ n");

  /* 4——查找并删除平均成绩不及格学生记录*/
  mm=N-l;
  for(i=mm;i>=O;i——)
    if(avestu[i]<60)
    {
      mm= mm-l;
      for（j=0；j<=mm；j+ +）
      {
        for(k=0；k<3；k++)
          scores[j][k]= scores[j+l][k];
        avestu[j]=  ④  ；
      }
    }

  /* 5 ——输出平均成绩及格学生成绩*/
  for（i=0；i<=mm；i++）
  {
    for(j=0；j<3；j++)
      printf(” %8. 2f",scores[i][j]);
      printf( “%8.2f\n" ,avestu[i]);
  }
}
```
---
82．下列程序实现的是将键盘中输入的字符串写入文献“score．dat”中并显示输出，用“#”作为字符串输入结束的标志。在题 82 答题处填写合适的内容。
```c
# include <stdio. h>
# include <conio. h>
# include <string. h>
void main()
{
  void wtext(FILE * fp) ;
  void rtext ( FILE * fp) ;
    ①  ;
  fp=fopen("score. dat","w") ;
  wtext(fp) ;
  fclose(fp) ;
  fp=fopen("score. dat","r") ;
  rtext( fp) ;
    ②  ;
}
/*1——写字符串到文献*/
void wtext(FILE* fp)
{
  char strc[60],cc[2]="#";
  do{
    gets( strc);
    if( strcmp(  ③  )= =0）
      return;
    fputs(strc,fp);
    fputc('\n',fp);
  }while(1);
}
/* 2- -从文献读字符串到屏幕*/
void rtext( FILE* fp)
{
  char ch;
  while( !feof(fp)
  {
    ch= fgetc(  ④  );
    putchar(ch) ;
  }
  getch() ;
}
```
---

### 真题2022

### 反转字符串题目
```c
(6)  char str1[L_MAX],str2[L_MAX];
(7)  void REV_STR(char str1[],char str2[],int m);
(8)  int m;
(9)  gets(str1);
(10) m=strlen(str1);
(11) REV_STR(str1,str2,m);
(12) printf("%s\n",str2);
(13) }
(14) void REV_STR(char str1[],char str2[],int m)
(15) {
(16) int i,j;
(17) i=0;
(18) j=m-1;
(19) while(i<m)
(20) {
(21) str2[i]=str1[j];
(22) i++;j--;
(23) }
(24) str2[i]='\0';
(25) }
```
上述程序中,第(1)、(2)行是 ① 指令;子函数REV_STR有 ② 个形式参数,其声明语句位于第 ③ 行。
程序运行时输入:A12345,输出结果是 ④。

---

79. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
#include<string.h>
int main()
{
    char c[50]={"1H3ap1py!"};
    char str[50];
    long sum=0;
    int s,i=0;
    printf("string:\n");
    printf("%s\n",c);
    for(s=0;s<strlen(c);s++)
    {
        if((c[s]>='a'&&c[s]<='z')||(c[s]>='A'&&c[s]<='Z'))
        {
            str[i]=c[s];
            i++;
        }
        if(c[s]>='0'&&c[s]<='9')
        {
            sum=10 * sum+c[s]-48;
        }
    }
    str[i]='\0';
    printf("word:%s\n",str);
    printf("number:%d\n",sum);
    return 0;
}
```
```

80. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include <stdio.h>
int main()
{
    int i,j,s;
    char c='A';
    printf("This is:\n");
    for(i=1;i<=4;i++)
    {
        for(s=1;s<=8-i;s++)
            printf(" ");  //输出一个空格
        for(j=1;j<=i;j++)
        {
            printf("%c",c);
            c=c+1;
        }
        printf("\n");
    }
    printf("c=%-8d\n",c-'A');
    return 0;
}
```
81. 下列程序的功能是:输入不含空格的字符串,寻找并输出字符串中出现次数最多的字母,大小写视作同一字母,不统计非字母符号;若出现次数最多的字母有多个,输出其中ASCII码值最小的字母。请在答题卡上写出①~④表示的内容以完善程序。
```c
#include<stdio.h>
#include<ctype.h>
int main()
{
    char ch,s[1100],amount[27]={0};
    int i,max=0,c;
    ① ("%s",s);
    /* 把字符串 s 转换为小写字母,统计各字母出现次数 */
    for(i=0;s[i]!='\0';i++)
    {
        ch=tolower( ② );
        if(ch>='a'&&ch<='z') amount[ch-'a'+1]++;
    }
    /* 寻找并输出出现次数最多的字母 */
    for(i=1;i< ③ ;i++)
    {
        if( ④ )
        {
            c=i-1+'a';
            max=amount[i];
        }
    }
    if(max)
        printf("%c\n",c);
    else
        printf("No\n");
    return 0;
}
```
82. 下列程序的功能为:输入一个4~6位的正整数,输出该数各位数字所能组成的最小正整数,将结果写入文件data.txt。例如:输入4239,输出2349;输入5102,输出125。注意:如果输入的数值不在要求范围内,如432,程序提示重新输入数据,直到输入正确位数的数据为止。请在答题卡上写出①~④表示的内容以完善程序。
```c
#include<stdio.h>
#include<stdlib.h>
//输入4～6位的正整数
int input()
{
    int n;
    printf("请输入一个4～6位正整数:\n");
    scanf("%d",&n);
    while(!( ① &&n<=1000000))
    {
        printf("请重新输入一个4～6位正整数:\n");
        scanf("%d",&n);
    }
    return n;
}
//组成最小正整数
int min(int num)
{
    int d[8],i,j,n=0,t,s=0;
    while(num)
    {
        d[n]=num-(num/10)*10;
        ② ;
        n++;
    }
    for(i=0;i<n-1;i++)
        for(j=i+1;j<n;j++)
        {
            if( ③ )
            {
                t=d[i];
                d[i]=d[j];
                d[j]=t;
            }
        }
    for(i=0;i<n;i++)
        s=s*10+d[i];
```

### 真题2023

#### 73. 阅读下列程序,请将①~④表示的内容填写在答题卡上相应位置。
```c
(1) #include<stdio.h>
(2) struct Worker
(3) {
(4) char name[20];
(5) int salary;
(6) }per[20];
(7) int main()
(8) {
(9) int i=0;
(10) for(i=0;i<3;i++)
(11) {
(12) scanf("%s",per[i].name);
(13) scanf("%d",&per[i].salary);
(14) }
(15) for(i=0;i<3;i++)
(16) {
(17) if(per[i].salary>=1500)
(18) printf("%s\n",per[i].name);
(19) }
(20) return 0;
(21) }
```
上述程序中,用于输出数据的函数位于第 ① 行,从第 ② 行开始声明了结构体类型;程序运行后,主函数main的返回值是 ③ ;将源程序转换为目标程序的过程,称为 ④ 。
---
#### 74. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
#include<string.h>
int main()
{
    printf("File Edit Help\n");
    char key='F',password[]="123456";
    printf("Option:%c\n",key);
    unsigned int i;
    printf("password:");
    for(i=0;i<strlen(password);i++)
        printf("*");
    printf("\n");
    switch(key)
    {
    case 'F':
        printf("menu:File\n");break;
    case 'E':
        printf("menu:Edit\n");break;
    case 'H':
        printf("menu:Help\n");break;
    default:
        printf("Error.\n");
    }
    return 0;
}
```

#### 75. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
#include<string.h>
int main()
{
    char number_d[]="19731204";
    unsigned digit[10]={0},i,c,count=0;
    printf("%s\n",number_d);
    for(i=0;i<strlen(number_d);i++)
    {
        c=number_d[i]-48;
        digit[c]++;
    }
    printf("Missing number:\n");
    for(i=0;i<10;i++)
    {
        if(! digit[i])
        {
            printf("%c",i+48);
            count++;
        }
    }
    printf("\ncount:%d\n",count);
    return 0;
}
```

#### 76. 文件`student.txt`中存放某班级学生信息记录,每条记录包含学生姓名和身高数据。下列程序的功能是:从该班选两名身高最相近的学生作为国旗护旗手,输出护旗手的姓名。请在答题卡上写出①~④表示的内容以完善程序。
```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define STU_MAX 100
int main()
{
    FILE * in;
    int i,j,t,min,height[STU_MAX],Stu_num=0;
    char name[STU_MAX][20],str_temp[20];
    if((in=fopen("student.txt","r"))==NULL)
    {
        printf("Can not open file!\n");exit(0);
    }
    //从文件中读取姓名和身高数据
    while(! ① )
    {
        fscanf(in,"%s%d",name[Stu_num],&height[Stu_num]);
        Stu_num++;
    }
    fclose(in);
    if(Stu_num<2)
    {
        printf("The number of student error!\n");return -1;
    }
    //按照身高排序
    for(i=1;i< ② ;i++)
    {
        j=i−1;
        t=height[i];
        strcpy(str_temp,name[i]);
        while(j>=0&&height[j]>t)
        {
            height[j+1]= ③ ;
            strcpy(name[j+1],name[j]);
            j−−;
        }
        if((j+1) !=i)
        {
            height[j+1]=t;
            strcpy(name[j+1],str_temp);
        }
    }
    t=height[1]-height[0];
    min=1;
    //找出身高最相近的数组元素下标(即求相邻两个元素差值的最小值)
    for(i=2;i<Stu_num;i++)
    {
        if(t>=height[i]-height[i-1])
        {
            t= ④ ;
            min=i;
        }
    }
    printf("护旗手姓名:%s,%s\n",name[min],name[min-1]);
    return 0;
}
```

#### 77. 整数0~99的升序数列,要求每隔两个数值取出一个,到末尾时循环至开头继续进行。编程找出被取出数值的序列,把该序列存放到文件`sortfile.txt`中。

以0~4的升序数列为例子:{0,1,2,3,4}0→1→2(取出)→3→4→0(取出)→1→3→4(取出)→1→3→1(取出)→3→3→3(取出),形成序列:{2,0,4,1,3}。
请在答题卡上写出①~④表示的内容以完善程序。
```c
#include<stdio.h>
#include<stdlib.h>
#define COUNT_ID 100
int main()
{
    FILE * wrfile;
    int Nodel_id(int group[],int p);
    int i,arr[COUNT_ID],j=0,count=0;
    for(i =0;i<COUNT_ID;++i)
         ① ;
    if((wrfile=fopen("sortfile.txt","w"))==NULL)
    {
        printf("File not open\n");
        exit(0);
    }
    //取出并存放前99个数值
    while(count<COUNT_ID-1)
    {
        for(i=0;i<2;i++)
        {
            j= ② ;
            j=(++j)%COUNT_ID;
        }
        j=Nodel_id(arr,j);
        ③ ;
        fprintf(wrfile,"%d,",j);
        ++count;
    }
    //取出最后一个数值
    j=Nodel_id(arr,j);
    fprintf(wrfile,"%d",j);
    fclose(wrfile);
    return 0;
}

//找出数列中下一个未被取出的数值
int Nodel_id(int group[],int p)
{
    while(group[p%COUNT_ID] == COUNT_ID)
        p= ④ ;
    return p;
}
```

### 真题2024

#### 73. 阅读下列程序,请将①~④表示的内容填写在答题卡上相应位置。
```c
(1) #include<stdio.h>
(2) #include<string.h>
(3) #define A 9.8
(4) int main()
(5){
(6) int i=0,j=0,sumt=0,t[3]={0};
(7) double v,s;
(8) char time[20];
(9) printf("enter speed\n");
(10) scanf("%f",&v);
(11) printf("enter time(hh:mm:ss)\n");
(12) scanf("%s",time);
(13) while(i<strlen(time))
(14) {if(time[i]==':') j++;
(15) else t[j]=t[j]*10+time[i]-0x30;
(16) i++;}
(17) sumt=t[0]*3600+t[1]*60+t[2];
(18) s=v*sumt+A*sumt*sumt/2;
(19) printf("s=%11.5e",s);
(20) return(0);
(21)}
```
上述程序中,第 __①__ 行定义了一个符号常量;变量`s`的类型是 __②__ 型;程序中使用了输入输出函数`scanf`和`printf`,编译预处理时需要包含的头文件是 __③__ ;第 18 行表达式中优先级最低的运算符是 __④__ 。
---
#### 74. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
int main()
{
    char nums[]="04.951";
    printf("transform\n");
    printf("data:%s\n",nums);
    printf("trans1:%5.1f\n",4.951);
    switch(nums[4])
    {
        case '5':
            if(nums[5]=='0') break;
        case '6':case '7':case '8':case '9':
            nums[3]+=1;
            if(nums[3]>'9') {nums[1]+=1;nums[3]='0';}
            if(nums[1]>'9') {nums[0]+=1;nums[1]='0';}
            break;
    }
    nums[4]='\0';
    printf("trans2:%5s\n",nums);
    return(0);
}
```

#### 75. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
int main()
{
    char idf[]="Text_123";
    int count[5]={0};
    int p=0;
    printf("%s\n",idf);
    while(idf[p]!='\0')
    {
        if(idf[p]>='A'&&idf[p]<='Z')count[0]++;
        else if(idf[p]>='a'&&idf[p]<='z')count[1]++;
        else if(idf[p]>='0'&&idf[p]<='9')count[2]++;
        else if(idf[p]=='_')count[3]++;
        else count[4]++;
        p++;
    }
    printf("upper\tlower\tnumber\tunder\n");
    for(p=0;p<4;p++)
        printf("%d\t",count[p]);
    printf("\n");
    if(((idf[0]>='A'&&idf[0]<='Z'||idf[0]>='a'&&idf[0]<='z')&& !count[4])
        printf("Valid\n");
    else
        printf("Invalid\n");
    return(0);
}
```

#### 76. 某课程考分记录表如题76表所示,存储于文件`student.txt`中。考生可以多次参加该课程考试,取得多个考分,最终成绩按最高分计。文件中的数据首先按照考生考号升序排序,考号相同时按照考分升序排序。编程实现:输入考号,查找并输出考生姓名和最终成绩。

题76表：
| 考号 | 230201 | 240202 | 240202 | 240203 | 240203 | 240203 | 240205 | 240207 | ... |
|------|--------|--------|--------|--------|--------|--------|--------|--------|-----|
| 姓名 | 孔佳   | 叶雯   | 叶雯   | 张雨   | 张雨   | 张雨   | 谢钧   | 李彤   | ... |
| 考分 | 97     | 89     | 98     | 77     | 88     | 96     | 96     | 95     | ... |
```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct STU_REC
{
    char id[9];    //考号
    char name[16]; //姓名
    int grade;     //考分
};
int main()
{
    int find_stuid(char findid[],int length,struct STU_REC stuinfo[]);
    __①__ *p_stu;
    struct STU_REC stu[100];
    int n,stu_n;
    char id[9];
    if((p_stu=fopen("student.txt","r"))==NULL)
    {
        printf("Can not open file!\n");
        exit(0);
    }
    n=0;
    //读入文件中的考生信息
    while(!feof(p_stu))
    {
        __②__ (&stu[n],sizeof(struct STU_REC),1,p_stu);
        n++;
    }
    fclose(p_stu);
    printf("Please enter student_id:\n");
    scanf("%s",id);
    stu_n=find_stuid(id,n-2,stu);
    //根据返回的记录号输出考生姓名和成绩
    if(stu_n>=0)
        printf("%s,%d\n",stu[stu_n].name,stu[stu_n].grade);
    else
        printf("无该考生信息!\n");
    return(0);
}
//查找指定考号的记录号
int find_stuid(char findid[9],int length,struct STU_REC stuinfo[100])
{
    int left=0,right=length,mid,res=-1;
    while(left<=right)
    {
        mid=(left+right)/2;
        if(__③__)
            left=mid+1;
        else if(strcmp(stuinfo[mid].id,findid)>0)
            right=mid-1;
        else
        {
            res=mid;
            __④__;
        }
    }
    return(res);
}
```

#### 77. 平面内有若干个点,从指定点出发用一根线逐个连接所有点,遍历路径的算法描述如下：
1. 指定起点 A；
2. 确定最近下一点 B:计算出点 A 与其他未连接点的距离,找到距离最短的点 B；
3. 连接 AB:把 AB 之间的距离计入遍历路径长度之中；
4. 把点 B 作为新的起点 A,返回执行(2),直到遍历所有点；
5. 取得从指定点出发的遍历路径长度。

平面坐标系内有 10 个点,分别输入每个点的坐标,编程将 10 个点分别作为起点,按上述算法找出 10 个遍历路径,并按照遍历路径长度升序输出各点坐标。
```c
#include<stdio.h>
#include<math.h>
#define NUM_D 10 //平面内点的个数
int main()
{
    float getmindist(int start,float dotc[][3]);
    float dotc[NUM_D][3]={0},t;
    int i,j,k,p;
    for(i=0;i<NUM_D;i++)
        scanf("%f,%f",&dotc[i][0],&dotc[i][1]);
    for(i=0;i<NUM_D;i++)
        dotc[i][2]=__①__;
    for(i=1;i<NUM_D;i++)
    {
        __②__;
        for(j=i;j<NUM_D;j++)
            if(dotc[p][2]>dotc[j][2]) p=j;
        if(p!=i-1)
            for(k=0;k<3;k++)
            {
                t=dotc[p][k];dotc[p][k]=dotc[i-1][k];dotc[i-1][k]=t;
            }
    }
    for(i=0;i<NUM_D;i++)
        printf("%7.2f,%7.2f--%7.2f\n",dotc[i][0],dotc[i][1],dotc[i][2]);
    return(0);
}
//求从指定起点遍历路径的长度
float getmindist(int start,float dotc[NUM_D][3])
{
    int signdot[NUM_D]={0};
    int i,j,p_min;
    float s_min=0,d_min,d;
    signdot[start]=1;
    for(i=1;i<NUM_D;i++)
    {
        d_min=0;
        //确定距离最近的下一点
        for(j=0;j<NUM_D;j++)
        {
            if(!signdot[j])
            {
                //求两点之间的距离d
                d=sqrt(pow(dotc[start][0]-dotc[j][0],2)+pow(dotc[start][1]-dotc[j][1],2));
                if(d_min==0||__③__)
                {
                    d_min=d;
                    p_min=j;
                }
            }
        }
        start=p_min;
        signdot[start]=1;
        __④__;
    }
    return(s_min);
}
```

### 真题2025

73.阅读下列程序,请将①～④表示的内容填写在答题卡上相应位置。
```c
(1)#include<stdio.h>
(2)int negative(int a)
(3){
(4)if(a>0) a＝－a;
(5)return(a);
(6)}
(7)int main()
(8){
(9)int x,y;
(10)char c;
(11)c='K';
(12)scanf("%d",&x);
(13)y=negative(x);
(14)printf("%d- ->%d- ->%c\n",x,y,c+y);
(15)}
```
上述程序中,主函数main中定义了 __①__ 个char型变量;变量x的输入在第 __②__ 行;程序中唯一的自定义子函数从第 __③__ 行开始定义;主函数中,合计调用了 __④__ 个函数。

74.阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
int main()
{
    int a=12,b=10,y,t;
    printf("segment:\n");
    printf("a＝%d\n",a);
    t=a;
    a=b;
    b=t;
    printf("a＝%d\tb＝%d\n",a,b);
    if(a>0)y=1;
    else if(b<0)y=-1;
    else b=0;
    printf("y＝%4d\n",y);
    return(0);
}
```
75.阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
int main()
{
    int numa[10]={4,5,7,14};
    int numb[10]={3,5,6,7,9,11,12,13};
    int cn,m,n;
    puts("numa:");
    for(m=0;m<4;m++)
        printf("%-3d",numa[m]);
    printf("\n");
    cn=0;m=0;n=0;
    while(m<4&&n<8)
    {
        if(numa[m]==numb[n])
        {printf("%-3d",numa[m]);cn++;m++;n++;}
        else if(numa[m]>numb[n])n++;
        else m++;
    }
    printf("\nthe same number:%d\n",cn);
}
```
76.招录考试中考生记录表如题76表所示,存储于文件grade.dat中。现有A、B、C三个单位,每个单位录用不超过5名工作人员。根据招录规则,编程输出A、B、C三个单位的录用名册文件。请在答题卡上写出①～④表示的内容以完善程序。

招录规则：
1. 总分＝笔试成绩＋面试成绩。
2. 根据总分由高到低按序录用;若总分相同,面试成绩高者优先录用。(注:考生总分相同,则面试成绩不同)
3. 同一考生的两个志愿,先选择第1志愿录用;若第1志愿招录取满,选择第2志愿录用;若两个志愿均招录取满,该考生落选。

题76表
| 姓名 | 第1志愿 | 第2志愿 | 笔试成绩 | 面试成绩 |
|------|---------|---------|----------|----------|
| 谢小包 | C | A | 75 | 72 |
| 叶佳文 | A | B | 76 | 81 |
| | | | ... | |
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 5
void get_rank(char na[][3][20],int g[][3],int);
int main()
{
    FILE *fp, *fp1, *fp2, *fp3;
    int len=0,i,k;
    int gd[200][3]={0},ct[3]={0};
    char nv[200][3][20];
    if(! (  __①__ =fopen("grade.dat","r+")))
    {
        printf("无法打开文件! \n");
        exit(0);
    }
    while(! feof(fp))
    {
        fscanf(fp,"%s%s%s",nv[len][0],nv[len][1],nv[len][2]);
        fscanf(fp,"%d%d",&gd[len][0],&gd[len][1]);
        //总分＝笔试成绩+面试成绩。
        gd[len][2]=gd[len][0]+gd[len][1];
        len++;
    }
    __②__;
    if(! ((fp1=fopen("A.txt","w"))&&(fp2=fopen("B.txt","w"))&&
    (fp3=fopen("C.txt","w"))))
    {
        printf("无法打开文件! \n");
        exit(0);
    }
    i=0;
    /* 录用:同一考生的两个志愿,先选择第1志愿录用;若第1志愿招录取满,选择第2志愿录用;若两个志愿均招录取满,该考生落选。 */
    while((ct[0]<MAX||ct[1]<MAX||ct[2]<MAX)&& __③__ )
    {
        for(k=1;k<=2;k++)
            switch(nv[i][k][0])
            {
                case 'A':if(ct[0]<5){fprintf(fp1,"%s ",nv[i][0]);ct[0]++;k++;break;
                case 'B':if(ct[1]<5){fprintf(fp2,"%s ",nv[i][0]);ct[1]++;k++;break;
                case 'C':if(ct[2]<5){fprintf(fp3,"%s ",nv[i][0]);ct[2]++;k++;break;
            }
        i++;
    }
    fclose(fp);fclose(fp1);fclose(fp2);fclose(fp3);
}
//排名:根据总分由高到低按序录用;若总分相同,面试成绩高者优先录用。
void get_rank(char nv[][3][20],int gd[][3],int size)
{
    int i,j,k,p,gt;
    char nt[20];
    for(i=0;i<size-1;i++)
    {
        p=i;
        for(j=i+1;j<=size-1;j++)
            if( __④__ )
                p=j;
            else if(gd[p][2]==gd[j][2]&&gd[p][1]<gd[j][1])
                p=j;
        if(p!=i)
            for(k=0;k<=2;k++)
            {
                strcpy(nt,nv[p][k]);strcpy(nv[p][k],nv[i][k]);strcpy(nv[i][k],nt);
                gt=gd[p][k];gd[p][k]=gd[i][k];gd[i][k]=gt;
            }
    }
}
```
77.文件"sortdata.txt"中存放一组正整数组成的升序表。程序的功能是:输入一个不低于3位的正整数,不改变各数字之间的顺序关系,用削峰法删除其中三个数字后,得到一个值最小的新整数;查找新整数在上述升序表中是否存在,若存在输出它的序号。请在答题卡上写出①～④表示的内容以完善程序。

削峰法删除数字:一串数字,从最左侧开始,连续升序或降序的部分作为一段。若该段数字降序排列,删除最左侧的一个大数字后,新组成一个最小数;反之,该段数字升序排列,删除该段最右侧的一个大数字后,新组成一个最小数。
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define DEL 3
int main()
{
    int get_min(char strn[],int);
    int find(int);
    char strn[20];
    int newn,m;
    gets(strn);
    newn=get_min(strn,DEL);
    printf("最小整数:%d\n",newn);
    m=find(newn);
    if(m>=0)printf("在有序表中的序号:%d\n",m+1);
    else printf("有序表中不存在该数");
```
```c
//用削峰法删除其中三个数字后,得到一个值最小的新整数
int get_min(char strn[],int deln)
{
    int num,lenth,i,k,dn;
    lenth=strlen(strn);
    for(dn=1; __①__ ;dn++)
    {
        i=0;
        while(strn[i]<=strn[i+1]&&i<lenth-dn)
            i++;
        for(k=i;k<lenth-dn;k++)
            __②__ ;
    }
    num=0;
    for(k=0;k<=lenth-deln-1;k++)
        num=num*10+strn[k]-0x30;
    return(num);
}
//查找新整数在升序表中的序号
int find(int num)
{
    FILE *fpd;
    int a[100],p,h=0,b=0;
    if((fpd=fopen("sortdata.txt","r+"))==NULL)
    {
        printf("cannot open file. \n");
        exit(0);
    }
    while(! feof(fpd))
    {
        fscanf(fpd,"%d",&a[b]);
```

### 真题2026

#### 73. 阅读下列程序,请将①~④表示的内容填写在答题卡上相应位置。
```c
#include<stdio.h>
void dump(int x)
{
   ;
}
int main()
{
   int b=2;
   float a[5]={1,2};
   if(a[0]>0)
   printf("num:%5.1f\n",a[1]);
   clse
   dump(b);
   return 0;
}
```
上述程序中,第8行变量 b 的数据类型是 __①__ ,关系表达式位于第 __②__ 行,空语句位于第 __③__ 行,数组 a 有 __④__ 个元素。
---
#### 74. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include <stdio.h>
int main()
{
    int r=200,d=3,level=1;
    float dct;
    printf("Welcome!\n");
    printf("DailyRate:%dRMB\n",r);
    switch(level){
        case 1:dct=0.7;printf("Discount:0.7\n");break;
        case 2:dct=0.9;printf("Discount:0.9\n");break;
        default:dct=1.0;printf("Discount:1.0\n");
    }
    printf("charge:%7.2fRMB\n",r * d * dct);
    return 0;
}
```

#### 75. 阅读下列程序,请将运行结果填写在答题卡上相应位置。
```c
#include<stdio.h>
#include<string.h>
int main()
{
    char s1[]={"RIV12greatER34"},subs[100]={};
    int i,j=0,sum=0,len=strlen(s1);
    printf("split:\n");
    printf("%s\n",s1);
    for(i=0;i<len;i++){
        if(s1[i]>='0'&&.s1[i]<='9'){
            sum=sum * 10+s1[i]-48;
        }else if(s1[i]>='A'&&.s1[i]<'Z'){
            subs[j++]=s1[i];
        }else
            printf("%c",s1[i]);
    }
    subs[j]='\0';
    printf("\n%s\t%d\n",subs,sum);
}
```

#### 76. 文件 `gz.txt` 中存储的是按照姓名升序排列的收入记录,结构如题76图所示:每条记录包含姓名和收人,每个人可能有多条收人记录。文件中无空白记录行,编程实现:输人姓名,统计其名下总收人。请在答题卡上写出①~④表示的内容以完善程序。

题 76 图
| 姓名 | 收入 |
| Jack | 300  |
| Kate | 450  |
| Kate | 400  |
| Rose | 350  |
| ...  | ...  |
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//搜索姓名(xm)在有序表(name)中的位置
int search(char xm[],char name[][20],int n)
{
    int head=0,tail=n-1,mid,ret=-1;
    while(head<=tail){
        mid=head+(tail-head)/2;
        if(  ①  )
            head=mid+1;
        else
            tail=mid-1;
    }
    if(strcmp(name[tail],xm)==0) ret=tail;
    return ret;
}
int main()
{
     ②  *fgz;
    char name[100][20]={},fname[20];
    int sr[100]={0},n=0,sum=0;
    if((fgz=fopen("gz.txt","r"))==NULL){
        puts("File cannot open!\n");exit(0);
    }
    while(!feof(fgz)){
        fscanf(fgz,"%s  %d",name[n],&sr[n]);n++;
    }
    fclose(fgz);
    scanf("%s",fname);
    int regn=search(fname,name,n);
    if(regn!=-1){
        while(strcmp(name[regn],fname)==0)
            regn--;
         ③  ;
        while(strcmp(name[regn],fname)==0){
            sum+=sr[regn];regn++;
        }
        printf("%s 名下总收入:%d\n",fname, ④ );
    }else
        printf("查无此人:%s\n",fname);
    return 0;
}
```

#### 77. 问卷包含八条四个选项的单选题,用户凭手机号可以多次完整作答;作答记录保存在文件 `asw.txt` 中,结构如题77图所示:每条记录包含手机号和答案。问卷参考答案按题目顺序保存在文件 `key.txt` 中。编程实现:文件 `asw.txt` 中每个手机号仅保留一条正确率最高的记录。请在答题卡上写出①~④表示的内容以完善程序。

题77图
| 手机号       | 答案       |
| 13615164777  | ABCABCDD   |
| 18920686220  | ACCACCBC   |
| 17952667096  | BCCACDBC   |
| 18920686220  | AACCDADD   |
| ...          | ...        |
```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define M 50
#define N 8
//获取问卷作答记录,统计正确答案数
int  ①  (char tel[][12],char asw[][N+1],int yes[])
{
    FILE *fa, *fk;
    char key[N+1];
    int i=0,p;
    if((fa=fopen("asw.txt","r"))==NULL||(fk=fopen("key.txt","r"))==NULL){
        printf("File cannot open!\n");exit(0);
    }
    fscanf(fk,"%s",key);
    while(!feof(fa)){
        fscanf(fa,"%s  %s",tel[i],asw[i]);
        if(strlen(tel[i])!=0){
            for(p=0;asw[i][p]!='\0'&&key[p]!='\0';p++)
                if(  ②  )
                    yes[i]++;
            i++;
        }
    }
    fclose(fa);fclose(fk);
    return i;
}
//根据手机号和正确答案数降序排序
void sort(char tel[][12],char asw[][N+1],int yes[],int ct)
{
    int i,j,t;
    char s1[12],s2[N+1];
    for(i=0;i<ct-1;i++)
        for(j=1;j<ct-i;j++)
            if(  ③  ||strcmp(tel[j-1],tel[j])==0&&yes[j-1]<yes[j]){
                strcpy(s1,tel[j-1]);strcpy(tel[j-1],tel[j]);strcpy(tel[j],s1);
                strcpy(s2,asw[j-1]);strcpy(asw[j-1],asw[j]);strcpy(asw[j],s2);
                t=yes[j-1];yes[j-1]=yes[j];yes[j]=t;
            }
}
int main()
{
    FILE *fp;
    char teln[M][12]={},asw[M][N+1]={};
    int yes[M]={0},i,m,n,p,ct;
    ct=get_rec(teln,asw,yes);
    sort(teln,asw,yes,ct);
    for(i=0;i<ct;i++){
        p=i;
        while(strcmp(teln[i],teln[p+1])==0&&p+1<ct)
            p++;
        for(m=i+1,n=p+1;n<ct&&i<p;m++,n++){
            strcpy(teln[m],teln[n]);
            strcpy(asw[m],asw[n]);
            yes[m]=yes[n];
        }
         ④  ;
        if((fp=fopen("asw.txt","w"))==NULL){
            printf("File cannot open!\n");exit(0);
        }
        for(i=0;i<ct;i++)
            fprintf(fp,"%s  %s\n",teln[i],asw[i]);
        fclose(fp);
        return 0;
}
```

## 模拟题

### 2023级计算机应用专业调研卷

## 四、程序阅读题（全部为 C 语言题，共 5 小题，每题 12 分，共 60 分）

### 73 题

阅读下列程序，将①\~④内容填空。

```c
#include<stdio.h>
#define N 2 
#define M N+1
int main()
{
    int i,s=0; 
    for(i=1;i<=2+M+1;i++) 
        s=s+i;
    printf("s=%d
",s);
    return 0;
}
```

问题：

1. 程序中 N,M 被称作\*\*\*\*；

2. 程序循环\*\*\_\_次；

3. 程序的运行结果为\*\*\*\*；

4. 若将`i\&lt;=2\*M\+1`改成 `i\&lt;=2\*\(M\)\+1` 则运行结果为\*\*\*\*。

---

### 74 题

阅读程序，写出运行结果（代码片段）：

```c
#include<stdio.h>
int main()
{
    int i,j,k,s=0,t=0;
    for(i=1;i<=5;i++)
    {
        s+=i;
        for(j=1;j<i;j++)
        {
            s+=2;t-=1;
            for(k=j;k<5;k++)
            {
                s-=1;t=t+k;
            }
            s+=j;
            t=-t;
        }
    }
    printf("s=%d,t=%d
",s,t);
}
```

---

### 75 题

阅读带函数调用、全局 / 局部变量的 C 程序，写出每步输出结果：

```c
#include<stdio.h>
int reset(int i);
int workover(int i);
int i=0;
int main()
{
    int i=5;
    reset(i/2); 
    printf("i=%d
",i); 
    reset(i=i/2); 
    printf("i=%d
",i);
    reset(i/2);
    printf("i=%d
",i);
    workover(i);
    return 0;
}
int workover(int i)
{
    i=(i%i)*(i*i/(2*i)+4);
    printf("i=%d
",i);
    return(i);
}
int reset(int i)
{
    i=i<=2?5:0;
    return i;
}
```

---

### 76 题

苏超球队积分管理程序补全
假设今年苏超比赛有若干支球队参赛，每支球队有一个积分。现在需要对这些球队的积分进行管理，包括排序、删除和统计。

请在答题卡上写出①～④表示的内容以完善程序。(每空 3 分，共 12 分)

```c
#include<stdio.h>
#include <string.h>
#define MAX_TEAMS 20     // 最大球队数量
#define NAME_LEN 20      // 球队名称最大长度

// 球队结构体
typedef struct {
    char name[NAME_LEN];  // 球队名称
    int score;            // 积分
    int wins;             // 胜场数
} Team;

// 交换两个球队信息
void swap(Team *a, Team *b)
{
    Team temp;
    temp= *a;
    *a = *b;
    *b = temp;
}

// 按积分降序排序，积分相同则按胜场数降序
void sortTeams(Team teams[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
        for (j = 0; __①__; j++)
        // 填空 1:完善排序条件
        if (teams[j].score<teams[j+1].score|| __②__)
            swap(&teams[j], &teams[j + 1]);
}

// 查找并删除指定名称的球队
int deleteTeam(Team teams[], int n, char name[]) {
    int i, j;
    // 填空 2:完善删除逻辑
    for (i = 0; i < n; i++) {
        if (strcmp(teams[i].name,name)==0) { // 找到要删除的球队
            // 填空 3:将后面的球队依次前移
            for (__③__; j++) {
                teams[j]=teams[j+1];
            }
            return n - 1; // 返回新的球队数量
        }
    }
    return n; // 未找到球队，数量不变
}

// 统计积分大于等于指定值的球队数量
int countHighScoreTeams(Team teams[], int n, int minScore)
{
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (teams[i].score >= minScore)
            count++;
    }
    __④__;
}

int main() {
    Team teams[MAX_TEAMS] = {
        {"凯尔特人", 68, 22},
        {"流浪者", 65, 21},
        {"阿伯丁", 50, 15},
        {"希伯尼安", 48, 14},
        {"圣约翰斯通", 42, 12}
    };
    int n = 5; // 当前球队数量

    // 按规则排序球队
    sortTeams(teams, n);
    printf("排序后的苏超球队排名:
");
    for (int i = 0; i < n; i++)
        printf("%d. %s - 积分:%d,胜场:%d
",
            i + 1, teams[i].name, teams[i].score, teams[i].wins);

    // 删除指定球队
    char teamToDelete[] = "圣约翰斯通";
    n = deleteTeam(teams, n, teamToDelete);
    printf("
删除%s后剩余%d支球队
", teamToDelete, n);

    // 统计高分球队
    int highScoreCount = countHighScoreTeams(teams, n, 50);
    printf("积分不低于 50 分的球队有%d 支
", highScoreCount);
    return 0;
}
```

要求：完善程序①②③④填空。

---

### 77 题

二维数组模拟阅兵方阵，功能：列调换、区域统计、对角线替换、连续士兵统计、行列转置，完善程序填空：

```c
#include <stdio.h>
#define SIZE 6  //方阵尺寸(行列数相等)

//初始化方阵
void initSquare(int square[SIZE][SIZE]){
    int i,j;
    //初始化全为0 
    for (i=0;i<SIZE;i++){
        for (j =0;j<SIZE;j++){
            square[i][j]=0;
        }
    }
    square[0][0]= square[0][1]= square[0][2]=1; 
    square[1][0] = square[1][1]= square[1][2]=1; 
    square[2][0]= square[2][1]=square[2][2]=1;
    square[3][3] = square[3][4]= square[3][5]=1; 
    square[4][3]= square[4][4]= square[4][5]=1; 
    square[5][3]=square[5][4]=square[5][5]=1;
}

//打印方阵 
void printSquare(int square[SIZE][SIZE]){ 
    int i,j;
    for(i=0;i<SIZE;i++){
        for(j=0;j<SIZE;j++){ 
            printf("%d ", square[i][j]);
        }
        ___①___;  //填空1换行
    }
}

//1.调换两列元素
void swapColumns(int square[SIZE][SIZE],int col1,int col2){
    int i,temp;
    for (i=0;i<SIZE;i++){ 
        //填空2：交换第i行中col1和col2列的元素
        ___②___;
        square[i][col2]=temp;
        ___③___;
    }
}

//2.统计指定矩形区域内的士兵总数
int countInArea(int square[SIZE][SIZE], int startRow, int endRow, int startCol, int endCol){
    int count=0;
    int i,j;
    //填空3：遍历指定矩形区域并统计值为1的元素 
    for (i = startRow;i<= endRow;i++){
        for (j= startCol;j<=endCol;j++){
            if (square[i][j]==1)
                count++;
        }
    }
    return count;
}

//3.将主对角线(从左上到右下)上的空缺(0)替换为士兵(1)
void fillDiagonal(int square[SIZE][SIZE]){
    int i;
    //填空4：遍历主对角线元素并替换空缺
    for(i=0;i<SIZE;i++){
        if (square[i][i]==0){
            square[i][i]=1;
        }
    }
}

//4.查找指定行中连续士兵的最大数量
int maxConsecutiveInRow(int square[SIZE][SIZE], int row){
    int max=0,current=0;
    int j;
    for(j=0;j<SIZE;j++){
        if (square[row][j]==1)
        {
            //填空5：更新当前连续计数
            current++;
            if(___④___){
                max=current;
            }
        }else{
            //填空6：重置当前连续计数
            current=0;
        }
    }
    return max;
}

int main(){
    int square[SIZE][SIZE];
    initSquare(square);
    printf("初始方阵:
"); 
    printSquare(square);
    //调换第2列和第5列(下标1和4)
    swapColumns(square, 1,4); 
    printf("
调换列后的方阵:
"); 
    printSquare(square);
    //统计3-5行(下标2-4)和1-3列(下标0-2)区域的士兵数
    int areaCount=___⑤___;
    printf("
指定区域士兵总数:%d
",areaCount);
    //填补主对角线空缺 
    fillDiagonal(square);
    printf("
填补对角线后的方阵:
");
    printSquare(square);
    int maxConsec = maxConsecutiveInRow(square, 3); //查找第4行(下标3)的最大连续士兵数
    printf("
第4行最大连续士兵数:%d
",maxConsec);
    return 0;
}
```

要求：补全程序①\~④等填空内容。
### 2025 南通市2024-2025高三校际联考

### 73 题

阅读下列程序，写出运行结果。

```c
#include "stdio.h"
#include "string.h"
void main()
{
    int x=79,y=0x1a3;
    double a=0.031345623,b=5.8912345;
    char s[]="\116\x61tional\t\x44\141y.\n";
    printf("%#o,%#x\n",x,x);
    printf("%d,%o\n",y,y);
    printf("a=%e,b=%lf\n",a,b);
    printf("size=%d,len=%d\n",sizeof(s),strlen(s));
}
```

---

### 74 题

阅读下列程序，写出运行结果。

```c
#include <stdio.h>
int main()
{
    char dates[]="20241006";
    int month,ss;
    printf("Today is:");
    printf("%10s\n",dates);
    printf("Century:%5d\n",(dates[0]-48)*10+dates[1]-47);
    printf("Season:");
    month=(dates[4]-48)*10+dates[5]-48;
    if(month==1)month=13;
    ss=(month-2)/3;
    switch(ss)
    {
        case 0:printf("Spring.\n");break;
        case 1:printf("Summer.\n");break;
        case 2:printf("Autumn.\n");break;
        case 3:printf("Winter.\n");break;
        default:printf("Date error!\n");break;
    }
    return 0;
}
```

---

### 75 题

阅读下列程序，写出运行结果。

```c
#include "stdio.h"
main()
{
    int i,j,k,s1,s2,s3;
    s1=s2=0;s3=1;
    for(j=1;j<=3;j++)
        s1++;
        for(k=1;k<=j;k++,s2+=k+2)
        {
            s2++;
            for(i=-1;i<=k;i++)
                s3=-s3;
            s3=s3+i;
        }
    printf("s1=%d,s2=%d,s3=%d",s1,s2,s3);
    s1++;
}
```

---

### 76 题

功能：已有升序数组，输入一个数，按升序规律插入数组，补全程序①\~④空缺。

```c
#include <stdio.h>
#define N 10
void main()
{
    double a[N+1],x;
    int i,p;
    for (i=0;i<N;i++)
    {
        printf("%5.1lf",a[i]);
        a[i]=3*i+2;
    }
    printf("\n");
    printf("Please a data:\n");
    ① ;
    for(i=0,p=N;i<N;i++)
        if(x<a[i])
        {
            break;
        }
    for( ③ ;i--)
        a[p]=x;
        a[i]=a[i-1];
    for(i=0; ④ ;i++)
    {
        if(i%5==0)
            printf("%5.1lf",a[i]);
        printf("\n");
    }
}
```

---

### 77 题

功能：输入无空格字符串，找出出现次数最多的字母；不区分大小写，非字母不统计；多个最多则输出 ASCII 最大的字母，补全①\~④。

```c
#include <stdio.h>
#include <ctype.h>
int main()
{
    char ch,s[200],amount[27]={0};
    int i,max=0,c;
    scanf(①);
    for(i=0;s[i]!='\0';i++)
    {
        ch=s[i];
        if(ch>='a'&&ch<='z')
            ch=②;
        amount[ch-'a']++;
    }
    for(i=0;i< ③ ;i++)
        if(④)
        {
            c=i+'a';
            max=amount[i];
        }
    if (max)
        printf("%c\n", c);
    else
        printf("No\n");
    return 0;
}
```

---

你可以直接把上面全部内容复制，保存为 `C语言真题\.md` 即可使用。
需要我顺带把这 5 道题**标准答案、填空补全、运行结果**也加在文档末尾吗？

### 2025 学年苏州市单招期末调研

### 73 题

```c
(1)#include<stdio.h>
(2)#include< ① >
(3)void fun(int s[],int n)
(4){
(5) int i,t1,t2,p;
(6) for (i=0;i<n;i++)
(7) {
(8) p=10;
(9) t1=s[i];t2=pow(t1,2);
(10) while(t1>p)
(11) p*=10;
(12) while(t2>=t1)
(13)
(14) if(t2%p==t1)
(15)
(16) printf("%d 是%d 的子序列\n",t1,(int)pow(t1,2));break;
(17) else t2=t2/10;
(18) }
(19) }
(20)}
(21)int main()
(22){
(23) int s[4]={14,545,259,60};
(24) fun(s,4);
(25)}
```

题目要求：

1. 使用`pow()`需补充头文件①；

2. `p*=10` 是什么运算符②；

3. `(int)` 是什么类型转换③；

4. 写出程序运行结果④。

---

### 74 题

```c
# include <stdio.h>
int main( )
{
    long int x= 4280396,i,len=0;
    char dates[10],s,t;
    printf("Data is:\n");
    while(x)
    {
        dates[len++]=x%8+'0';
        x/=8;
    }
    dates[len]='\0';
    for(i=0;i<len/2;i++ )
    {
        t= dates[i];
        dates[i]=dates[len-1-i];
        dates[len-1-i]=t;
    }
    printf("%s\n",dates);
    for(i=1;i<len-1;i+=3)
        s= dates[i]>dates[i+1]? dates[i]:dates[i+1];
    switch(s+17)
    {
        case 'A':printf("Red \n"); break ;
        case 'B':printf("Orange\n" ); break;
        case 'C':printf("Yellow\n"); break;
        case 'D':printf("Green \n");break ;
        case 'E':printf("Blue\n");break;
        case 'F':printf("Indigo \n");break;
        case 'G':printf("Violet\n");break;
        default:printf("Invalid\n");
    }
}
```

题目要求：写出程序运行输出结果。

---

### 75 题

```c
#include <stdio.h>
#define N 10
int main()
{
    int a[N][N]={0},b[]={2,1,3,1,3,5,9,7,8,4};
    int i,j,k,f,m=0;
    k=(sizeof(b)/sizeof(int)+2)/3;
    for(i=0;i<k;i++)
        for(j=0;j<k;j++)
        {
            f=i-j>=0?i-j:j-i;
            if(f<=1)
                a[i][j]=b[m++];
        }
    for(i=0;i<k;i++)
    {
        for(j=0;j<k;j++)
            printf("%4d",a[i][j]);
        printf("\n");
    }
}
```

题目要求：写出程序运行输出结果。

---

### 76 题

**功能**：求一维数组众数，出现次数最多的数；多个众数从小到大输出，无众数提示。

```c
#include <stdio.h>
#define N 8
int mode(int a[],int b[]);
int main( )
{
    int a[N],i,n,b[N];
    for (i=0;i<N;i++)
        scanf("%d",&a[i]);
    ①
    n=mode(a,b);
    for(j=i+1; ② ;j++)
        if( )c[i]++;
    if(n==0)
        printf("该数列无众数!");
    else
        printf("该数列有%d 个众数:",n);
    for(i=0;i<n;i++)
        printf("%d\t",b[i]);
}
int mode(int a[],int b[])
{
    int i,j,x,max,n,k=0,k1=0,k2=0,c[N]={0};
    //将输入的数据排序
    for(i=N-2;i>=0;i--)
    {
        x=a[i];
        a[j-1]= a[j];
        a[j-1]=x;
    }
    //求数字出现的频率
    max= 1;
    for(i=0;i<N;i=j)
    {
        c[i]=1;
        for(j=i+1;j<N;j++)
            else break;
        if(max<c[i]) max=c[i];
        k1++;
    }
    //将出现频率最高的数字放在b 数组
    for(i=0;i<N;i++)
        if(max==c[i])
        {
            k2++ ;
            b[k++]=a[i];
        }
    if( ④ )
        return 0;
    else return k;
}
```

题目要求：补全 ①②③④ 四处空缺代码。

---

### 77 题

**功能**：读取`student\.txt`学生成绩文件、按总分降序排序、插入新学生成绩并保持有序。

```c
#include <stdio.h>
#include <stdlib.h>
#define N 11

print(int score[][5],int n)
{
    int i,j;
    printf("学号 数学 语文 英语 总分\n");
    for (i=0;i<n;i++)
    {
        for (j=0;j<5;j++)
            printf("%5d",score[i][j]);
        printf("\n");
    }
}

void sort(int score[][5],int n)
{
    int i,j,k,temp;
    for (i=0;i<n-1;i++)
    {
        for (j=i+1;j<n;j++)
            if(score[i][4]<score[j][4])
            {
                for (k=0;k<5;k++)
                    temp=score[i][k],score[i][k]=score[j][k],score[j][k]=temp;
            }
    }
}

int main()
{
    FILE *file;
    int score[N][5],a[5];
    int i,j,n=10,k,temp;
    if(( ① )==NULL)
    {
        printf("can't open a file!");
        exit(1);
    }
    for(i=0;i<10;i++)
        for (j=0;j<5;j++)
            fscanf(file,"%d",&score[i][j]);
    fclose(file);
    print(score,10);
    
    printf("请输入需要插入的学生的学号､语文､数学､英语:\n");
    scanf("%d%d%d%d",&a[0],&a[1],&a[2],&a[3]);
    a[4]=a[1]+a[2]+a[3];
    
    i=n-1;n++;
    while( ③ )
    {
        for (j=0;j<5;j++)
            score[i+1][j]=score[i][j];
        i--;
    }
    for (j=0;j<5;j++)
        ④
        
    print(score,n);
}
```

题目要求：补全 ①②③④ 四处空缺代码。

---

我已经整理成标准 Markdown 格式，你可以直接复制保存为 `\.md` 文件。
需要我顺便把**这 5 道题的标准答案、填空补全、运行结果**也加在文档后面吗？

### 2025 职教高考联盟 2 模

### 73 题 C 语言程序阅读

阅读下列程序，请将①\~④处表示的内容填写在答题卡中的相应位置。

```c
#include <stdio.h>
int m=5,n=6,a[10]={0,1,2};
void fl(void);
void f2(int m);
void main()
{ 
    int i;
    for(i=0;i<7;i++) 
        fl(); 
        f2(1);
    printf("\n%d,%d",a[m],a[n]);
}
void fl(void)
{ 
    static int n=3;
    a[n]=a[n-1]+a[n-2]+a[n-3];
    n++;
}
void f2(int m)
{ 
    for(;m<3;m+=2)
    { 
        int m; 
        for(m=1;m<4;m++) 
            printf("%d,",a[m++]);
    }
}
```

问题：
上述程序中，根据定义的位置，变量 m,n 是 ① 变量；程序的第 \(3\)\(4\) 行称为 ② 语句；程序运行时，输出结果的第一行是 ③ ，第二行是 ④。

---

### 74 题 C 语言程序阅读

阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include <stdio.h>
void main()
{ 
    int k=3.7,m=0;
    int a=012,b=4;
    do
    { 
        switch(k--)
        { 
            case 1:
                switch(++m)
                { 
                    case 1:b++;continue;
                    default:a++;b++;
                    case 0:a+=2;break;
                }
            case 2: a--;
            default: a+=2;b++;
        }
    }while(k>=0);
    printf("a=%d,b=%d,m=%d\n",a,b,m);
}
```

---

### 75 题 C 语言程序阅读

阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include "stdio.h"
void main()
{ 
    int m1=0,m2=5,m3=-1,i,j,k;
    for(i=3;i>=0;i--) 
    { 
        m1=m1+i;
        m3++;
        for(j=1;j<=3;j++)
        { 
            m2++;m3--;
            for(k=-2;k<=j;k++)
                m1++;
            m3=-m3;
        }
        m2-=6-j;
        printf("m1=%d\tm2=%d\tm3=%d\n",m1,m2,m3); 
    }
}
```

---

### 76 题 C 语言字符串函数填空

下面程序中函数`strmerge\(\)`的功能是：合并两个有序的字母字符串 \(字典序\) a 和 b 产生一个新的字符串 c，合并过程中要求删除重复出现的字符，同时保证合并后的字符串仍然有序，函数返回合并过程中删除的重复字符的个数。main \(\) 函数中输出合并后的字符串 “copy” 以及在合并过程中删除的字符个数 3。请将①\~④处的答案填写在答题卡对应的题号处。

```c
int strmerge(char a[],char b[],char c[]) { 
    #include<stdio.h> 
    int i=0,j=0,k=0;
    char t;
    while( ① )
    { 
        if(a[i]==b[j])
        { 
            t=a[i]; ② 
        } 
        else if(a[i]<b[j])
            t=a[i++];
        else
            t=b[j++];
        if(t!=c[k-1]) ③ 
    }
    while(a[i])
        if(a[i]!=c[k-1])
            c[k++]=a[i++];
        else
            i++;
    while(b[j])
        if(b[j]!=c[k-1])
            c[k++]=b[j++];
        else
            j++;
    c[k]='\0';
    return ④ ;
}
void main()
{ 
    char s1[10]="ccp",s2[10]="oppy",s3[20];
    int n;
    n=strmerge(s1,s2,s3);
    puts(s3); 
    printf("%d",n);
}
```

---

### 77 题 C 语言文件操作 \+ 排序填空

当前文件夹下的文本文件`file1\.txt` 中存放了若干个用空格分隔的整数，程序先从该文件中读取全部数据存入到整型数组 a 中，然后对数组 a 进行升序排序，并把排序结果一次写入到 d 盘 score 文件夹下的二进制文件`file2\.dat` 中。请将①\~⑥处的答案填写在答题卡上对应的题号处。

```c
#include <stdio.h>
#include <stdlib.h>
#define N 100
void insertsort(int x[],int num)//排序 
{ 
    int i,j,t;
    for( ① ;i--)
    { 
        j=i+1;
        t=x[i]; 
        while(j<num&&t>x[j]) 
        { 
            x[j-1]=x[j];
            ② 
        }
        x[j-1]=t;
    }
}
void main()
{ 
    int i,a[N],n=-1;
    FILE *fp1,*fp2;
    if((fp1=fopen("file1.txt","r"))==NULL)
    {
        printf("can't open file!");
        exit(0);
    }
    fp2= ③ ;
    //读取全部数据
    while(!feof(fp1))
    {
        ④ ;
        n++;
    }
    fclose(fp1);
    //调用排序算法
    ⑤ ;
    printf("\n"); 
    for(i=0;i<n+1;i++)
        printf("%d\t",a[i]);
    //将排序后的数据一次性写入文件
    for(i=0;i<n+1;i++)
        ⑥ ;
    fclose(fp2);
}
```

### 2025 计算机校级联盟-滨海中专

### 73 程序阅读题

```c
#include<stdio.h>
#include<math.h>
int main()
{
    int i,j,n;
    scanf ("%d", &n);
    for(i=2;i<=sqrt(n);i++)
        if(n%i==0)
            break;
    if(i>sqrt(n)) printf("Yes");
    else
        printf("No");
    return 0;
}
```

问题：

1. 用于输入数据的函数位于第\\*\\*\_\_行

2. 程序第 \(7\) 行中`sqrt\(n\)`作用是\\*\\*\\*\\*

3. 第 \(5\) 行定义变量的类型是\\*\\*\\*\\*

4. 如果输入数据是 10，程序运行结果是\\*\\*\\*\\*

### 74 程序运行结果题

阅读下列程序，写出运行结果

```c
#include <stdio.h>
int main()
{
    int a=1,i=10;
    do
    {
        switch(i%2)
        {
            case 1:i--;a=a+4;break;
            case 0:i--;continue;
        }
        if(a>10)
            break;
        i=i-2;
        printf("i=%d\n",i);
    }while(i>0);
    return 0;
}
```

### 75 程序运行结果题

阅读下列程序，写出运行输出图形 / 结果

```c
#include <stdio.h>
#define N 6
int main()
{
    int i,j;
    for(i=0;i<N;i++)
    {
        if(i!=N-1)
        {
            for(j=0;j<2*N-1;j++)
            {
                if(j==N-i-1 ||j==N+i-1)
                    printf("*");
                else
                    printf(" ");
            }
        }
        else
        {
            printf("\n");
            for(j=0;j<2*N-1;j++)
                printf("*");
        }
    }
    return 0;
}
```

### 76 程序完善题

功能：找出 \[100,200\] 之间逆序数等于本身的数，按每行 5 个元素输出
补全程序①\~④处内容

```c
#include<stdio.h>
int main()
{
    int i,t,sum,n=0;
    for(i=100;i<=200;i++)
    {
        sum=0;
        ① ;
        while(t)
        {
            sum=sum*10+t%10;
            ② ;
        }
        if(sum==i)
        {
            printf("%d\t",i);
            if(③) ④ ;
            printf("\n");
        }
    }
    return 0;
}
```

### 77 程序完善题

功能：输入两个大于零的整数，求最大公约数和最小公倍数
补全程序①\~④处内容

```c
#include <stdio.h>
int main()
{
    int m,n,r,p;
    scanf ("%d%d", ① );
    p=m*n;
    if(m<n)
    {
        n=m-n;
        m=m-n;
    }
    while(n)
    {
        r=m%n;
        m=n;
        n=r;
    }
    printf("m,n的最大公约数是:%d\n", ② );
    printf("m,n的最小公倍数是:%d", ③ );
    return 0;
}
```

### 2025 镇江 职教高考计算机一模

## 五、程序阅读题（共 5 题，均为 C 语言）

### 78 题 C 语言字符提取数字求和程序

阅读下列程序，将有关问题的答案填写在答题处。

```c
(01)#include<stdio.h>
(02)#include<ctype.h>
(03)void apart(char a[])//被调函数
(04){
(05) int i,sum,sign=1,s;
(06) i=sum=0;
(07) while(a[i])
(08)
(09) while(!isdigit(a[i]) &&a[i])
(10) {
(11) sign=a[i]=='-'?-1:1;
(12) i++;
(13) }
(14) s=0;
(15) while(isdigit(a[i]))
(16) s= ③
(17) s=s*sign;
(18) if(s!=0)
(19) sum+=s;
(20) }
(21) printf("*sum%-8d*
",sum);
(22)}
(23)int main()
(24){
(25) char sour[100]={"kn--.26, q, -37. &#%%-18 w194,jAF5aS"};
(26) apart (sour);
(27) return0;
(28)}
```

问题：

1. 第 \(01\)\(02\) 行称为\*\*\*\*

2. \(03\) 行`//`后的语句是 C 语言中的\*\*\_\_语句，运行不执行

3. 第 \(16\) 行空格处应填什么代码

4. 程序运行结果为多少

---

### 79 题 C 语言二维字符数组程序阅读

```c
#include"stdio.h"
#include <stdio.h>
int main() {
    char p[3][5] = {"3697", "2854", "6453"};
    int i, j;
    long num=0;
    for(i=0; i<2; i++) {
        j=0;
        while(p[i][j]!='\0') {
            if((p[i][j]-'\0')%2)
                num=num*10+p[j][i]-'0';
            j+=2;
        }
    }
    printf("%d
" ,num);
}
```

要求：写出程序运行结果


---

### 80 题 C 语言全局变量、静态变量、外部变量程序阅读

```c
#include"stdio.h"
int y=2;
void fun(int m,int n){
extern int x;
static int y=3;
x=m+n;
m++;
y=m+5;
}
int x=5;
void main(){
int i;
for(i=1;i<=3;i+=2){
fun (y=x+5,x);
printf("x=%d, y=%d
",x,y);
}
}
```

要求：写出程序运行输出结果

---

### 81 题 C 语言字符串环最小串查找程序填空

题目：将长度为n的字符串`str`看成一个首尾相连的环，这样从`str`的n个位置开始向后取n个字符，可以得到n个长度为n的字符串。程序找出这n个字符串中最小字符串。 例如：将长度为10的字符串"CBSTIBSTU0"看成一个首尾相连的环。因此可以分别得到"CBSTIBSTU0"、"BSTIBSTUOC"、"STIBSTUOCB"…"OCBSTIBSTU"等10个字符串，这10个字符串中最小的字符串为"BSTIBSTUOC"。
```text
CBSTIBSTU0 起始位置为 1 的字符串 BSTIBSTUOC 是最小字符串
FJMQFJMPQS 起始位置为 4 的字符串 FJMPQSFJMQ 是最小字符串
```
```c
#include<stdio.h>
#include<string.h>
#define N 10
int comp(char str[], int p, int q) {
    int i ;
    for(i = 0; i < N; i++)
        if(str[(p+i)%N] != str[(q+i)%N])
            return ①;
    return 0;
}

int main() {
    char str[2][N+1]={"CBSTIBSTUO", "FJMQFJMPQS"};
    int i, j,min;
    for(i = 0; i<2; i++)
    {
        ②;
        for(j=1;j<N;j++)
            if(comp(③))
                min = j;
        printf("%s 起始位置为%d 的字符串",str[i],min);
        for(j = 0; j < N; j++)
            putchar(④);
        printf("是最小字符串
");
    }
    return 0;
}
```

要求：补全标注①②③④四处空缺

---

### 82 题 C 语言孪生素数统计 \+ 文件操作程序填空

题目：统计不大于 n 的孪生素数对数，并写入`d:\file\.txt`，完善程序。

```c
#include<stdlib.h>
#include<stdio.h>
#define N 80
int main()
{
FILE *f;
if((f=fopen( ))==NULL)
printf("can not open file
");
exit(0);
int i, j=0, p1, p2,n, a[N][2];
scanf ("%d", &n);
for(i=3;i<=n-2;i=i+2)
{
p1=i;
p2=i+2;
if(2 _==2)
a[j][0]=p1;
a[j++][1]=p2;
}
for(i=0;i<j;i++)
{printf("%d %4d
", a[i][0],a[i][1]);
fclose(f);
return 0;
}
int prime(int n)
int i, k=sqrt(n);
if(n<2)
return 0;
for(i=2; ④ ;i++);
if(i>k)
return 0;
return 1;
}
```

要求：补全标注①②③④四处程序空缺
### 2025年职教高考联盟计算机

### 73 题

阅读下列程序，请将 1\~4 表示的内容填写在答题卡中的相应位置：

```c
(1) #include <stdio. h>
(2) #include <string.h>
(3)#define N 18
(4) void main()
(5) {char a[N]="\AB\103%D\66\0BCA";
(6) char c;
(7) int i;
(8) for(i=1;a[i];i++)
(9) {c=a[i];
(10) 
(11) switch (c) {
(12) case 'A' :putchar (c+1) ;break;
(13) case 'B' :putchar(c-1);i++;continue;
(14) case 'C' :putchar (c+1) ;break;
(15) default:putchar( '#' );break;
(16)
(17) putchar ('@');
(18)
(19) 
(20)} printf("\nsize=%d, len=%d\n", sizeof (a), strlen(a));
```

问题：
第 \(3\) 行定义的 N 是一个\\*\\*\\*1\\*\\*\\*；本程序中使用到的库函数有\\*\\*\\*2\\*\\*\\*；在 Dev C\+\+ 编程环境中，sizeof 的功能是\\*\\*\\*3\\*\\*\\*；此题中字符 \&\#39;%\&\#39; 对应的输出是\\*\\*\\*4\\*\\*\\*。

---

### 74 题

阅读下面程序，请将运行结果填写在答题卡上相应位置：

```c
#include<stdio. h>
int main() 
{
    int sn[6]={73, 60, 47, 35};
    int d[2]={18, 43};
    int i,p,k;
    printf ("The array is:\n");
    for(i=0;i<4;i++)
        printf("%4d", sn[i]);
    printf("\n"); 
    for(i=0;i<2;i++)
    {
        p=i+3;
        while(d[i]>sn[p]&&p>=0)
        {
            sn[p+1]=sn[p];
            p=p-1;
        }
        sn [p+1]=d[i];
        for (k=0;k<5+i;k++)
            printf("%d", sn[k]);
        printf("\n");
    }
    return 0;
}
```

---

### 75 题

阅读下面程序，请将运行结果填写在答题卡上相应位置：

```c
#include<stdio. h>
int a=7, b=5;
int f(int c) 
{
    static int a=2;
    int t=1; 
    while(--c>=a)
        t=t*c;
    return (a++)+t;
}
void main()
{
    int i,s=0;
    for(i=1;i<3;i++) 
    {
        int a=5;
        s+=f (a);
        printf("%d\t", s);
    }
    s+=a+b;
    printf("%d\n", s);
}
```

---

### 76 题

请将 1\~4 表示的内容填写在答题卡中的相应位置，实现如下图形的打印：

```text
1 2 4 7 11
3 5 8 12
6 9 13
10 14
15
```

```c
#include <stdio. h>
#define N 5
int main()
{
    int i,j,k;
    int a[N][N]={0}; 
    for(1 ;j<N;j++)
        for(i=j;i>=0;i--)
            2 =k++;
    for(i=0;i<N;i++)
        for(j=0;_3_;j++)
            printf("%d\t", a[i][j]);
    ④
    return 0;
}
```

需填空：①②③④

---

### 77 题

程序功能：将二维数组`int n\[2\]\[5\]`中第一行各元素的最高位，存放在数组第二行的相应列，再将 5 个 1 位正整数从右至左组合成一个 5 位正整数，并存入 D 盘 abc 文件夹下的文本文档 data\.txt 中。将 1\~4 空缺内容补全。

```c
#include<stdio. h>
#include<stdlib.h>
#define N 5
void f1(int n][N)//取出二维数组n第一行各元素的最高位,存放在第二行的相应列
{
    int i,t;
    for(i=0;i<N;++i) 
    {
        t=n[0][i];
        while(t>=10)
            t/=10;
        n[1][i]=t;
    }
}
int f2(int n[])//从右至左将一维数组n中5个1位正整数组合成一个5位正整数返回
{
    int s,i; 
    for(s=0, i=N-1;i>=0;--i)
        ___2___;
    return s;
}
int main()
{
    int a[2] [N]={32, 507, 766, 96803, 110};
    int i, j, val; FILE *fp;
    ___3___
    f1(a);
    val=f2(a[1]);
    for(i=0;i<2;++i)
    {
        for(j=0;j<N;++j) 
        { 
            printf("%6d",a[i][j]); 
            fprintf(fp, "%6d", a[i][j]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    printf("%6d\n", val);
    fclose(fp);
    return 0;
}
```

需填空：①②③④（题干标注 4 处空缺）

---

以上就是试卷里**全部 C 语言程序阅读、程序填空类题目**，无其他 C 语言相关选择 / 填空题型。需要我把这几道题的**标准答案和详细解析**也整理出来吗？

### 2025年职教高考计算机应用专业综合理论试卷

## 一、程序阅读填空题

### 73 题 C 语言程序阅读填空

```c
#include<stdio.h>
#include<math.h>
main()
{
    int a[]={4,5,0,-3,-1,-2};
    int i=0,y,f,sum=0;
    while(a[i]!=-1)
    {
        f=a[i]==0?0:a[i]/abs(a[i]);
        switch(f)
        {
            case 1:y=2*a[i]+1;break;
            case 0:y=0;i++;continue;
            case -1:y=2*a[i]-1;
        }
        sum=sum+y;
        i++;
    }
    printf("sum=%4d",sum);
}
```

问题：

1. 第 \(3\) 行省略了函数返回值的类型，则默认为\\*\\*\\*\\*\(英文\)；

2. 第 \(9\) 行语句包含的表达式中，优先级级别最高的运算符是\\*\\*\\*\\*；

3. 执行了 \(13\) 行中的 continue 语句，程序将跳转到第\\*\\*\_\_行；

4. 该程序的运行结果是\\*\\*\\*\\*。

### 74 题 C 语言程序阅读写运行结果

```c
#include<stdio.h>
#include<math.h>
char ch='A';
int k=2;
void draw()
{
    int k=2,i;
    for(i=1;i<=5-2*abs(k);i++)
        printf("%c",ch);
    ch++;
    k--;
}
void drawl(char ch)
{
    static int k=2;
    int i;
    for(i=1;i<=2*abs(k)+2;i++)
        printf("%c",ch);
    ch++;
    k--;
}
int main()
{
    int i,j,p;
    char ch='B';
    for(i=1;i<=2*k+1;i++)
    {
        draw();
        drawl(ch);
        printf("\n");
    }
}
```

要求：写出程序运行结果

### 75 题 C 语言程序阅读写运行结果

```c
#include <stdio.h>
void change(int a[],int b[],int c[],int n)
{
    int i,j,t,p=0;
    for(i=0;i<n;i++)
    {
        b[i]=1;
        for(j=0;j<n;j++)
            if(a[i]>a[j]) b[i]++;
        c[b[i]-1]=a[i];
    }
}
int main()
{
    long num=20250321;
    int i,j,dex[3][10]={0},n=0;
    while(num/10)
    {
        dex[0][n++]=num%100;
        num=num/10;
    }
    printf("%3d",dex[0][n-1]);
    change(dex[0],dex[1],dex[2],n);
    printf("\n");
    for(i=1;i<3;i++)
    {
        for(j=0;j<n;j++)
            printf("%3d",dex[i][j]);
        printf("\n");
    }
}
```

要求：写出程序运行结果

### 76 题 完善 C 语言程序（打印 100 以内半素数）

素数、半素数定义：

- 素数：大于 1，除 1 和自身无其他约数

- 半素数：大于 1，可分解为**两个不相同素数乘积**

```c
#include<stdio.h>
#include<math.h>
#define N 100
int prime[N];

//寻找2~N之间的所有素数，返回素数个数
int prime_table()
{
    int i,j,k;
    int p[N]={1,1,0};
    for(i=2;i<=N;i++)
        for(j=i+i;j<=N;____1____)
            p[j]=1;
    for(k=0,i=0;i<N;i++)
        if(p[i]!=1) ____2____=i;
    return k;
}

//二分查找素数
int binary_search(int a[],int n,int goal)
{
    int low,high,mid;
    low=0;high=n-1;
    while(low<=high)
    {
        mid=(low+high)/2;
        if(a[mid]>goal) high=mid-1;
        else ____3____;
    }
    return -1;
}

//寻找1~N之间的所有半素数
int main()
{
    int n,i,k,flag;
    n=prime_table();
    printf("1~%d之间的半素数的有:\n",N); 
    for(k=1;k<N;k++)
    {
        flag=0;
        for(i=0;i<n;i++)
        {
            if((k%prime[i]==0)&&____4____)
            {
                flag=1;break;
            }
        }
        if(flag==1 && pow(prime[i],2)!=k)
            printf("%d\t",k);
    }
}
```

要求：补全①②③④四处代码

### 77 题 完善 C 语言程序（压缩字符串还原）

压缩规则：连续相同字符转为`字符\*次数`，如`cccaeeeeebkkkkkkkkkkkkkkd`压缩为`c\*3ae\*5bk\*14d`，编程实现读取文件压缩字符串并还原。

```c
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
void fun(char t[]);
int main()
{
    char t[100];
    int n;
    FILE *fin;
    if((____1____)==NULL)
        exit(0);
    while(!feof(fin))
    {
        fscanf(fin,"%s",t);
        printf("压缩后的字符串为:%s\n",t);
        fun(t);
        printf("压缩前的字符串为:%s\n",t);
    }
    fclose(fin);
}
void fun(char t[])
{
    int i=0,k,j,p=0;
    char temp[100];
    while(t[i])
    {
        if(t[i]=='*' && i!=0)
        {
            k=0;j=i+1;
            while(isdigit(t[j]) && t[j])
            {
                ____2____;
                j++;
            }
            for(j=1;j<=k;j++)
                temp[p++]=t[i-1];
            ____3____;
        }
        else
            temp[p++]=t[i];
        i=i+1;
    }
    temp[p]='\0';
    ____4____;
}
```

要求：补全①②③④四处代码

### 2025年苏南五市职教高考计算机专业统测

### 73 题 C 语言程序阅读填空

阅读下列程序，填写①\-④对应内容

```c
#include<stdio.h>
int a=2;
int fun(int c)
{ 
    static int a=3; 
    c++; 
    return (a++)+c; 
} 
int main() 
{ 
    int i,k=0; 
    for(i=0;i<2;i++) 
    {
        int a=3; 
        k+=fun(a) ; 
        printf("%4d",k); 
    } 
    k+=a; 
    printf("%4d",k); 
    return 0; 
}
```

问题：
上述程序中，第 \(1\) 行以 \#开头的称为 ① 命令；第 \(2\) 行中 a 被定义为 ② 变量；程序从第 ③ 行开始执行，程序运行结果是 ④。

---

### 74 题 C 语言程序阅读写运行结果

```c
#include<stdio.h> 
main( ) 
{
    char s[]="\\BAD\x43!$DA@C&DI\0*ABD"; 
    int k; 
    char c; 
    for(k=1 ;(c=s[k])!='\0';k=k+2) 
    { 
        switch(c) 
        {
            case 'A':putchar('%');continue; 
            case 'B':++k;break; 
            default:putchar('*'); 
            case 'D':putchar('&');continue; 
        } 
        putchar('#'); 
    }
}
```

要求：写出程序运行结果

---

### 75 题 C 语言程序阅读写运行结果

```c
#include <stdio.h> 
#include <ctype.h> 
#define N 80 
fun(char s[ ]) 
{ 
    int i,j; 
    for(i=0,j=0;s[i]!='\0';i++) 
        if(s[i]>'z'||s[i]<'a'&&s[i]>'Z'||s[i]<'A') 
        { 
            s[j]=s[i]; 
            j++; 
            s[j]='\0'; 
            return(j); 
        } 
    return(i);
}
int main()
{
    char str[N]="Abc983*90df4"; 
    int i,s;
    puts(str);
    s=fun(str);
    for(i=0;i<s;i++)
        if(isdigit(str[i]))
            str[i]=str[i]<'7'?str[i]+3:str[i]-7; 
    printf("There are %d char in the new string:\n",s); 
    puts(str); 
    return 0;
}
```

要求：写出程序运行结果

---

### 76 题 C 语言程序填空完善

程序功能：由随机函数产生 30 个互不相同的 2 位整数放入 5\*6 数组；找出每行最大最小值；删除每行最大值；将每行最小值放在该行主对角线，保持数据相对位置不变，最后输出数组。补全程序空缺处。

```c
#include"stdio.h"
#include "stdlib.h"
#include"time.h"
int main()
{
    int b[30],a[5][6],i,j,t,max,min,p1,c=0;
    srand((unsigned)time(NULL));
    for(i=0;i<30;i++)
        b[i]=_1
    for(j=0;j<i;j++)
        if(b[j]==b[i])
        {i--;2
        }
    for(i=0;i<5;i++)
        for(j=0;j<6;j++)
            a[i][j]=b[c++];
    for(i=0;i<5;i++)
    { 
        for(j=0;j<6;j++)
        printf("n");
    }
    for(i=0;i<5;i++)
    {
        //求最大值和最小值
        max=a[i][0];p1=0;
        min=a[i][0];
        for(j=1;j<6;j++)
        { 
            if(a[i][j]>max)
            {max=a[i][j];p1=j;}
            if(a[i][j]<min)
            {min=a[i][j];}
        }
        printf("%d,%d\n",max,min);
        /*删除最大值*/ 
        for(j=p1;j<5;j++) 
        /*移动最小值到主对角线*/ 
        while( ④ )
        { 
            t=a[i][0]; 
            for(j=0;j<4;j++) 
                a[i][j]=a[i][j+1]; 
            a[i][j]=t; 
        }
    }
    for(i=0;i<5;i++) 
    { 
        for(j=0;j<5;j++) 
            printf("%d\t",a[i][j]); 
        printf("\n"); 
    }
}
```

要求：填写程序空缺②、④等位置代码

---

### 77 题 C 语言文件 \+ 背包算法程序填空

功能：从 d:\\input\.txt 读取物品重量、价值，背包限容量 100、物品不超 20 种，部分 / 完整选取物品使总价值最高，将选择结果写入 d:\\output\.txt 并输出总价值。补全程序。

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX_ITEMS 20
int main(){
    int values[MAX_ITEMS],weight[MAX_ITEMS],wp[MAX_ITEMS];
    int n=0;
    int c= 100;
    int total_weight=0,remain_c;
    int t1,x,t2;
    double total_value =0,cost_per[MAX_ITEMS],part_value;
    FILE *input, *output;
    input = fopen("d:\\input.txt", "r");
    if (input == NULL) { 
        printf("无法打开输入文件!\n"); 
        return ①; 
    } 
    while ( ② &&n<MAX_ITEMS) {
        fscanf(input, "%d", &weight[n]); 
        fscanf(input, "%d", &values[n]);
        cost_per[n]=(double)values[n]/weight[n]; 
        wp[n]=n+1;
        n++;
    }
    fclose(input);
    /*按单位重量的价值,进行降序排序*/
    for (int i=0;i<n-1; i++){
        for (int j=i+ 1;j<n;j++) {
            if(③){
                t1=wp[i],wp[i]=wp[j],wp[j]=t1;
                t2=cost_per[i],cost_per[i]=cost_per[j],cost_per[j]=t2;
            }
        }
    }
    output = fopen("d:\\output.txt", "w"); 
    if (output==NULL) { 
        printf("无法打开输出文件!\n"); 
        return 1; 
    }
    for (int i = 0; i < n; i++) { ④ ; 
        if (total_weight + weight[x] <= c) { 
            fprintf(output, "物品 %d - 重量: %d, 价值: %d\n", wp[i], weight[x], values[x]); 
            total_weight += weight[x]; 
            total_value += values[x]; 
        } else 
        { 
            remain_c= c-total_weight; 
            part_value= ④;
            fprintf(output, "物品 %d - 重量: %d, 价值: %.2f (部分)\n", wp[i], remain_c, part_value); 
            total_value += part_value; 
            break;
        }
    }
    fprintf(output, "\n 总价值:%.2f",total_value); 
    fclose(output); 
    printf("处理完成!\n"); 
    return 0;
}
```

要求：补全①②③④空缺内容

### 2025盐城市职教高考二模计算机专业试卷

### 73\. C 语言程序阅读题

```c
(1)#include <stdio.h> 
(2)#include <math.h> 
(3)#define N 3 
(4)double fact(int i) 
(5){ 
(6)int j; 
(7)double f=1.0; 
(8)for(j=2; j<=i; j++) 
(9) f=f*j; 
(10)return f; 
(11)} 
(12)double sumfact(int n) 
(13){ 
(14)int i; 
(15)double s=0.0; 
(16)for(i=1; i<=n; i++) 
(17) s=s+fact(i); 
(18)return s; 
(19)} 
(20)int main(void) 
(21){ 
(22)int n; 
(23)double sum; 
(24)sum=sumfact(N); 
(25)printf("1-%d 阶乘和的平方根=%.0f\n",N,sqrt(sum)); 
(26)}
```

问题：
①根据定义的位置，\(2\) 是\\*\\*\_\_头文件；
②函数`double fact\(int i\)`的功能是\\*\\*\\*\\*；
③\(18\) 句返回值的类型是\\*\\*\\*\\*；
④程序运行的结果是\\*\\*\\*\\*。

---

### 74\. C 语言程序阅读题

阅读下列程序，写出程序运行结果

```c
#include <stdio.h> 
#include <string.h> 
#include <ctype.h> 
#define flag 1 
int main() 
{
    char str[30]="2025 We meet\0every where!",c;
    int size=sizeof(str); 
    int i=0,num=0,other=0;
    printf("size=%d\n",size); 
    for(i=0;str[i];i++) 
        switch(isdigit(str[i])) 
        {
            case 1:num++; 
            case 0:other++; 
        } 
    printf("num=%d\nother=%d\n",num,other); 
    i=0;
    while((c=str[i])!='\0') 
    { 
        i++; 
#if flag 
#else 
        if(c>='a'&&c<='z') c=c-32; 
        if(c>='A'&&c<='Z') c=c+32; 
#endif 
        printf("%c",c); 
    }
    printf("\n");
}
```

---

### 75\. C 语言程序阅读题

阅读下列程序，写出程序运行结果

```c
#include "stdio.h" 
int judge (int x); 
int main() 
{
    int a[3][3]={24,45,11,26,18,54,61,16,18}; 
    int b[9]; 
    int i,j,k=0;
    for(i=0;i<3;i++) 
        for(j=0;j<3;j++) 
            if(judge(a[j][i])) 
                b[k++]=a[j][i]; 
    for(i=0;i<k;i++) 
        printf("%d\t",b[i]); 
}
int judge(int x) 
{
    if((x%10+x/10)%2==0)
        return 1; 
    else 
        return 0; 
}
```

---

### 76\. C 语言程序填空題

程序功能：选举优秀员工，录入 20 人投票，统计 4 人得票并从高到低排序输出

```c
#include "stdio.h" 
#include "string.h" 
#define N 4 
struct person {
    char stu_name[10]; 
    int count;
}; 
int main() { 
    int i,j,temp; 
    char nam[10]; 
    char monitor_name[10]; 
    ① tongji[N] ={"zhanghua",0,"zhaoming",0,"lijin",0,"wangpin",0};
    //输入20次投票姓名
    printf("请输入二十次得票各选手的姓名\n"); 
    for(i=1;i<=20;i++) 
        scanf("%s", ② );
    for(j=0;j<N;j++) 
        if(strcmp(monitor_name,tongji[j].stu_name)==0) 
            tongji[j].count++; 
    //由高到低排序 
    for(i=1;i<=N-1;i++) 
        for(j=0;j<=N-1-i;j++) 
            if( ③ )
            {
                temp=tongji[j].count; 
                tongji[j].count=tongji[j+1].count; 
                tongji[j+1].count=temp;
                strcpy(nam,tongji[j].stu_name); 
                strcpy(tongji[j].stu_name,tongji[j+1].stu_name); 
                strcpy(tongji[j+1].stu_name,nam);
            }
    //输出四人的得票数 
    for(i=0;i<N;i++) 
        printf("%s,%d\n",tongji[i].stu_name,tongji[i].count);
}
```

要求：补全①②③三处空缺代码

---

### 77\. C 语言程序填空題

功能：读取二进制文件 stud\_dat 中 10 个学生数据，读取单数学生信息并显示，求最高年龄

```c
#include <stdlib.h> 
#include <stdio.h> 
//定义结构体数组 
struct student_type 
{ 
    char name[10]; 
    int age; 
    char sex; 
}stud[10]; 

int main() 
{ 
    ① *fp; 
    int i,maxage; 
    //打开文件 
    if((fp=fopen("stud_dat","rb"))==NULL) 
    { 
        printf("cannot open file\n"); 
        exit(0); 
    }
    //按要求间隔读取数据 
    maxage=0;
    for(i=0;i<10;i+=2) 
    {  
        ② (fp,i*sizeof(struct student_type),0); 
        fread(&stud[i],sizeof( ③ ),1,fp); 
        printf("%s %d %c\n",stud[i].name,stud[i].age,stud[i].sex); 
        if(stud[i].age>maxage) 
            maxage=stud[i].age;
    }
    printf("maxage=%d",maxage);
}
```

要求：补全①②③三处空缺代码

### 2026 凤凰职教一模相关题目

### 73 题

阅读下列程序，请将①\~④处表示的内容填写在答题卡中的相应位置。

```c
#include <stdio.h>
int m=5,n=6,a[10]={0,1,2};
void fl(void);
void f2(int m);
void main()
{ 
    int i;
    for(i=0;i<7;i++) 
        fl(); 
        f2(1);
    printf("\n%d,%d",a[m],a[n]);
}
void fl(void)
{ 
    static int n=3;
    a[n]=a[n-1]+a[n-2]+a[n-3];
    n++;
}
void f2(int m)
{ 
    for(;m<3;m+=2)
    { 
        int m; 
        for(m=1;m<4;m++) 
            printf("%d,",a[m++]);
    }
}
```

问题：
上述程序中，根据定义的位置，变量 m,n 是 ① 变量；程序的第 \(3\)\(4\) 行称为 ② 语句；程序运行时，输出结果的第一行是 ③ ，第二行是 ④。

---

### 74 题

阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include <stdio.h>
void main()
{ 
    int k=3.7,m=0;
    int a=012,b=4;
    do
    { 
        switch(k--)
        { 
            case 1:
                switch(++m)
                { 
                    case 1:b++;continue;
                    default:a++;b++;
                    case 0:a+=2;break;
                }
            case 2: a--;
            default: a+=2;b++;
        }
    }while(k>=0);
    printf("a=%d,b=%d,m=%d\n",a,b,m);
}
```

---

### 75 题

阅读下列程序，请将运行结果写在答题卡对应的题号处。

```c
#include "stdio.h"
void main()
{ 
    int m1=0,m2=5,m3=-1,i,j,k;
    for(i=3;i>=0;i--) 
    { 
        m1=m1+i;
        m3++;
        for(j=1;j<=3;j++)
        { 
            m2++;m3--;
            for(k=-2;k<=j;k++)
                m1++;
            m3=-m3;
        }
        m2-=6-j;
        printf("m1=%d\tm2=%d\tm3=%d\n",m1,m2,m3); 
    }
}
```

---

### 76 题

下面程序中函数`strmerge\(\)`的功能是：合并两个有序的字母字符串 \(字典序\) a 和 b 产生一个新的字符串 c，合并过程中要求删除重复出现的字符，同时保证合并后的字符串仍然有序，函数返回合并过程中删除的重复字符的个数。`main\(\)`函数中输出合并后的字符串 “copy” 以及在合并过程中删除的字符个数 3。请将①\~④处的答案填写在答题卡对应的题号处。

```c
int strmerge(char a[],char b[],char c[]) { 
    #include<stdio.h> 
    int i=0,j=0,k=0;
    char t;
    while( ① )
    { 
        if(a[i]==b[j])
        { 
            t=a[i];
            ② 
        } 
        else if(a[i]<b[j])
            t=a[i++];
        else
            t=b[j++];
        if(t!=c[k-1])
            ③ 
    }
    while(a[i])
        if(a[i]!=c[k-1])
            c[k++]=a[i++];
        else
            i++;
    while(b[j])
        if(b[j]!=c[k-1])
            c[k++]=b[j++];
        else
            j++;
    c[k]='\0';
    return ④ ;
}
void main()
{ 
    char s1[10]="ccp",s2[10]="oppy",s3[20];
    int n;
    n=strmerge(s1,s2,s3);
    puts(s3); 
    printf("%d",n);
}
```

---

### 77 题

当前文件夹下的文本文件`file1\.txt`中存放了若干个用空格分隔的整数，程序先从该文件中读取全部数据存入到整型数组 a 中，然后对数组 a 进行升序排序，并把排序结果一次写入到 d 盘 score 文件夹下的二进制文件`file2\.dat`中。请将①\~⑥处的答案填写在答题卡上对应的题号处。

```c
#include <stdio.h>
#include <stdlib.h>
#define N 100
void insertsort(int x[],int num)//排序 
{
    int i,j,t;
    for( ① ;i--)
    { 
        j=i+1;
        t=x[i]; 
        while(j<num&&t>x[j]) 
        { 
            x[j-1]=x[j];
            ② 
        }
        x[j-1]=t;
    }
}
void main()
{ 
    int i,a[N],n=-1;
    FILE *fp1,*fp2;
    if((fp1=fopen("file1.txt","r"))==NULL)
    {
        printf("can't open file!");
        exit(0);
    }
    fp2= ③ ;
    //读取全部数据
    while(!feof(fp1))
    {
        ④ ;
        n++;
    }
    for(i=0;i<n+1;i++)
        printf("%d\t",a[i]);
    printf("\n"); 
    //调用排序算法
    ⑤ ;
    //将排序后的数据一次性写入文件
    for(i=0;i<n+1;i++)
        ⑥ ;
    fclose(fp1);
    fclose(fp2);
}
```

### 2026 凤凰职教二模

## 一、程序阅读填空题（73\~77 题 全为 C 语言）

### 73 题

阅读下列程序，请将 1\~4 表示的内容填写在答题卡上相应位置。

```c
(1) #include <stdio.h>
(2)#define A 5
(3) #define B (A+2) 
(4) #define C A+2 
(5) #define D C*3+B
(6) int main(void) 
(7) { int x=C*3,y=D*3;
(8) printf("x=%d,y=%d\n", x,y);
(9) return 0;
(10)}
```

问题：

1. 第 (1) 行中`<stdio.h>`两边的尖括号表示以__方式引入系统头文件；

2. 第 (2)~(5) 行的`define`是编译预处理中的__命令；

3. 其中 A、B、C、D 称为____；

4. 本程序的运行结果为____。

---

### 74 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(void)
{
    char a[][20]= {"sysTem","forEver","byte","viSual"};
    int i,j,s,n=sizeof(a)/sizeof(a[0]),b[10];
    for(i=0;i<n;i++)
    {
        s=0;
        for(j=0;a[i][j];j++) 
        {
            if(!islower(a[i][j]))
                continue;
            switch(a[i][j])
            {
                default:s=s+1;
                case 'a':case 'b':case 'c': s=s+2;break;
                case 'r':case 's':case 't': s=4;break;
            }
            s++;
        }
        b[i]=s;
    }
    for(i=0;i<n;i++)
        printf("%5d",b[i]);
    return 0;
}
```

---

### 75 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>
#define N 6
int funs(int n)
{ 
    int t=0;
    while(n)
    { 
        t+=n%10;
        n=n/10;
    }
    return t;
}
void fun(int a[])
{
    int i,j,t,si,sj;
    for(i=1;i<N;i++)
    { 
        si=funs(a[i]);
        for(j=0;j<i;j++)
        {
            sj=funs(a[j]);
            if(si>sj)
                t=a[i],a[i]=a[j],a[j]=t;
        }
    }
}
int main(void)
{ 
    int i,a[N]={43,35,67,12,18,50};
    for(i=0; i<N; i++)
        printf("%4d",a[i]);
    printf("\n");
    fun(a);
    for(i=0;i<N; i++)
    {
        printf("%4d",a[i]);
        if((i+1)%3==0)
            printf("\n");
    }
    return 0;
}
```

---

### 76 题

AI 学习知识点规律：第一天 1 个；接下来两天每天 2 个；再接下来三天每天 3 个…… 输入天数 n，求总知识点数。完善程序填空 1\~4。

```c
#include "stdio.h"
int study(int n)
{
    int s=0,sum=0,k=1;
    do
    { 
        s= ① ;
        sum+= ② ;
        k++;
    }while( ③ );
    sum=sum-(s-n)*(k-1);
    return sum;
}
int main(void)
{
    int y,n;
    printf("n=");
    scanf("%d",&n);
    if(n>0)
    { 
        y=study(n);
        printf("n=%d,y=%d\n",n,y);
    }
    else 
        printf("error!\n");
    return 0;
}
```

---

### 77 题

程序功能：从`f:\\ks\.txt`读取 6 个整数存入数组，求前 2 个、前 3 个… 前 6 个数的最大公约数之和，追加写入文件末尾。完善程序填空①\~⑥。

```c
#include "stdio.h"
main()
{
    int i,s,sum=0,a[6];
    FILE *fp= ① ;
    if(fp==NULL) 
    {
        printf("error");
        exit(0);
    }
    for(i=0;i<6;i++)
        ② ;
    s=a[0]; 
    for(i=1;i<6;i++)
    {
        ③ ;
        sum+=s;
    }
    fprintf(fp,"\n");
    fclose(fp);
}
int gcd(int x,int y)
{ 
    int r;
    while(y)
    { 
        ⑤ ;
        x=y;
        y=r;
    }
    ⑥ ;
}
```

### 2026 江苏省2026年中职职教高考冲刺阶段教学质量诊断分析

### 73 题

阅读下列程序，请将 1\~4 表示的内容填写在答题卡上相应位置。\(每空 3 分，共 12 分\)

```c
#include<stdio.h>
void adjust(int arr[],int len)
{
    int i,j;
    int temp;
    for (i=0;i<len;i++)
        if (arr[i]%2!=0)
            for (j=i+1;j<len;j++)
                if(arr[j]%2==0)
                {
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                    break;
                }
}
int main()
{
    int arr[]={3,1,4,6,5};
    int len=sizeof(arr)/sizeof(arr[0]);
    int i;
    adjust(arr,len);
    printf("调整后的数组为");
    for (i=0;i<len;i++)
        printf("%d ",arr[i]);
    return 0;
}
```

问题：
程序中第 20 行中的表达式主要作用是①；函数 adjust 主要实现功能②，其中的参数 arr 是按③传递；程序最后运行结果为④。

---

### 74 题

阅读下列程序、把运行结果填写在答题卡上相应位置。

```c
#include<stdio.h>
void fun(int j)
{
    extern int a,b;
    static int i=0;
    int c;
    b=j++; 
    c=i+j; 
    a=++i; 
    printf("c=%d,i=%d,j=%d\n",c,i,j);
}
int a=0,b=1;
int main()
{
    a=1;b=2;
    fun(b);
    fun(a); 
    printf("a=%d,b=%d\n",a,b);
    return 0;
}
```

---

### 75 题

阅读下列程序，把运行结果填写在答题卡上相应位置。

```c
#include<stdio.h> 
#include<string.h>
void fun(char s[])
{ 
    int i,j=0,k=0;
    char num[80],letter[80];
    for (i=0;s[i]!='\0';i++)
    {
        if(s[i]>='0' && s[i]<='9')
            num[k++]=s[i];
        else if (s[i]>='a'&&s[i]<='z'||s[i]>='A'&&s[i]<='Z')
            letter[j++]=s[i];
    }
    num[k]='\0'; 
    letter[j]='\0';
    strcat(num,letter);
    strcpy(s,num);
}
int main()
{
    char s[]="";
    fun(s);
    puts(s);
    return 0;
}
```

---

### 76 题

程序实现功能：从二进制文件`numbers\.bin`读取 15 个整数，去除重复值后，将去重结果重新写入该文件 \(覆盖原内容\)。请将 1\~4 表示的内容填写到答题卡上相应的位置。\(每空 3 分，共 12 分\)

```c
#include<stdio.h>
#include<stdlib.h>
int is_exist(int arr[],int len,int val)
{
    int i;
    for (i=0;i<len;i++)
        if (arr[i]==val) return 1;
    return 0;
}
int main()
{
    FILE *fp;
    int nums[15],unique[15];
    int i,k=0;
    fp=fopen("numbers.bin","rb");
    if(!fp)exit(1);
    fread(①);
    fclose(fp);
    //去重处理
    for (i=0;i<15;i++)
    {
        if (! is_exist(②))
            unique[k++]=③;
    }
    fp=fopen("numbers.bin","wb");
    fwrite(④);
    fclose(fp);
    return 0;
}
```

---

### 77 题

该程序的主要功能是将 10 进制字符 \&\#34;123456\&\#34; 转成 16 进制字符串 \&\#34;0x1E240\&\#34; 并输出。请将 1\~4 表示的内容填写到答题卡上相应的位置。\(每空 3 分，共 12 分\)

```c
#include<stdio.h>
#include<string.h>
#define N 1000
//10进制字符串除以16，返回余数
int decDiv16(char num[N])
{
    char quotient[N]={0};
    int q_len=0,remainder=0,i;
    //计算商和余数
    for (i=0;num[i]!='\0';i++)
    {
        int current= ① ;
        quotient[q_len++]=(current/16)+'0';
        remainder=current%16;
    }
    //去除商的前导0 ②
    int start=0;
    while (quotient[start]=='0' && start<q_len-1)
        start++;//找到第一个非0位置
    //将去除前导0后的商复制回原数组
    strcpy(num,quotient+start);
    return remainder;
}
int main()
{
    char dec[N]="123456";
    char hex[N]={0};
    int i,h_len=0;
    while (strcmp(dec,"0")!=0)
    {
        int rem=decDiv16(dec);
        hex[h_len++]= (rem<10)?(rem+'0'):(rem-10+'A');
    }
    //处理原数为0的情况
    if (h_len==0)
        hex[h_len++]='0';
    //逆序输出16进制结果
    printf("\n");
    printf("16进制=0x");
    for(i=h_len-1;i>=0;i--) 
        printf("%c",hex[i]);
    return 0;
}
```

### 2026 职教高考联盟

### 73 题

阅读下列程序，请将 1\~4 表示的内容填写在答题卡上相应位置。

```c
#include <stdio.h>
int main(void)
{
    char s[]="This is a C pro\0gram.";
    int k;
    char c;
    puts(s); 
    s[8]='\0';
    for(k=2;k<6;k++)
    { 
        switch(c=s[k])
        {
            case'i': printf("%s","FIL");
            case 's': ++k;break;
            default: puts("Users"); 
            case 'r': puts("include");
                continue;
        }
        printf ("%8s\n","Files");
    }
    return 0;
}
```

问题：
上述程序中，第 \(3\) 行中数组 s 在内存中的占用空间为\\*\\1\\\\字节；第 \(6\) 行中的字符串结束符 \&\#39;\\0\&\#39; 属于\\\\2\\\\字符；第 \(14\) 行 continue; 语句执行结束后，程序将继续执行第\\\\3\\\\行内容；第 \(16\) 行中 \&\#34;%8s\&\#34; 中的 8 用于指定输出数据的\\\\*。

---

### 74 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio. h>
int main(void)
{
    int i, j, arr1[8]={2, 4, 6, 8, 10}, arr2[8]={1, 3, 4,6, 9, 10, 12};
    for(i=0;i<5;i++)
        printf("%-3d", arr1[i]);
    printf("\n"); 
    for(j=0;j<7;j++) 
        printf("%-3d", arr2[j]);
    printf("\n");
    i=j=0;
    while(i<5 && j<7) 
    {
        if(arr1[i]<arr2[j])
            printf("%-3d", arr1[i++]);
        else if(arr1[i]>arr2[j])
            j++;
        else
            i++,j++;
    }
    while(i<5)
        printf("%-3d", arr1[i++]);
    printf("\n");
    return 0;
}
```

---

### 75 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio. h>
int a=3;
int fun(int a, int b)
{ 
    static int c;
    a=a+b;
    c+=b+a;
    b=a+c;
    return b;
}
int main(void)
{
    int c=5,d;
    d=fun (a++, fun (--a, c)); 
    printf("%d %d %d", a, c, d) ;
    return 0;
}
```

---

### 76 题

给定若干个仅由字符 A 和 B 组成的字符串 \(长度为 1\\80\)，计算出对应串的积分。请完善程序填空 1\\4。
积分规则：每个字符 A 的得分为目前连续出现 A 的个数；每个字符 B 的得分为 1 分 \(多个连续出现的 B 仅积 1 分\)。
例如：`\&\#34;AABBBABAAA\&\#34;`积分为 1\+2\+\(1\)\+1\+\(1\)\+1\+2\+3=12

```c
#include <stdio. h>
int count (char str[])
{
    int i=0, j, sum=0, t=1; 
    while (str[i])
    {
        if( ① )
        {
            t++;
            i++;
        }
        if(str[i++]=='B')
            sum = sum + 1;
        while( ② )
            i--;
        ③
    }
    return sum;
}
int main(void)
{
    int i;
    char str[3] [80]={"AABBBABAAA", "BAAA", "AABBBABB"};
    for(i=0;i<3;i++)
        printf("%s的积分为:%d\n",str[i], ④ );
    return 0;
}
```

---

### 77 题

程序功能：从键盘输入 N 个学生的姓名和语文、数学、英语三门课程成绩，求出三门课程的均分，并按均分降序排序后，将成绩表写入二进制文件 fd\.dat。完善程序填空 1\~4。

```c
#include <stdio. h>
#include <string.h>
#define N 3
#define LEN sizeof (STU)
typedef struct node
{ 
    char nam[10];
    int sc[3];
    float av;
}STU;

//按均分降序排序 
void sort (STU s[], int n)
{
    int i,j;
    for(i=0;i<N-1;i++)
        for(j=0;j<2;j++) 
            if(s[j].av<s[j+1].av)
                // 填空1 交换两个结构体
}

int main(void)
{
    int i,j;
    FILE *fout; 
    STU s[N];
    //输入学生信息并计算均分 
    printf("请输入%d个学生的姓名和语文、数学、英语三门课程成绩:\n",N);
    for(i=0;i<N;i++)
    {
        scanf("%s", s[i].nam); 
        s[i]. av=0;
        for(j=0;j<3;j++) 
        {
            scanf("%d", &s[i].sc[j]); 
            s[i].av+= ③ ;
        }
    }
    printf("\nBefore sort Data: \n"); 
    for(i=0;i<N;i++)
        printf("%s:%3d, %3d, %3d:%5.1f\n",s[i].nam, s[i].sc[0], s[i].sc[1],s[i].sc[2], s[i].av);
    
    //按均分降序排序
    sort(s, N);
    //显示排序后的结果
    printf("\nAfter sort Data: \n");
    for(i=0;i<N;i++)
        printf ("%s:%3d, %3d, %3d:%5.1f\n", s[i].nam, s[i]. sc[0], s[i].sc[1],s[i].sc[2], s[i].av);
    
    //写入二进制文件 
    fout=fopen("fd.dat","wb");
    for(i=0;i<N;i++)
        fwrite( ④ );
    fclose (fout);
    return 0;
}
```

### 2026年扬州市职业学校职教高考调研卷

## 五、程序阅读题（全为 C 语言题目，共 5 题，每题 12 分，共 60 分）

### 78 题

阅读下列程序，答案填写在答题卡相应位置。\(每空 3 分，共 12 分\)
题目：函数`sort\(int a\[\],int left,int right\)`对数组 a 中下标在`\[left,right\]`间的元素进行升序排序。
例如：当 sort 函数参数 left,right 的值分别为 2,5 时，程序运行结果是：
排序前:\-6 9 18 0 \-3 7 12 \-4
排序后:\-6 9 \-3 0 7 18 12 \-4

```c
(1)#include <stdio.h>
(2)#define N 8
(3)void sort(int a[],int left,int right)
(4){ int round,num,t;
(5) for(round=left;round<right;round++)
(6) for(num=left;num<right+left-round;num++)
(7) if(a[num]>a[num+1])
(8) { t=a[num];a[num]=a[num+1]; a[num+1]=t;}
(9)void print(int a[]) 
(10){int i;
(11) for(i=0;i<N;++i)
(12) printf("%4d",a[i]); printf("
"); }
(13)int main() 
(14){int s[N]={-6,9,18,0,-3,7,12,-4},i,t1=9;
(15)printf("排序前:");
(16)int *km=&t1,*km=t1; 
(17) print(s);
(18) sort(s,2,5); 
(19) printf("
排序后:");
(20) print(s);
(21) return 0;}
```

问题：
上述程序中，第 \(1\) 行中`\&lt;\&gt;`按照 1 方式查找，第 \(17\) 行中`sort\(s,2,5\)`为函数 2，s 为 3 参数，第 \(14\) `int \*km`含义为 4。

---

### 79 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。\(共 12 分\)

```c
#include<stdio.h> 
#define N4 
int main(){ 
    float a[N]; 
    char s[N][10]={"11.011","1101.101","1011.011","101.101"}; 
    int i,j; 
    float sum, suml, sum2, p, temp; 
    for(i=0;i<N;i++){ 
        sum=suml=sum2=0;
        j=0;
        while(s[i][j]){ 
            while(s[i][j]=='0'||s[i][j]=='1') 
                suml=suml*2+s[i][j++]-48;
            if(s[i][j]=='.')j++;
            p=0.5;
            while(s[i][j]=='0'||s[i][j]=='1'){ 
                sum2=sum2+(s[i][j++]-48)*p;
                p=p*0.5;
            }
            sum=suml+sum2;
            a[i]=sum; 
        }
    }
    if(sum!=0)
        for(i=0;i<N-1;i++) 
            for(j=0;j<N-1;j++) 
                if(a[j]>a[j+1]){ 
                    temp=a[j]; 
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
    for(i=0;i<N;i++) 
        printf("%.Of	",a[i]);
    return 0;
}
```

---

### 80 题

阅读下列程序，请将运行结果填写在答题卡上相应位置。\(共 12 分\)

```c
#include <stdio.h>
#include <ctype.h>
void apart(char a[])
{
    int i,sum,sign=1,s;
    i=sum=0;
    while(a[i])
        while(!isdigit(a[i]) && a[i])
        {
            sign=a[i]=='-'?-1:1;
            i++;
        }
        s=0;
        while(isdigit(a[i])) 
            s=s*10+a[i++]-'0';
        s=s*sign;
        if(s!=0){
            printf("%d	",s);
            sum+=s;
        }
    printf("
%d
",sum);
}
int main()
{
    char sour[100]={"a-+-23b--45c--78d-99e+-.12f"};
    apart(sour);
    return 0;
}
```

---

### 81 题

阅读下列程序，将有关问题的答案填写在题 81 答题处。\(每空 3 分，共 12 分\)
题目：将长度为 n 的字符串 str 看成一个首尾相连的环，这样从 str 的 n 个位置开始向后取 n 个字符，可以得到 n 个长度为 n 的字符串。程序找出这 n 个字符串中最小的字符串。

```c
#include<stdio.h>
#include<string.h>
#define N 10
int comp (char str[],int p, int q) {
    int i;
    for(i=0;i<N;i++)
        if(str[(p+i)%N]!= str[(q+i)%N])
            return ①
    return 0;
}
int main(){
    char str[2][N+1]={"CBSTIBSTUO", "FMQFJMPQS"};
    int i,j,min;
    for(i=0;i<2;i++){
        for(j=1;j<N;j++)
            if(comp(③))
                min=j;
        printf("%s起始位置为%d的字符串",str[i],min);
        for(j =0;j<N;j++) 
            printf("最小字符串
"); 
        putchar(④);
    }
    return 0;
}
```

---

### 82 题

阅读下列程序，将有关问题的答案填写在题 82 答题处。\(每空 3 分，共 12 分\)
题目：下列程序的功能是将一组用指数形式表示的实数转化为十进制形式表示的实数。
```text
12.123e-3---0.012123
-0.015e5---1500
3.141e2---314.1
-0.618e-2---0.00618
```
```c
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#define M 3
void change(double nums[][M], int length) {
    int i, j;
    for(i = 0; i < length; i++) {
        float base = 10, num = nums[i][0];
        if(nums[i][1] < 0)
            ①;
        for(j = 0; j < fabs(nums[i][1]); j++)
            num = num * base;
        nums[i][2] = num;
    }
}

int ext_num(char str[], double nums[][M]) {
    int i, len = 0;
    for(i = 0; str[i]; i++)
        if(isdigit(str[i])) {
            int sign = 1, j = 0;
            char temp[63];
            if(i>0&&str[i-1] == '-') sign = -1;
            while(isdigit(str[i]) || str[i] == '.'&&str[i])
                ②;
            temp[j] = 0;
            nums[len/2][len%2]= sign * atof(temp);
            //函数atof()功能：将指向字符串转换double型的值
            len++;
            i--;
        }
    return ③;
}

int main() {
    char num_table[] = "12.123e-3,-0.015e+5,3.141e+2,-0.618e-2";
    double nums[4][M];
    int i, length;
    length = ④;
    change(nums, length);
    for(i = 0; i < length; i++)
        printf("%10.3lfe%-2.0lf---%G
", nums[i][0], nums[i][1], nums[i][2]);
    return 0;
}
### 2026盐一调计算机专业试卷

### 73 题 C 语言程序阅读

阅读下列程序，将①\~④表示的内容填写在答题卡上相应位置。

```c
#include <stdio.h>
int cal1(int m, int n) 
{return (m - n) + (m * n);
}
int cal2(int x) 
{if (x > 10) {
return x/2;}
else 
{return x*3;
}
}
int g = 2;
int main() 
{int a = 7, b = 4, res1, res2, res3;
double f = 3.5;
res1 = cal1(a, b);
res2 = cal2(res1 + g);
res3 = res1 - res2 + (int)f;
printf("res1=%d,res2=%d\n", res1, res2);
printf("res3=%d,f=%.1f\n", res3, f);
return 0;
}
```

问题：
上述程序中有***①***个自定义函数；变量 g 可以在 ② 函数中使用；程序执行后，第（19）行输出内容为******③******，第（20）行输出内容为******④*****。

---

### 74 题 C 语言程序阅读

阅读下列程序，写出运行结果。

```c
#include <stdio.h>
int main() 
{
int x = 7, y = 3, z;
    char ch = 'A';
    printf("初始值：x=%d, ch=%c\n", x, ch);
    z = (x-- * ++y) % 5;
    ch = ch + z;
    printf("运算后：z=%d, ch=%c\n", z, ch);
    if (z > 2)     x = x + 5;
    else if (z == 2)    x = x - 3;
       else   x = x * 2;
    printf("x更新后：%d\n", x);
    printf("逻辑结果：%d\n", (x > 10) && (y < 5));
    return 0;
}
```

---

### 75 题 C 语言程序阅读

阅读下列程序，写出运行结果。

```c
#include <stdio.h>
int main() 
{
    int arr1[6] = {2, 8, 15, 20, 25, 30};
    int arr2[5] = {5, 15, 20, 28, 35};
    int i = 0, j = 0, count = 0, sum = 0;
for (; i < 4; i++) 
        printf("%4d ", arr1[i]);
    printf("\n");
    i = 0; 
while (i < 6 && j < 5) 
{
        if (arr1[i] == arr2[j]) 
         {  sum += arr1[i];
            count++;
            i++;
            j++;}
         else if (arr1[i] < arr2[j])  i++;
             else   j++;
    }
    printf("sum=%d\n", sum);
printf("count=%d\n", count);
int max;
if (i>=6)   printf("max:not in arr1\n");
    else  {max = arr1[i];
for (; i < 6; i++) 
       if (arr1[i] > max) max = arr1[i];   
          printf("max=%d\n", max);}
    return 0;
}
```

---

### 76 题 C 语言程序填空完善

足球联赛排名排序程序，补全①～④处代码。

```c
#include <stdio.h>
#include <string.h>
#define TEAM_NUM 13
#define DATA_COL 4
#define PLAYOFF_NUM 8

int strToInt(char str[]) 
{
    int num = 0;
for (int i = 0; str[i] != '\0'; i++) 
{
        if (str[i] >= '0' && str[i] <= '9') 
            num = num * 10 + (str[i] - '0');
    }
    return num;
}

void sortTeams(char teams[TEAM_NUM][DATA_COL][20], int n) 
{
    char temp[DATA_COL][20];
for (int i = 0; i < n - 1; i++) 
{
        for (int j = 0; j <    ①     ; j++) 
{   
            int score1 = strToInt(teams[j][1]);
            int score2 = strToInt(teams[j+1][1]);
            int goal1 = strToInt(teams[j][2]), lose1 = strToInt(teams[j][3]);
            int goal2 = strToInt(teams[j+1][2]), lose2 = strToInt(teams[j+1][3]);
            int net1 = goal1 - lose1, net2 = goal2 - lose2;
            if (score1 < score2)
{
                for(int k = 0; k < DATA_COL; k++)
{
strcpy(temp[k], teams[j][k]);
strcpy(teams[j][k], teams[j+1][k]);
strcpy(teams[j+1][k], temp[k]);} 
            }
 else if (score1 == score2) 
{    
                if (net1 < net2) 
{
                     for(int k = 0; k < DATA_COL; k++)
{
                        strcpy(temp[k], teams[j][k]);
                        strcpy(teams[j][k], teams[j+1][k]);
                        strcpy(teams[j+1][k], temp[k]);
                        }
                   }
 else if (net1 == net2) 
{  if (    ②     ) 
{      
                          for(int k = 0; k < DATA_COL; k++)
{   strcpy(temp[k], teams[j][k]);
                            strcpy(teams[j][k], teams[j+1][k]);
                            strcpy(teams[j+1][k], temp[k]);
                        }
                    }
                }
            }
        }
    }
}

int main() 
{
    char teams[TEAM_NUM][DATA_COL][20];
    FILE *fp = fopen("jifenbang.dat", "r");
if (fp == NULL) 
{
        printf("文件打开失败");
        return 1;
    }
for (int i = 0; i < TEAM_NUM; i++)
        fscanf(fp, "%s %s %s %s", teams[i][0], teams[i][1], teams[i][2], teams[i][3]);
    fclose(fp);
    sortTeams(     ③     ); 
    printf("晋级淘汰赛的8支城市队（名次从高到低）：\n");
for (int i = 0; i < PLAYOFF_NUM; i++) 
        printf("%d. %s\n",      ④     );
    return 0;
}
```

---

### 77 题 C 语言文件读写 \+ 排序查找程序填空

学生成绩读取、排序、查找程序，补全①\~④处代码。

```c
#include <stdio.h>
#include <stdlib.h>
#define MAX_STU 50

int main() 
{
    void sort_score(int id[], int total[], int n);
    int find_id(int id[], int n, int target_id);
    int id[MAX_STU], chinese[MAX_STU], math[MAX_STU], english[MAX_STU], total[MAX_STU];
    FILE *fp;
    int n = 0, target_id, pos;
if(     ①     ) 
{   printf("文件打开失败！\n");
        return 0;
    }
while(!feof(fp) && n < MAX_STU) 
{   fscanf(fp, "%d%d%d%d",      ②     );
        total[n] = chinese[n] + math[n] + english[n];
        n++;
    }
    fclose(fp); 
    sort_score(id, total, n);
    printf("请输入要查找的学生学号：");
    scanf("%d", &target_id);
    pos = find_id(id, n, target_id);
    if(pos != -1)
        printf("学号%d的总成绩为：%d\n", target_id,      ③     );
    else
        printf("未找到学号为%d的学生\n", target_id);
    return 0;
}

void sort_score(int id[], int total[], int n) 
{
    int i, j, temp_id, temp_total;
for(i = 0; i < n - 1; i++) 
{
        for(j = 0; j < n - i - 1; j++) 
{   if(     ④     ) 
{
                temp_total = total[j];
                total[j] = total[j+1];
                total[j+1] = temp_total;
                temp_id = id[j];
                id[j] = id[j+1];
                id[j+1] = temp_id;
            }
        }
    }
}

int find_id(int id[], int n, int target_id) 
{
for(int i = 0; i < n; i++) 
        if(id[i] == target_id)
            return i;
    return -1;
}
```

### 2026盐城市职教高考二模计算机试卷

## C 语言部分

本大题共 5 小题，每题 12 分，共 60 分，答案一律填写到答题纸上。

### 73. 函数定义与宏定义

题干：阅读下列程序，请将①~④表示的内容填写在答题卡上相应位置。

```c
(1) #include <stdio.h>
(2) #define NUM 10
(3) int add(int x, int y);
(4) int mul(int a, int b)
(5) {
    return a * b + NUM;
}
(6) }
(7) int main()
(8) {
    int x = 10, y = 20, res1, res2;
(9)     res1 = add(x, y);
(10)     res2 = mul(res1, y);
(11)     printf("res1=%d, res2=%d
", res1, res2);
(12)     return 0;
(13) }
(14) int add(int x, int y)
(15) {
    return x + y * NUM;
}
```

设问：

1. 上述程序中第（2）行的功能是：①
2. 对 `add` 函数的函数定义在第：② 行
3. 程序执行后，`res1` 的值为：③
4. `res2` 的值为：④

### 74. 循环与分支程序运行结果

题干：阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>

int main()
{
    int i, j, k = 0;
    char ch = 'X';
    printf("k=%d, ch=%c
", k, ch);

    for (i = 3;
    i > 0;
    i--)
    {
        for (j = 1;
        j <= i;
        j++)
        {
            k += i - j;
            ch = (ch - 'A' + 1) % 26 + 'A';
        }
    }

    printf("k=%d, ch=%c
", k, ch);

    int temp;
    if (k % 3 == 0)
        temp = k + 5;
    else if (k % 2 == 0)
        temp = k - 1;
    else
        temp = k * 2;

    printf("temp=%d
", temp);
    return 0;
}
```

### 75. 数组与循环程序运行结果

题干：阅读下列程序，请将运行结果填写在答题卡上相应位置。

```c
#include <stdio.h>

int main()
{
    int a[] = {
        5, 7, 4, 6, 8, 3}
        ;
        int b[2][3] = {
            {
                2, 4, 1}
                , {
                    3, 5, 2}
                }
                ;
                int i, j, n;

                for (i = 0;
                i < 6;
                i++)
                {
                    n = b[i / 2][i % 3] + a[i];
                    for (j = 1;
                    j <= 10;
                    j++)
                    {
                        if (j > n)
                            break;
                        if (j % 2 == 0)
                            continue;
                        printf("*");
                    }
                    printf("
");
                }

                return 0;
            }
```

### 76. 身份证号出生日期提取与年龄计算

题干：字符数组 `a` 中存放了 3 组身份证号，请提取出 3 组身份证号中的出生年月日，存放到整型数组 `b[3][3]` 中，每行分别按序存放年月日，计算到 2026 年 1 月 1 日时三人的实际年龄，最终输出出生日期、年龄。请在答题卡上写出①~④表示的内容以完善程序。

年龄计算规则：先减年份，生日未到年龄再减 1。

示例输出：

```text
第 1 个出生日期：2005 年 1 月 15 日 年龄：20 岁
第 2 个出生日期：2006 年 5 月 20 日 年龄：19 岁
第 3 个出生日期：2003 年 12 月 5 日 年龄：22 岁
```

```c
#include <stdio.h>

// 提取年月日，直接存入 b 的某一行
void getBirth(char id[18], int birth[3])
{
    int year = (id[6] - '0') * 1000
    + (id[7] - '0') * 100
    + (id[8] - '0') * 10
    + (id[9] - '0');
    int month = (id[10] - '0') * 10 + (id[11] - '0');
    int day = ①;

    birth[0] = year;
    birth[1] = month;
    birth[2] = day;
}

// 根据年月日计算并返回年龄
int calcAge(int birth[3])
{
    int year = birth[0];
    int month = birth[1];
    int day = birth[2];
    int age = ②;

    if (month > 1 || (③))
    {
        age--;
    }

    return age;
}

int main()
{
    char a[3][19] = {
        "320981200501151234",
        "320981200605206789",
        "320981200312055678"
    }
    ;
    int b[3][3], i, age;

    for (i = 0;
    i < 3;
    i++)
    {
        getBirth(a[i], b[i]);
    }

    for (i = 0;
    i < 3;
    i++)
    {
        age = ④;
        printf("第%d个出生日期：%d年%d月%d日 年龄：%d岁
",
        i + 1, b[i][0], b[i][1], b[i][2], age);
    }

    return 0;
}
```

### 77. 文件读取与按进货总价排序

题干：在 D 盘根目录下，有一个名为 `123.txt` 的文件，文件中有 20 条商品的信息，每条信息包括商品名称、进货单价、进货量。从文件中读取所有商品信息，按每种商品进货总价升序排序后，输出进货价最高的三种商品的名称及进货总价。请完善代码中①~④处内容。

```c
#include <stdio.h>
#include <string.h>
#define N 20

// 按进货总价升序排序
void bubbleSort(char name[][50], float data[][3], int n)
{
    int i, j;
    float tempData[3];
    // 临时存放 单价、数量、总价
    char tempName[50];
    // 临时存放名称

    for (i = 0;
    i < n - 1;
    i++)
    {
        for (j = 0;
        j < n - 1 - i;
        j++)
        {
            if (①)
            {
                strcpy(tempName, name[j]);
                strcpy(name[j], name[j + 1]);
                strcpy(name[j + 1], tempName);

                tempData[0] = data[j][0];
                tempData[1] = data[j][1];
                tempData[2] = data[j][2];

                data[j][0] = data[j + 1][0];
                data[j][1] = data[j + 1][1];
                data[j][2] = data[j + 1][2];

                data[j + 1][0] = tempData[0];
                data[j + 1][1] = tempData[1];
                data[j + 1][2] = tempData[2];
            }
        }
    }
}

int main()
{
    char name[N][50];
    // 商品名称
    float data[N][3];
    // 二维浮点数组：分别存放单价、数量、总价
    FILE *fp;
    int i;

    if ((②) == NULL)
    {
        printf("文件打开失败！
");
        return 1;
    }

    for (i = 0;
    i < N;
    i++)
    {
        fscanf(fp, "%s %f %f", name[i], &data[i][0], &data[i][1]);
        data[i][2] = data[i][0] * data[i][1];
    }

    fclose(fp);
    bubbleSort(③);

    printf("进货总价最高的三种商品：\n");
    for (④;
    i < N;
    i++)
    {
        printf("名称：%s\t进货总价：%.2f\n", name[i], data[i][2]);
    }

    return 0;
}
```
