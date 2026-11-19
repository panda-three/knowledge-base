/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：二维数组stu_name和stu_id中分别存放着学生的姓名和身份证信息，请统计
      男生人数，输出男生姓名，并根据出生日期对所有学生信息进行升序排序。

程序中已有函数mid(char str[],int p,int w)，功能是将字符串str中p位置开始，
w个数字字符转换成整数，函数返回该整数。

程序运行结果如下： 
共2个男生: 李四 钱七

钱七    321326200508316352
李四    321003200512085412
王五    32070120060103816X
张三    320121200602283046
赵六    320308200608242163


1、编写函数find_boy(char stu_id[][19],int boy_id[])，调用mid函数取学生
   身份证号码的第17位（男生为奇数），将男生所在行的下标写入boy_id,返回男
   生人数；
2、编写函数sort(char stu_name[][10],char stu_id[][19])，调用mid函数取
   学生的出生日期，按出生日期对所有学生信息进行升序排序。 
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define N 5

int mid(char str[],int p,int w)
{
    int i,num=0;
    for(i=p-1;i<p+w-1;i++)
        num=num*10+str[i]-48;
    return num;
}
int find_boy(char stu_id[][19],int boy_id[])
{
/**********Program**********/
   int i;
   int cnt=0;
   for(i=0;i<N;i++){
   	   char a[20];
	   strcpy(a,stu_id[i]);
	   int wei=mid(a,17,1); 
	   if(wei%2==1){
	   	   boy_id[cnt++]=i;
	   }
   }
   
//   int i=0;
//   while(stu_id[i]!='\0'){
//   	    char a[20];
//	   strcpy(a,stu_id[i]);
//	   int wei=mid(a,17,1); 
//	   if(wei%2==1){
//	   	   boy_id[cnt++]=i;
//	   }
//	   i++;
//   }
   return cnt;

/**********  End  **********/
}
void sort(char stu_name[][10],char stu_id[][19])
{
/**********Program**********/
   int i,j;
   for(i=0;i<N;i++){
	     for(j=0;j<N-1-i;j++){
//	     	char a[20];
//	        strcpy(a,stu_id[j]);
//	        char b[20];
//	        strcpy(b,stu_id[j+1]);
	        
	        int date1=mid(stu_id[j],7,8);
	        int date2=mid(stu_id[j+1],7,8);
	        if(date1>date2){
	        	char temp1[20];
	        	strcpy(temp1,stu_name[j]);
	        	strcpy(stu_name[j],stu_name[j+1]);
	        	strcpy(stu_name[j+1],temp1);
	        	
	        	char temp2[20];
	        	strcpy(temp2,stu_id[j]);
	        	strcpy(stu_id[j],stu_id[j+1]);
	        	strcpy(stu_id[j+1],temp2);
			}
		 }
	     
   }
/**********  End  **********/

}
int main(void) 
{
    int i,n=0;
    char stu_name[N][10]={"张三","李四","王五","赵六","钱七"};
    char stu_id[N][19]={"320121200602283046","321003200512085412","32070120060103816X",
                        "320308200608242163","321326200508316352"};
    int boy_id[N];
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    n=find_boy(stu_id,boy_id);
    printf("共%d个男生: ",n);
    for(i=0;i<n;i++)
    {
        printf("%s\t",stu_name[boy_id[i]]);
        fprintf(fp,"%s\t",stu_name[boy_id[i]]);
    }
    puts("\n");
    sort(stu_name,stu_id);
    for(i=0;i<N;i++)
    {
        printf("%s\t%s\n",stu_name[i],stu_id[i]);    
        fprintf(fp,"%s\t%s\n",stu_name[N-1-i],stu_id[N-1-i]);
    }
    fclose(fp);
    return 0;
}

