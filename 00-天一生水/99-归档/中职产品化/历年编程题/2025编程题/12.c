/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符串str中存储着由空格分隔的英文单词。程序需先逐个提取这些单词，
      并将其存储于二维数组words的每一行。随后，从words中找出所有不降单词，
      并保存至二维数组ascend中。
      所谓不降单词是指从左至右单词的各字母的ASCII值非递减，例如"been"和
      "ghosy"便属于不降单词。
    
程序运行结果如下：
一共有8个单词
其中有6个不降单词，分别是:
aim
boost
begin
deeps
add
glory

1.编写函数int split(char words[][20], char str[])，将str中由空格分隔的
  英文单词，依次存放于二维数组words的每一行，最终返回单词的数量。

2.编写函数int check(char ascend[][20],char words[][20],int n)，从存储
  在words中的n个单词里找出所有不降单词，并将这些不降单词保存至ascend中，
  最后返回不降单词的数量。  
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int split(char words[][20],char str[]) 
{
/**********Program**********/
	int i=0,cnt=0;
	while(str[i]){
		if(str[i]!=' '){
			char temp[20];int k=0;
			while(str[i]&&str[i]!=' '){
			  temp[k++]=str[i];
			   i++;
			}
			temp[k]='\0';
			strcpy(words[cnt++],temp);
		}else{
		  i++;
	    }		
	}
	return cnt;
/**********  End  **********/
}

int check(char ascend[][20],char words[][20],int n) 
{
/**********Program**********/
    /*
       1.遍历words这个数组，取出每一个单词
	   2.判断是否为不降单词  ：标志位
	   3.放入ascend中 
    */
     int i;
//      1.遍历words这个数组，取出每一个单词
     int cnt=0;
	 for(i=0;i<n;i++){
	 	char temp[20];
		strcpy(temp,words[i]) ;
//		 2.判断是否为不降单词  ：标志位
        int j;
        int flag=1;//是不降单词 
		for(j=1;temp[j];j++){
			if(temp[j]<temp[j-1]){
				flag=0; //不是不降单词
				break; 
			}
		}
		if(flag==1){
//			 3.放入ascend中 
			strcpy(ascend[cnt++],temp);
		}
	 } 
  
     return cnt;
/**********  End  **********/
}

int main(void) 
{
    char str[]= {"aim bright boost cheer begin deeps add glory "};
    char words[10][20], ascend[10][20];
    int i,j,n;
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL)
    {
        printf("File open error\n"), exit(0);
    }    
    n=split(words,str);
    printf("一共有%d个单词\n",n);
    fprintf(fp, "单词个数[%d]\n",n);
    n=check(ascend,words,n);
    printf("其中有%d个不降单词，分别是:\n",n);
    fprintf(fp, "不降词数[%d]\n",n);
    for(i=0; i<n; i++) 
    {
        printf("%s\n",ascend[i]);   
        j=0;
        while(ascend[i][j])
            fprintf(fp, "%c",ascend[i][j++]+90);  
        fprintf(fp, "--");                
    }
    fclose(fp);
    return 0;
}
