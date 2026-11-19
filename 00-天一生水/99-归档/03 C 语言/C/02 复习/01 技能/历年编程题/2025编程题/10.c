/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：已知一元二次方程ax^2+bx+c=0在区间[p,q]中有一个根，一元二次方程的
      系数a、b、c，以及p和q的值依次存储在一个以空格分隔的字符串str中，
      编写程序，分别从str中取出a、b、c、p和q的值，然后求出该方程在区间[p,q]
      的根(精确到小数点后2位)。

注意：str中存储的数值字符串或为整数或为小数形式的浮点数。
    
程序运行结果是：
取到的5个数分别是：
2.300  -7.520  4.630  -1.000  1.370
方程在区间[-1.000,1.370]的根是0.82

1.编写函数void getNumber(char s[], double fnum[])，从s中取出a、b、c、p和q
  的值依次保存在fnum中。

2.编写函数double find(double fnum[])，将fnum前3个元素作为一元二次方程的
  系数，后2个元素作为区间，并在该区间中求出该一元二次方程的根。函数返回该根。  
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

void getNumber(char s[], double fnum[]) 
{
/**********Program**********/
    int i;
    int cnt=0;
    for(i=0;s[i];i++){
    	if(s[i]!=' '){ //起始 
    	    char temp[10];
    	    int k=0;
    		for(;s[i]&&s[i]!=' ';i++){
    			temp[k++]=s[i];
			} 
			if(k>0){
				temp[k]='\0';
				double num=atof(temp);
				fnum[cnt++]=num;
			}
		}
	}

/**********  End  **********/
}

double find(double fnum[]) 
{
/**********Program**********/




/**********  End  **********/
}

int main() 
{
    char s[]=" +2.3 -7.52   4.63  -1  1.37";    
    int i;
    double fnum[5],root;
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("File open error\n"), exit(0);
    }   
    getNumber(s,fnum);
    printf("取到的5个数分别是：\n"); 
    for(i=0; i<5; i++)
    {
        printf("%.3lf  ",fnum[i]);
        fprintf(fp,"[%.3lf]",fnum[i]);
    }    
    root = find(fnum);
    printf("\n方程在区间[%.3lf,%.3lf]的根是%.2lf\n",fnum[3],fnum[4],root);     
    fprintf(fp,"{%.2lf}\n",root);     
    fclose(fp);
    return 0;
}
