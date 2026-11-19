/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：程序从十进制正整数start开始，产生一个十进制正整数数列，将数列按行填入二维
      整型数组dec左下三角。再将dec中整数转换为十六进制形式的字符填入二维
      字符型数组hex的对应位置中。

当start=17时,程序运行结果如下：
10进制形式
 17 
 18 20 
 23 27 32
 38 45 53 62
16进制形式
11
12 14
17 1B 20
26 2D 35 3E 

1.编写函数void gen(int dec[][ROW],int start)，从十进制正整数start开始，
  按照上述显示结果产生十进制正整数数列，按行填写到二维整型数组dec中左下三角。

2.编写函数void transf(char hex[][COL],int dec[][ROW])，将二维整型数组dec中
  的十进制正整数转换为十六进制字符形式，填写到二维字符型数组hex的对应位置
  （dec中的正整数均小于256）。
---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#define ROW 4
#define COL 9

void gen(int dec[][ROW],int start)
{
/**********Program**********/
	 int i,j,inc=1;
      for(i=0;i<ROW;++i)
        for (j=0;j<=i;++j){
            dec[i][j]=start;
            start+=inc++;
        }
/**********  End  **********/
}
void transf(char hex[][COL],int dec[][ROW])
{
/**********Program**********/
      int i,j,cnt=0; 
      for(i=0;i<ROW;++i)
      	for (j=0;j<=i;++j){
            int k=dec[i][j];
			hex[i][j*2]=(k/16<10? k/16+48:k/16+55);
			hex[i][j*2+1]=(k%16<10?k%16+48:k%16+55);
        }

//    int i,j,k;
//    for(i=0;i<ROW;++i)
//        for(j=0;j<=i;++j){
//            k=dec[i][j];
//            hex[i][j*2]=(k/16<10? k/16+48:k/16+55);
//            hex[i][j*2+1]=(k%16<10?k%16+48:k%16+55);
//        }
        
/**********  End  **********/
}
int main(void)
{
    int dec[ROW][ROW],i,j;
    char hex[ROW][COL]={0};
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    gen(dec,17);
    printf("10进制形式\n");
    for(i=0;i<ROW;++i)
    {
        for(j=0;j<=i;++j)
        {
            printf("%3d ",dec[i][j]);
            fprintf(fp,"%d ",dec[i][i-j]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    transf(hex,dec);
    printf("16进制形式\n");
    for(i=0;i<ROW;++i)
    {
        for(j=0;j<=i;++j)
        {
            printf(" %c%c",hex[i][j*2],hex[i][j*2+1]);
            fprintf(fp,"%c%c",hex[i][(i-j)*2],hex[i][(i-j)*2+1]);
        }
        printf("\n");
        fprintf(fp,"\n");
    }
    fclose(fp);
    return 0;
}

