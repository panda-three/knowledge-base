/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：非智能手机键盘如下，在发英文信息时，是通过按下多次数字键来输入字
      母，例如：输入a需按键1次，输入b需按键2次，输入z需按键4次，输入空格
      需按键1次。编写程序，计算发出一段英文信息（内容只包含空格和英文小
      写字母），需要按键的次数，并根据按键次数的升序，输出英文信息及对应
      的次数。
       1     2    3
            abc  def
      --------------
       4     5    6
      ghi   jkl  mno
      --------------
       7     8    9
      pqrs  tuv wxyz

             0
             - 
程序运行结果如下：
排序前结果为：
    this is a book=>31
    beijing olympic games=>42
    he likes computer=>36
    c programe=>19
    i have a dream=>23

排序后结果为：
    c programe=>19
    i have a dream=>23
    this is a book=>31
    he likes computer=>36
    beijing olympic games=>42
                
1.编写函数int ajcs(char sen[])，统计输入sen字符串需要在键盘上按键的次数，
  并作为函数的返回值。 

2.编写函数void sort(char sen[][100],int cs[],int n)，根据cs数组中n个按键
  次数的值进行升序排序。 
---------------------------------------------------------
注意：请勿改动主函数main()中的任何语句。
-------------------------------------------------------*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>

#define N 5
int num[26]={1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4};
int ajcs(char sen[])
{
/**********Program**********/
    int i;
    int sum=0;
    for(i=0;sen[i];i++){
    	if(sen[i]==' '){
    		sum=sum+1;
		}else if(isalpha(sen[i])){
			sum=sum+num[sen[i]-97];
		}
	}
    return sum;

/**********  End  **********/
}
void sort(char sen[][100],int cs[],int n)
{
/**********Program**********/
    int i,j;
    for(i=0;i<n-1;i++){
    	for(j=0;j<n-1-i;j++){
    		if(cs[j]>cs[j+1]){
    			int temp;
    			temp=cs[j];
    			cs[j]=cs[j+1];
				cs[j+1]=temp; 
				
				char ch[100];
				strcpy(ch,sen[j]);
				strcpy(sen[j],sen[j+1]);
				strcpy(sen[j+1],ch);
			}
		}
    }



/**********  End  **********/
}
int main()
{
    char sen[N][100]={"this is a book",
                      "beijing olympic games",
                      "he likes computer",
                      "c programe",
                      "i have a dream"};
    int cs[N],i;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    for(i=0;i<N;i++)
        cs[i]=ajcs(sen[i]);
        
    printf("排序前结果为：\n");
    for(i=0;i<N;i++)
        printf("%s=>%d\n",sen[i],cs[i]);

    sort(sen,cs,N);

    printf("\n排序后结果为：\n");
    for(i=0;i<N;i++)
    {
        printf("%s=>%d\n",sen[i],cs[i]);
        fprintf(fp,"%s->%d\n",sen[i],cs[i]);
    }
    fclose(fp);   
    return 0;
}

