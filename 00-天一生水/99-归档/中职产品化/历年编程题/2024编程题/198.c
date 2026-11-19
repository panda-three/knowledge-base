/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：有NUM位同学(学号从1-8)选修了COUR门课程，选修情况存放在一维整型
      数组cour中，程序统计每个学生选修课程的门数，并按照选修课程门数降序
      排序。

cour中数据及含义如下：
134567,1347,145678,34678,12345678
第一个整数134567表示学号1,3,4,5,6,7六位同学选修了第一门课程；
第二个整数1347表示学号1,3,4,7四位同学选修了第二门课程;余类推。

程序运行结果如下：
选修
学号：1  2  3  4  5  6  7  8
门数：4  1  4  5  3  4  5  3
排序
学号：4  7  1  3  6  5  8  2
门数：5  5  4  4  4  3  3  1

1.编写函数void cal(int study[][NUM+1],int cour[])，根据cour中数据统计每个
  学生选修课程门数，存放在study[1]中相应位置（study[0]中已存放了学生学号）。
2.编写函数void sort(int study[][NUM+1])，对study中学生选修课程门数降序排序，
  如选修课程门数相同，则按学号升序排序。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define COUR 5
#define NUM 8

void cal(int study[][NUM+1],int cour[])
{
/**********Program**********/
     int count[9]={0};
     int i;
     for(i=0;i<COUR;i++){
     	int temp=cour[i];
     	while(temp){
     		count[temp%10]++;
     		temp=temp/10;
		}
	 }
     for(i=1;i<=8;i++){
     	 study[1][i]=count[i];
	 }
/**********  End  **********/
}

void sort(int study[][NUM+1])
{
/**********Program**********/
    int i,j;
    for(i=1;i<8;i++){
    	for(j=1;j<=8-i;j++){
    		if(study[1][j]<study[1][j+1]){
    			int temp=study[1][j];
    			study[1][j]=study[1][j+1];
    			study[1][j+1]=temp;
    			
    			int temp1=study[0][j];
    			study[0][j]=study[0][j+1];
    			study[0][j+1]=temp1;
			}else if(study[1][j]==study[1][j+1]){
				if(study[0][j]>study[0][j+1]){
						int temp=study[1][j];
		    			study[1][j]=study[1][j+1];
		    			study[1][j+1]=temp;
		    			
		    			int temp1=study[0][j];
		    			study[0][j]=study[0][j+1];
		    			study[0][j+1]=temp1;
				}
			}
		}
	}
/**********  End  **********/
}
int main(void)
{
    int i,j;
    int cour[COUR]={134567,1347,145678,34678,12345678};
    int study[2][NUM+1]={{0,1,2,3,4,5,6,7,8}};
    char item[2][10]={"学号:","门数:"};
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    cal(study,cour);
    printf("选修\n");
    for(i=0;i<2;i++)
    {
        printf("%s ",item[i]);
        for(j=1;j<=NUM;++j)
        {
            printf("%3d ",study[i][j]);
            fprintf(fp,"%d ",study[i][NUM-j+1]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    sort(study);
    printf("排序\n");
    for(i=0;i<2;i++)
    {
        printf("%s ",item[i]);
        for(j=1;j<=NUM;++j)
        {
            printf("%3d ",study[i][j]);
            fprintf(fp,"%d ",study[i][NUM-j+1]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    fclose(fp);
    return 0;
}

