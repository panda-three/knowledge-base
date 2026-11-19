/*-------------------------------------------------------
【程序设计】
---------------------------------------------------------
题目：有一个形如"Li89,92,  Sun,99－85,  Zhang;84  83Bao94 77"的字符串，
      字符串中字母为学生的名字，数字为该学生对应的语文、数学的成绩，编程
      将这个字符串的学生姓名字符取出放在name数组中，再把各科成绩取出放在
      二维数组a的前两列中。并计算出语文数学成绩的总分放置在数组a的第三列
      中，最后按总分降序排序。

程序运行结果如下：
原始成绩列表为：
          Li:  89  92  181
         Sun:  99  85  184
       Zhang:  84  83  167
         Bao:  94  77  171

排序后成绩列表为：
        Sun:  99  85  184
         Li:  89  92  181
        Bao:  94  77  171
      Zhang:  84  83  167
 
1.编写函数int abstract(char name[][15], int a[][3], char st[] ), 根据题目
  要求将字符串st中的学生姓名取出放在name数组中，两门成绩取出放在a数组前两列，
  计算两门课成绩的总分放在数组a的第三列，函数返回学生的人数。

2.编写函数void sortindex(int a[][3], int p[], int n)，根据数组a中n个同学
  第三列的成绩总分进行降序排序，排序时要求只改变存放学号的数组p,不改变数组a
  的顺序。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
---------------------------------------------------------*/
#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#define N 10
int abstract(char name[][15], int a[][3], char st[] )
{
/**********Program**********/
     int i;
     int cnt=0;
     int n=0;
	 for(i=0;st[i];i++){
	 	if(isalpha(st[i])){
	 		int k=0;
	 		char temp[15];
	 		for(;st[i]&&isalpha(st[i]);i++){
	 			 temp[k++]=st[i];
			}
			temp[k]='\0';
			strcpy(name[cnt++],temp);
		}
		
		if(isdigit(st[i])){
	 		int y=0;
	 		for(;st[i]&&isdigit(st[i]);i++){
	 			 y=y*10+st[i]-'0';
			}
		    a[n/2][n%2]=y;
		    n++; 
		}
	 }  
	 for(i=0;i<cnt;i++)
         a[i][2]=a[i][0]+a[i][1];
     return cnt;

/**********  End  **********/
}
void sortindex(int a[][3], int p[], int n)
{
/**********Program**********/
    int i,j;
	for(i=0;i<n-1;i++){
		for(j=0;j<n-1-i;j++){
			if(a[j][2]<a[j+1][2]){
				int temp;
				temp=p[j];
				p[j]=p[j+1];
				p[j+1]=temp;
			}
		}
	} 




/**********  End  **********/
}
int main()
{
    char st[200]={"Li89,92,  Sun,99－85,  Zhang;84  83Bao94 77"};
    char name[N][15];
    int score[N][3], p[N] ;
    int i,j,k;
    FILE *fp;
    if((fp=fopen("DATA.DAT","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    k=abstract(name, score, st);
    printf("\n原始成绩列表为：\n");
    for(i=0;i<k;i++)
    {
        p[i]=i;
        printf("%15s:", name[i]);
        fprintf(fp,"%s:", name[i]);
        for(j=0;j<3;j++)
        {
             printf("%4d",score[i][j]);
             fprintf(fp, "%d,",score[i][j]);
        }
        fprintf(fp,"\n");
        printf("\n");
    }
    printf("\n排序后成绩列表为：\n");
    sortindex (score,p,k);
    for(i=0;i<k;i++)
    {
        printf("%15s:", name[p[i]]);
        fprintf(fp,"%s:",name[p[i]]);
        for(j=0;j<3;j++)
        {
            printf("%4d",score[ p[i] ][j]);
            fprintf(fp, "%d,",score[ p[i] ][j]);
        }
        fprintf(fp,"\n");
        printf("\n");
    }
    printf("\n");
    fclose(fp);
    return 0;
}

