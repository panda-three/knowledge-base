/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：有3位以上男女生参加技能比赛，比赛成绩各不相同。按比赛成绩取前3名。
      但前3名中必须同时有男、女生。如果前3名都是男生，则用成绩最好的一名
      女生取代第3名男生。如果前3名都是女生，则用成绩最好的一名男生取代
      第3名女生。相关比赛数据保存在一维整型数组score中。其中第1个数据是
      参赛人数，其后数据是每位参赛学生的成绩、学号、性别组成的一个正整数。

score中8个数据及含义如下：
7  8811  10020  8531  9640  9350  9060  8671

第1个正整数7表示有7位学生参加了比赛。其后7个正整数，每个正整数包含3部分信息：
个位表示学生性别(0表示女生，1表示男生)；十位表示学号(学号各不相同)；剩余的高
2位或高3位是比赛成绩。

例如：8811表示1号男生成绩88；10020表示2号女生成绩100。

程序运行结果如下：
成绩/学号性别
100/20 96/40 93/50 90/60 88/11 86/71 85/31
获奖学生
学号   性别
  2     女
  4     女 
  1     男

1.编写函数void sort(int score[])，对一维数组score中的学生比赛成绩进行降序排序。
  比赛成绩各不相同。

2.编写函数void rewards(int rwd[],int score[])，根据score中的成绩以及上述取前3名
  的规定，确定前三名获奖学生，保存在rwd中。rwd只保存学号和性别数据，不保存成绩
  数据。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void sort(int score[])
{
/**********Program**********/
    int i,j;
    for(i=1;i<7;i++){
    	for(j=1;j<8-i;j++){
    		//去掉后几位n  /10^n 
    		//得到后几位n  %10^n
    		int temp1=score[j]/100;
    		int temp2=score[j+1]/100;
    		if(temp1<temp2){
    			int temp=score[j]; 
				score[j]=score[j+1];
				score[j+1]=temp; 
			}
		}
	}



/**********  End  **********/
}
void rewards(int rwd[],int score[])
{
/**********Program**********/
     int first=score[1];
     int second=score[2];
     int three=score[3];
     int sex1=first%10;
     int sex2=second%10;
     int sex3=three%10;
     if(sex1==0&&sex2==0&&sex3==0){
     	  int i;
     	  for(i=4;i<=7;i++){
     	  	  if(score[i]%10==1){
     	  	  	   int temp;
     	  	  	   temp=score[3];
     	  	  	   score[3]=score[i];
     	  	  	   score[i]=temp;
     	  	  	   break;
			  }
		  }
	 }
	 if(sex1==1&&sex2==1&&sex3==1){
     	  int i;
     	  for(i=4;i<=7;i++){
     	  	  if(score[i]%10==0){
     	  	  	   int temp;
     	  	  	   temp=score[3];
     	  	  	   score[3]=score[i];
     	  	  	   score[i]=temp;
     	  	  	   break;
			  }
		  }
	 }
     rwd[0]=score[1]%100;
     rwd[1]=score[2]%100;
     rwd[2]=score[3]%100;


/**********  End  **********/
}
int main(void)
{
    int i;
    int score[8]={7,8811,10020,8531,9640,9350,9060,8671};
    int rwd[3];
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    sort(score);
    printf("成绩/学号性别\n");
    for(i=1;i<=score[0];i++)
    {
        printf("%4d/%2d ",score[i]/100,score[i]%100);
        fprintf(fp,"%d/%d ",score[i]%100,score[i]/100);
    }
    printf("\n");
    fprintf(fp,"\n");
    rewards(rwd,score);
    printf("获奖学生\n");
    printf("学号 性别\n");
    for(i=0;i<3;i++)
    {
        printf("%3d  %s\n",rwd[i]/10%10,rwd[i]%10==0 ?"女":"男" );
        fprintf(fp,"%s%d\n",rwd[3-i-1]%10==0 ? "女":"男",rwd[3-i-1]/10%10);  
    }
    fclose(fp);
    return 0;
}
