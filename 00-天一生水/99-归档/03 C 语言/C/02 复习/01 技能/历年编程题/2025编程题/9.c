/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：字符数组str中存放了多个由10个数字字符组成的子串，每个子串之间由1个
      逗号","隔开，正确的子串是每个数字字符在子串中必须出现且仅能出
      现1次。但题目所给的str中的某些子串存在错误（最多只有1处出错），
      要求找出该子串中出错的数字字符，并将出错字符中的后一个替换为正确
      的数字字符。           
例如：字符串"0456987210"应改为"0456987213"。 

程序运行结果如下： 
    0922486375--->0921486375
    0962485371--->Right!
    0456987210--->0456987213
    2015987243--->2015987643

1.编写函数int GetStr(char str[],char Seq[][10])，从字符数组str中按要求取出
数字字符组成的子串放入二维字符数组Seq中，返回子串的个数。

2.编写函数int Check(char str[])，判断字符数组str中的数字字符有没有录入
  错误，如没有错误，则返回0；如有错误，请按题目要求进行替换，并返回1。   
-----------------------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
---------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define N 11
#define M 8

int GetStr(char str[],char seq[][N])
{
/**********Program**********/
    int i=0;
    int cnt=0;
    while(str[i]){
    	if(str[i]!=','){
    		 int k=0;
    		 char temp[20]; 
    		 while(str[i]&&str[i]!=','){
    		 	 temp[k++]=str[i];
    		 	 i++;
			 }
			 temp[k]='\0';
			 strcpy(seq[cnt++],temp);
		}else{
			i++;
		}
	}
    return cnt;
     
/**********  End  **********/
}
int Check(char str[])
{
/**********Program**********/
    /*
       1.统计字符出现的次数
	   2.找缺和重复的字符
	   3.把重复替换成缺的 
    */
    // 1.统计字符出现的次数
    int count[10]={0}; 
    int i;
    int n=strlen(str);
    for(i=0;i<n;i++){
    	int m=str[i]-'0';
    	count[m]=count[m]+1;
	}
	// 2.找缺和重复的字符
	char miss='a';
	char repeat='a';
	int j;
	for(j=0;j<10;j++){
		if(count[j]==0){
			miss=j+'0';
		}
		if(count[j]==2){
			repeat=j+'0';
		}
	}
	if(miss=='a'&&repeat=='a'){
		return 0;
	}
	
//	3.把重复替换成缺的 :1)找重复字符
    for(i=n-1;i>=0;i--){
    	if(str[i]==repeat){
    		str[i]=miss;
    		break;
		} 
	}
	return 1;
/**********  End  **********/
}
 
int main()
{
    char str[100]={"0922486375,0962485371,0456987210,2015987243"};
    char seq[M][N]={""};
    char tmp[N]="";
    int i,n;        
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    n=GetStr(str,seq);      
    for(i=0;i<n;i++)
    {    
        strcpy(tmp,seq[i]);
        if(Check(seq[i])==1)
        {    
            printf("%s--->%s\n",tmp,seq[i]);
            fprintf(fp,"%s***>%s\n",tmp,seq[i]);
        }    
        else
        {
            printf("%s--->Right!\n",seq[i]);
            fprintf(fp,"%s***>Right!\n",seq[i]);
        }    
    }
    fclose(fp);
    return 0;
}
