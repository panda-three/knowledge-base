/*----------------------------------------------------------------------
【程序设计】
------------------------------------------------------------------------
题目：一维字符型数组times中包含了多个由空格间隔的表示时间的字符串，每个时间
      字符串由10位字符组成，其中后缀"am"、"pm"表示上/下午。
      例如"11:04:34pm"表示下午11点4分34秒、"08:19:24am"表示上午8点19分24秒。也有
      不规范的时间格式，例如"18:39:18pm"（"pm"多余）。
      程序的功能是去除所有时间表示中的后缀"am"、"pm"，并将时间格式转换为规范化的，
      24小时制时间格式。

程序运行结果如下：
规范前时间：
11:04:34pm
00:19:24am
18:39:18pm

规范后时间：
23:04:34
00:19:24
18:39:18

1.编写函数int split(char time[][11],char times[])，将times中的多个时间形式的
  字符串，分解成单个时间形式的字符子串，存放到time中。函数返回time中字符串的个数。
2.编写函数void format(char time[][11],int n)，将time中n个表示时间字符串，
  进行规范化处理：去除后缀"am"或"pm"，并将时间格式转换为规范化的，24小时制时间格式。

---------------------------------------------------------
注意：在指定范围内编写程序，勿修改指定范围外的任何内容。
-------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int split(char time[][11],char times[])
{
/**********Program**********/




/**********  End  **********/

}
void format(char time[][11],int n)
{
/**********Program**********/




/**********  End  **********/

}

int main(){
    char times[100]=" 11:04:34pm  00:19:24am  18:39:18pm ";
    char time[10][11];
    int i,n;
    FILE *fp;
    if((fp=fopen("DATA.dat","w"))==NULL)
    {
        printf("File open error\n");
        exit(0);
    }
    n=split(time,times);
    puts("规范前时间：");
    for(i=0;i<n;++i)
    {
        puts(time[i]);
        fputs(time[n-1-i],fp);
    }
    fputs("\n",fp);
    format(time,n);
    puts("\n规范后时间：");
    for(i=0;i<n;++i)
    {
        puts(time[i]);
        fputs(time[n-1-i],fp);
    }
    fclose(fp);
    return 0;
}

