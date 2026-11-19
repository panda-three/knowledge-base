/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：数码单词是指由数字与字母构成的单词，例如"1T3h279e"就是一个数码单词。
      字符串str中存放用空格间隔的数码单词和非数码单词。程序实现两个功能：
      1．从str中找出第1个最长数码单词；
      2．提取str中每个数码单词中的数字字符，并按其在数码单词中的原有顺序
         组成一个新的整数。

测试数据：  "  1T3h9e 27C89 3Pro7gram 42is59 Beaut0iful administrator 1234567"
程序运行结果如下： 
第1个最长数码单词是: Beaut0iful, 其长度=10
共得到5个整数:       139    2789      37    4259       0
   
1．编写函数int sLoc(char str[])，功能是返回str[]中第1个最长数码单词的起始下标。
2．编写函数int getNum(char str[],int n[])，功能是将str[]中每个数码单词中的数字
   字符，转换成一个整数，保存在n[]中，函数返回n[]中整数个数。 

---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define M 4
#define N 80

int sLoc(char str[])
{
/**********Program**********/
   int i;
   int max_len=0;
   int start=0;
   for(i=0;str[i];i++){
   	   if(str[i]!=' '){
   	   	   int m=i;
   	   	   int len=0;
   	   	   //标志位思想 用来判断是否为数码单词，因为题目针对的是数码单词 
   	   	   int flag1=1;
   	   	   int flag2=1;
   	   	   for(;str[i]&&str[i]!=' ';i++){
   	   	   	   if(isalpha(str[i])){
   	   	   	   	    flag1=0;
			   }
			   if(isdigit(str[i])){
   	   	   	   	    flag2=0;
			   }
   	   	   	   len++;
		   }
		   if(flag1==0&&flag2==0){
		   	   if(len>max_len){
		   		    max_len=len;
		   	  		start=m;
			   }
		   }
	   }
   }

   return start;

/**********  End  **********/
}

int getNum(char str[],int n[])
{
/**********Program**********/
   int i;
   int cnt=0;
   for(i=0;str[i];i++){
   	   if(str[i]!=' '){
   	   	   int flag1=1;
   	   	   int flag2=1;
   	   	   int y=0;
   	   	   for(;str[i]&&str[i]!=' ';i++){
   	   	   	   //标志位思想 用来判断是否为数码单词，因为题目针对的是数码单词 
   	   	   	   if(isalpha(str[i])){
   	   	   	   	    flag1=0;
			   }
			   if(isdigit(str[i])){
   	   	   	   	    flag2=0;
   	   	   	   	    //注意：如果为数字，则才需要做拼接 
   	   	   	   	    y=y*10+str[i]-'0';
			   }
		   }
		   if(flag1==0&&flag2==0){
		   	   n[cnt++]=y;
		   } 
		  
	   }
   }

   return cnt;


/**********  End  **********/
}

int main(void)
{
    FILE *fp;
    char str[]= "  1T3h9e 27C89 3Pro7gram 42is59 Beaut0iful administrator 1234567";
    int i=0,n=0,sp=0;
    int number[N];
    if((fp=fopen("DATA.dat","w+"))==NULL) 
    {
        printf("File open error\n");
        exit(0);
    }
    sp=sLoc(str);
    printf("第1个最长数码单词是: "); 
    i=0;
    while(str[sp+i]!=32)
    {
        putchar(str[sp+i]);
        fputc(127+str[sp+i],fp);
        i++;        
    }
    printf(", 其长度=%d\n",i);
    fprintf(fp," ; 其长度=%d\n",i);
    n=getNum(str,number);
    printf("共得到%d个整数:  ",n);
    fprintf(fp,"共%d个整数: ",n);
    for(i=0;i<n;i++)
    {
        printf("%8d",number[i]);
        fprintf(fp,"%-8.2f",sqrt((double)number[i]));
    }
    printf("\n");
    fprintf(fp,"\n");
    fclose(fp);
    return 0;  
}
