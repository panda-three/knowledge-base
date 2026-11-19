/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：将N个字符串中连续的十六进制数字字符子串转换成十进制整数，并
      按行存入一个新的二维字符数组，从而形成N个新的字符串。然后，
      根据字符串比较大小的规则，删除在从小到大的序列中排位第三的
      字符串，并保持其他字符串的相对位置不变。

程序运行结果如下：
提取后:
train
growt
compe
gwsuh
skill
ablit

删除后:
train
compe
gwsuh
skill
ablit

1.编写函数void abstract(char a[],char b[])，将字符串a中连续的十六进制
  数字字符转换成十进制整数，依次存放到字符数组b中，形成新的字符串。 
2.编写函数void delet(char t[][10]，int n)，遍历数组t中n个字符串，根据
  字符串比较大小的规则，找到从小到大序列为第三的字符串，删除它，其他
  字符串相对位置不变。 
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define N 6 
    
void abstract(char a[],char b[])
{
/**********Program**********/
    int i;
    int cnt=0;
    for(i=0;a[i];i++){
    	if(a[i]!='#'){
    		int y=0;
    		for(;a[i]&&a[i]!='#';i++){
    			if(isalpha(a[i])){
    				a[i]=toupper(a[i]);
    				a[i]=a[i]-55;
				}
				if(isdigit(a[i])){
					a[i]=a[i]-48;
				} 
    			y=y*16+a[i];
			}
			b[cnt++]=y;
		}
	}
	b[cnt]='\0';
/**********  End  **********/
}

void delet(char t[][10],int n)
{
/**********Program**********/
    int i,j;
    for(i=0;i<n;i++){
    	for(j=0;j<n-1-i;j++){
    		if(strcmp(t[j],t[j+1])>0){
                  char temp[10];
                  strcpy(temp,t[j]);
                  strcpy(t[j],t[j+1]);
                  strcpy(t[j+1],temp);
			}
		}
	}
	for(i=3;i<n;i++){
		strcpy(t[i-1],t[i]);
	}
/**********  End  **********/
}

int main(void)
{
    char s[N][50]={"74#72#61#69#6E","67#72#6F#77#74",
                   "63#6f#6D#70#65","67#77#73#75#68",
                   "73#6B#69#6C#6c","61#62#6C#69#74"};
    char t[N][10];
    int i;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    for(i=0;i<N;++i)
         abstract(s[i],t[i]);
    printf("提取后: \n"); 
    fprintf(fp,"提取后  : \n"); 
    for(i=0;i<N;++i)
    {
        printf("%s\n",t[i]);
        fprintf(fp,"%s\n",t[i]);
    }
    delet(t,N);
    printf("\n删除后: \n"); 
    fprintf(fp,"删除后  : \n"); 
    for(i=0;i<N-1;++i)
    {
        printf("%s\n",t[i]);
        fprintf(fp,"%s\n",t[i]);
    }
    fclose(fp);
    return 0;
}
