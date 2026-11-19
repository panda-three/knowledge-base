/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：程序将字符型数组str中形如为" 2/1  3/2  5/3  8/5  13/8  "字符串视为
      无穷分数数列前5项。将这些字符形式的分数，转换为整型分子、分母，存放
      在二维数组中。并根据该数列的前5项，计算出该数列的后5项，并计算该数列
      前10项和。

程序运行结果如下：
2/1
3/2
5/3
8/5
13/8
21/13
34/21
55/34
89/55
144/89
sum=16.47991

1.编写函数void change(int fb[][2],char str[])，将str中形如为
  "  2/1  3/2  5/3  8/5  13/8  "字符串视为无穷分数数列前5项
  （分数字符串之间由若干个空格间隔）。函数将字符型的分子、分母
  转换为正整数，存放在二维数组fb中，分子存放在fb的第一列，分母
  存放在fb的第二列。
2.编写函数double cal(int fb[][2])，根据数列前5项的规律，计算
  数列第6项到第10项，函数返回该数列前10项的和。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

void  change(int fb[][2],char str[])
{
/**********Program**********/
    int i;
    int n=0;
    for(i=0;str[i];i++){
    	if(isdigit(str[i])){
    		int y=0;
    		for(;str[i]&&isdigit(str[i]);i++){
    		    y=y*10+str[i]-'0';	
			}
			fb[n/2][n%2]=y;
			n++;	
		}
	}



/**********  End  **********/
}
double cal(int fb[][2])
{
/**********Program**********/
     int i;
	 for(i=5;i<10;i++){
	 	fb[i][0]=fb[i-1][0]+fb[i-1][1];
	 	fb[i][1]=fb[i-1][0];
	 } 
     double sum=0.0;
     for(i=0;i<10;i++){
     	sum=sum+(double)fb[i][0] / fb[i][1];
	 }

     return sum;
/**********  End  **********/
}
int main()
{
	
    char str[]=" 2/1 3/2 5/3 8/5 13/8  ";
    int i,fb[10][2];
    double fbsum;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    change(fb,str);
    for(i=0;i<5;++i)
    { 
        printf("%d/%d\n",fb[i][0],fb[i][1]);
        fprintf(fp,"[%d/%d]\n",fb[i][0],fb[i][1]);
    } 
    fbsum=cal(fb);
    for(i=5;i<10;++i)
    {
        printf("%d/%d\n",fb[i][0],fb[i][1]);
        fprintf(fp,"[%d/%d]\n",fb[i][0],fb[i][1]);
    }
    printf("sum=%.5lf\n",fbsum);
    fprintf(fp,"%.5lf\n",fbsum);
fclose(fp);
return 0;
}

