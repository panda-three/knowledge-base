/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：已知一维字符数组s中存放由若干空格分隔的连续子串，提取连续子串中的
      数字字符，按其在子串中的顺序拼成纯数字子串存入二维数组str中，对二维
      数组中数字子串进行某种排序，使得排序后的数字子串按照从前向后的顺序
      组合成的"长数字串"所表示的整数最大。数字子串必需作为一个整体参与组合。

提示：排序时，可以将两子串前后拼合再比较大小，以便确定是否要交换两子串。
 
程序运行结果如下：

原始串为：
 ab9a3ds  ab9r   mn79a pm9s1d
提取的数字子串为：
93  9  79  91
可以拼接的最大整数为：
9939179

1.编写函数int tqszc(char s[],char str[][10]), 从s串中提取由空格分隔的纯
数字子串，存入二维数组str中，函数返回数字子串的个数。

2.编写函数void Sort(char str[][10],int n)，将str中的n个数字子串进行
排序，使之按序输出即可拼合出最大的整数。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int tqszc(char s[],char str[][10])
{
/**********Program**********/
   int i;
   //遍历字符串 
   char temp[10];
   int cnt=0; 
   while(s[i]){
   	  if(s[i]!=' '){
   	  	//提取 
   	  	int k=0;
   	  	while(s[i]&&s[i]!=' '){
   	  		//判断是否为数字
			if(isdigit(s[i])){
				temp[k++]=s[i];
			} 
			i++;
		}
		//存二维数组
		if(k>0){
			temp[k]='\0';
			strcpy(str[cnt],temp);
			cnt++;
		} 
	  } else{
	  	 i++;
	  } 
   } 

  return cnt;
/**********  End  **********/
}
void Sort(char str[][10],int n)
{
/**********Program**********/
   int i,j;
   for(i=0;i<n-1;i++){
   	  for(j=0;j<n-1-i;j++){
   	  	 char ab[20];
   	  	 strcpy(ab,str[j]);
   	  	 strcat(ab,str[j+1]);
   	  	 
   	  	 char ba[20];
   	  	 strcpy(ba,str[j+1]);
   	  	 strcat(ba,str[j]);
   	  	 
   	  	 if(strcmp(ab,ba)<0){
   	  	 	 char temp[10];
   	  	 	 strcpy(temp,str[j]);
   	  	 	 strcpy(str[j],str[j+1]);
   	  	 	 strcpy(str[j+1],temp);
		 }
	  }
   }



/**********  End  **********/
}
int main(void)
{
    int i,n;
    char s[]=" ab9a3ds  ab9r   mn79a pm9s1d ",str[20][10];
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL) 
    {
        printf("File open error\n"), exit(0);
    }   
    printf("原始串为：\n");
    puts(s); 
    n=tqszc(s,str);
    printf("提取的数字子串为：\n"); 
    fprintf(fp,"提取的数字子串为：\n"); 
    for(i=0;i<n;i++)
    {
        printf("%s  ",str[i]);
        fprintf(fp,"%s",str[i]);
    }            
    Sort(str,n);
    printf("\n可以拼接的最大整数为：\n");
    fprintf(fp,"\n");
    for(i=0;i<n;i++)
    {
        printf("%s",str[i]);
        fprintf(fp,"%s",str[i]);
    }            
    printf("\n") , fprintf(fp,"\n");
    fclose(fp);
    return 0;
}
