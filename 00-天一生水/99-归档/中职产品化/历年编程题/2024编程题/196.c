/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：将字符串中带符号整数转换成平衡三进制数(b3)。 

十进制数转换为平衡三进制数的方法：
先将十进制数转换为三进制数，如210(10)=21210(3)， 
然后从低位向高位逐位处理（处理每一位时需考虑低位的进位）:
·若为1或0，则保持不变;
·若为2，则替换为Z，并向高位进位(即高位+1)； 
·若为3(原来的2得到进位会变成3)，则替换为0，并向高位进位(即高位+1)。 

例如：210(10)=21210(3)=10ZZ10(b3)

正整数的平衡三进制中的Z变成1，1变成Z，即可得到对应负整数的平衡三进制。 
 210(10)=10ZZ10(b3)
-210(10)=Z011Z0(b3)

程序运行结果如下：
4       -5      0       64      237     -237

4       11
-5      Z11
0       0
64      1Z101
237     100Z10
-237    Z001Z0

1、编写函数int find(char s[],int d[]),将字符数组s中的数字子串（带符号）
   转变成十进制整数存放在整型数组d中,函数返回整数的个数。
2、编写函数void dtob3(int n,char b3[])，将十进制整数n转换成平衡三进制数
   存入b3字符数组。注：Z为大写字母
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define N 10 

int find(char s[],int d[])
{
/**********Program**********/
    int i;
    int cnt=0;
    for(i=0;s[i];i++){
    	if(isdigit(s[i])){
    		int sign=1;
    		if(s[i-1]=='-'){
    			sign=-1;
			}
    		int y=0;
    		for(;s[i]&&isdigit(s[i]);i++){
    			y=y*10+s[i]-'0';
			}
			d[cnt++]=sign*y;
		}
	}
    return cnt;


/**********  End  **********/
}
void dtob3(int n,char b3[]) 
{
/**********Program**********/
       if(n==0){
       	   strcpy(b3,"0");
       	   return;
	   }
       int i=0,len=0,t=0,f=1;
	   if(n<0) n=-n,f=-1;
	   while(n||t==1){
//	   	  if(n==0&&t==0){
//	   	  	  b3[len]='0';
//	   	  	  len++;
//	   	  	  break;
//		  }
	  	  b3[len]=n%3+48+t;
	   	  if(b3[len]=='2')
	   	     b3[len]='Z',t=1;
	   	  else if(b3[len]=='3')
	   	     b3[len]='0',t=1;
	   	  else 
	   	     t=0;
	   	  n/=3;
	   	  len++;
	   }
	   b3[len]=0;
	   for(i=0;i<len/2;i++){
	   	 t=b3[i];
	   	 b3[i]=b3[len-1-i];
	   	 b3[len-1-i]=t;
	   }
	   if(f==-1)
	     for(i=0;i<len;i++)
	        if(b3[i]=='1') b3[i]='Z';
	        else if(b3[i]=='Z') b3[i]='1';
//     int sign=1;
//     if(n<0){
//     	sign=-1;
//     	n=-n;
//	 }
//     int temp=n;
//     char a[20];
//     int k=0;
//     while(temp){
//     	int wei=temp%3;
//     	a[k++]=wei+'0';
//     	temp=temp/3;
//	 }
//	 a[k]='\0';
//	 char ch[k];
//	 int i;
//	 int m=0;
//	 for(i=k-1;i>=0;i--){
//	 	ch[m++]=a[i];
//	 }
//	 int j;
//     for(j=0;j<k;j++){
//     	if(ch[j]=='1'||ch[j]=='0') 
//     	   continue;
//     	else if(ch[j]=='2'){
//     		ch[j]='Z';
//     		ch[j+1]=ch[j+1]+1;
//		}
//		else if(ch[j]=='3'){
//			 ch[j]='0';
//			 ch[j+1]=ch[j+1]+1;
//		}  
//	 }
//	 ch[j+1]='\0';
//	 if(sign==-1){
//	 	for(j=0;j<=k;j++){
//	 		if(ch[j]=='1')
//			  ch[j]='Z';
//			else if(ch[j]=='Z')
//			  ch[j]='1';
//		}
//	 }
//     strcpy(b3,ch);

/**********  End  **********/
}
int main(void)
{
    char str[]="abc4def-5g0h64ig237km-237";
    int d[N],n;
    char b3[N][20]={0};
    int i;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    n=find(str,d);
    for(i=0;i<n;i++)
            printf("%d\t",d[i]);
    puts("\n");
    for(i=0;i<n;i++)
    {
        dtob3(d[i],b3[i]);
        printf("%d\t",d[i]);
        puts(b3[i]);
        fprintf(fp,"%d,%s\n",d[i],b3[i]);
    }
    fclose(fp);
    return 0;
}
