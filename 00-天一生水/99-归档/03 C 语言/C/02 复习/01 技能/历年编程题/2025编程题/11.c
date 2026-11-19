/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：s是一个字符串，按以下步骤对其进行处理：
      1.删除s中的非字母字符；
      2.从左到右按字符出现的顺序将相同的字符放置在一起。
      3.对于上述两步处理后的字符串s，从中找出等值子串依次存放到二维数组
      str中。其中，等值子串是指由两个及两个以上相同字符组成的字符串。

例如：原字符串为 "#fac_Mah@jd,dc-kdaj!f2ff"， 经过上述两步处理后的字符串为 
      "ffffaaaccMhjjdddk"，从中找出的等值子串依次为 
      "ffff"、"aaa"、"cc"、"jj"、"ddd"

程序运行结果如下：
原字符串为：#fac_Mah@jd,dc-kdaj!f2ff
处理后字符串为：ffffaaaccMhjjdddk
取出的等值字符子串有:
ffff
aaa
cc
jj
ddd
   
1.编写函数void Delete_move(char s[])，删除s字符串中非字母字符，再从左到右
  按字符出现的顺序将相同的字符放置在一起。

2.编写函数int Substr(char s[], char str[][100])。将s中的等值字符子串依次
  取出并放入二维数组str中，每一个等值子串在str中放一行。函数返回等值子串
  的个数。  
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

void Delete_move(char s[])
{
/**********Program**********/   
   int n=strlen(s);
   int i;
   char temp[200];
   int k=0;
   for(i=0;i<n;i++){
   	  if(isalpha(s[i])){
   		temp[k++]=s[i];
	  }
   }
   temp[k]='\0';
   int j;
   char result[200];
   int cnt=0;
   int used[256]= {0};
   int l;
   for(j=0;j<k;j++){
   	   int m=temp[j];
   	   if(used[m]==1){
   	   	   continue;
	    }
   	   for(l=0;l<k;l++){
   	   	   if(temp[l]==m){
   	   	   	  result[cnt++]=m;
		   }
	   }
   	   used[m]=1; 
   }
   result[cnt]='\0';
   strcpy(s,result);
/**********  End  **********/
}
int Substr(char s[], char result[][100])
{
/**********Program**********/
     int i;
     int len=strlen(s);
     int cnt=0;
     for(i=0;i<len;i++){
     	 if(s[i]==s[i+1]){
     	 	 int k=0;
     	 	 char temp[10];
     	 	 temp[k++]=s[i];
     	 	 for(;s[i]&&s[i]==s[i+1];i++){
     	 	 	temp[k++]=s[i];
			 }
			 if(k>=2){
				temp[k]='\0';
				strcpy(result[cnt++],temp); 
		     }
		 }
	 }

   return cnt;

/**********  End  **********/
}
int main(void)
{
    int i,n;
    char s[200]={"#fac_Mah@jd,dc-kdaj!f2ff"},result[50][100];   
    FILE *fp=fopen("DATA.dat","w");
    if(fp==NULL)
    {
        printf("File open error\n"), exit(0);
    }
    printf("原字符串为：%s\n",s);
    fprintf(fp,"[%s|",s);
    Delete_move(s);
    printf("整理后字符串为：%s\n",s);    
    fprintf(fp,"|%s|]",s);
    if(n=Substr(s,result))
    {
        printf("取出的等值字符子串有:\n");
        for(i=0; i<n; i++)
        {
            printf("%s\n",result[i]);
            fprintf(fp,"-%s=",result[i]);
        }
        fprintf(fp,"\n");    
    }else 
    {
        printf("无等值字符子串。\n");
    }
    fclose(fp);
    return 0;
}
