/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：计算一次歌唱比赛参赛选手的得分。假设有N个裁判给参赛选手打分（分值
      在[0,10]之间）。选手得分计算方法为：去掉一个最高分和一个次高分，
      再去掉一个最低分和一个次低分，所剩分数的平均分作为该参赛选手的
      最后得分。

程序运行结果如下：
 9.47,  9.56,  9.96, 10.00,  9.75,  9.78,  9.95,  9.86,  9.82,  9.18,
 9.00,  9.05,  9.87,  9.54,  8.99,  9.79, 10.00,  9.93,  9.62, 10.00,
 9.88, 10.00,  9.45,  9.75,  9.83,  9.00,  9.04,  8.97,  9.28,  9.98,

选手最终得分为：
9.79
9.63
9.54

1、编写函数void abstract(char a[][80], int n, double num[][N]), 
   数组a中存放有n个选手由N个裁判所打的得分组成的字符串，将每行字符串
   中N个得分取出分别存入数组num中。

例如：a数组字符串第一行为：
      "9.47,9.56,9.96,10.00,9.75,9.78,9.95,9.86,9.82,9.18"
      则存入数组num中的分数第一行为：
       9.47,9.56,9.96,10.00,9.75,9.78,9.95,9.86,9.82,9.18

2、编写函数void getscore(double num[][N], double score[], int n)，
   将数组num中n个选手的N个得分按上述方法计算每一个参赛选手的最后得分，
   并将最终得分对应存入数组score中。

-------------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
------------------------------------------------------------------------*/
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

#define N 10

void abstract(char a[][80], int n, double num[][N])
{
/**********Program**********/
    int i,j,k;
    for(i=0;i<3;i++){
    	char b[80];
    	int cnt=0;
    	strcpy(b,a[i]);
    	for(j=0;b[j];j++){
    	    if(b[j]!=','){
    	    	char temp[10];
    	    	k=0;
    	    	for(;b[j]&&b[j]!=',';j++){
    	    		temp[k++]=b[j];	
				}
				double d=atof(temp);
				num[i][cnt++]=d;
			}
		}
	}
/**********  End  **********/
}
void getscore(double num[][N], double score[], int n)
{
/**********Program**********/
   int i,j,cnt=0;
   for(i=0;i<n;i++){
   	    double min=num[i][0];
   	    double min1=num[i][0];
   	    double max=num[i][0];
   	    double max1=num[i][0];
   	    double sum=0.0;
   	    for(j=0;j<N;j++){
   	    	if(num[i][j]<min){
   	    		min1=min;
   	    		min=num[i][j];
			}else if(num[i][j]<min1){
				min1=num[i][j];
			}  
			 
   	    	if(num[i][j]>max){
   	    		max1=max;
   	    		max=num[i][j];
			}else if(num[i][j]>max1){
				max1=num[i][j];
			}
   	    	sum=sum+num[i][j];
		}
		double avg=(sum-max-min-max1-min1)/(N-4);
		score[cnt++]=avg;
   }



/**********  End  **********/
}
int main(void)
{
    char a[3][80]={ "9.47,9.56,9.96,10.00,9.75,9.78,9.95,9.86,9.82,9.18",
               "9.00,9.05,9.87,9.54,8.99,9.79,10.00,9.93,9.62,10.00",
               "9.88,10.00,9.45,9.75,9.83,9.00,9.04,8.97,9.28,9.98"};
    double num[3][N],s[3];
    int i,j;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
         printf("File open error\n");
         exit(0);
    }
    abstract(a, 3, num);
    getscore(num,s,3);
    for(i=0;i<3;i++)
    {
        for(j=0;j<N;j++)
        {
            printf("%6.2f,",num[i][j]);
            fprintf(fp, "%6.2f",num[i][j]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    printf("\n选手最终得分为：\n");
    for(i=0;i<3;i++)
    {
        printf("%.2f\n",s[i]);
        fprintf(fp, "%.2f\n",s[i]);
    }
    printf("\n");
    fclose(fp);
    return 0;
}

