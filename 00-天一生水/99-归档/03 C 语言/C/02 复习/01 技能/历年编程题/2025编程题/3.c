/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符串str中包含若干个单词，单词是以1个大写字母开头，后跟0到多个小写
      字母组成。从这些单词中提取出所有的特殊单词，并将其存储到二维字符数组
      words中。所谓特殊单词是指以1个大写字母开头，后跟0到4个小写字母组成的
      单词。比如单词"Hello"、"Num"、"C"等都是特殊单词；"Deepseek"不是
      特殊单词。
           
      字符数组dck是一个单词库，存有若干个由小写字母组成的单词。将取出的
      特殊单词与单词库的单词进行匹配，匹配时不区分大小写字母。输出匹配
      成功的特殊单词。

程序的运行结果是：
   初始字符串：
   12HelloWorld34TimeCuntDeepseek*NumProgramOkDesktopCFine
   提取的特殊单词：
   Hello World Time Cunt Num Ok C Fine
   匹配成功的单词：
   Hello Time Cunt

1.编写函数 int extractWords(char str[], char words[][M])，从字符串str中
  提取所有特殊单词,存储到二维数组 words中，函数返回所提取的特殊单词个数。

2.编写函数 int findDuplicates(char words[][M],char dck[][M],int n)，对n个
  特殊单词 words依次与单词库dck中的单词进行匹配，匹配时不区分大小写字母。
  匹配成功的特殊单词依次存放在words中，函数返回匹配成功的特殊单词个数。
-----------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
---------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define M 20 
#define N 100

int extractWords(char str[], char words[][M])
{
/**********Program**********/
   int i=0;
   int cnt=0;
   while(str[i]){
   	   //提取特殊单词
		if(isupper(str[i])){
			 char temp[10];
			 int k=0;
			 temp[k++]=str[i++]; 
			 while(str[i]&&islower(str[i])){
			 	 temp[k++]=str[i];
			 	 i++;
			 }
			 if(k<=5){
			 	temp[k]='\0';
				strcpy(words[cnt],temp);
				cnt++;  
			 }
		} else{
			i++;
		}
   }
   return cnt;
/**********  End  **********/   
}

int findDuplicates(char words[][M],char dck[][M],int n)
{
/**********Program**********/
//    1.遍历words 
//    2.大写转小写
//    3.顺序查找 
     int i;
     int cnt=0;
	 for(i=0;i<n;i++){
	 	 char temp[10];
	 	 strcpy(temp,words[i]);
	 	 temp[0]=tolower(temp[0]);
	 	 int j;
	 	 for(j=0;j<N;j++){
	 	 	if(strcmp(temp,dck[j])==0){
	 	 		strcpy(words[cnt],words[i]);
	 	 		cnt++;
			}
		 }
	 }
    return cnt;
/**********  End  **********/  
}

int main() 
{
    char str[] = "12HelloWorld34TimeCuntDeepseek*NumProgramOkDesktopCFine";
    char dck[N][M]={"hello","time","cunt","false","deepseek"};
    char words[N][M]; 
    int n, k;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    printf("初始字符串：\n");
    puts(str);
    n = extractWords(str, words);
    printf("提取的特殊单词：\n");
    for (k = 0; k < n; k++) 
    {
        printf("%s ", words[k]);
        fprintf(fp,"%s ",words[k]);
    }
    printf("\n");
    n = findDuplicates(words,dck, n);
    printf("匹配成功的单词：\n");
    for (k = 0; k < n; k++) 
    {
        printf("%s ", words[k]);
        fprintf(fp,"%s ",words[k]);
    }
    printf("\n");
    fclose(fp);
    return 0;

}
