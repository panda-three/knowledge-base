/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：程序将str中的连续数字字符转换为相应的正整数，按列保存在二维数组num中。
      然后按行统计num中每行素数个数，统计结果保存在一维数组pre中。

程序运行结果如下：
31  18  25  10
 6  19  23  21
14  12  27   8
 1   2   0

1.编写函数void change(int num[][COL],char str[])，将str中的连续数字字符转换为
  相应的正整数，按列保存在二维数组num中。str中至少有ROW*COL个连续数字字符串。
2.编写函数void find_prime(int pre[],int num[][COL])，统计二维数组num中每行
  素数个数，统计结果保存在一维数组pre的相应位置。

---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

#define ROW 3
#define COL 4
void change(int num[][COL],char str[])
{
/**********Program**********/
     int i;
     int n=0;
     for(i=0;str[i];i++){
     	  if(isdigit(str[i])){
     	  	   int y=0;
     	  	   for(;str[i]&&isdigit(str[i]);i++){
     	  	   	   y=y*10+str[i]-'0';
			   }
			   num[n%ROW][n/ROW]=y;
			   n++;
//			   if(n==ROW*COL)
//                return ;

		  }
	 }
//   int i,j,t;
//    i=j=0;
//    while(str[i]){
//        if(isdigit(str[i])){
//            t=0;
//            while(str[i] && isdigit(str[i]))
//                t=t*10+str[i++]-'0';
//            num[j%ROW][j/ROW]=t;
//            j++;
//            if(j==ROW*COL)
//                return ;
//        }
//        else
//            i++;
//   }

/**********  End  **********/

}
void find_prime(int pre[],int num[][COL])
{
/**********Program**********/

    int i,j,k,m,n,x;
	for(i=0;i<ROW;++i)
	{
        n=0;
        for(j=0;j<COL;++j)
        {
            x=num[i][j];
            m=(int)sqrt(x+1);
            for(k=2;k<=m;++k)
                if(x%k==0)
                    break;
            if(k>m)
                n++;
        }
        pre[i]=n;
	}



/**********  End  **********/
}
int main()
{
    char str[]={"31mi 6cr14osof 18 t v19 12i25,23sual 27stu10dio21see8de18c 15p"};
    int num[ROW][COL],pre[ROW];
    int i,j;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    change(num,str);
    for(i=0;i<ROW;++i)
    {
        for(j=0;j<COL;j++)
        {
            printf("%4d",num[i][j]);
            fprintf(fp,"%4d",num[ROW-1-i][j]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    find_prime(pre,num);
    for(i=0;i<ROW;++i)
    {
        printf("%3d",pre[i]);
        fprintf(fp,"%3d",pre[ROW-1-i]);
    }
    printf("\n");
    fprintf(fp,"\n");
    return 0;
}

