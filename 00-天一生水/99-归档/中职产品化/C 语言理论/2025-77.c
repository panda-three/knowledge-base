/*计算机应用专业综合理论试卷编程题：削峰法求最小新整数

题目描述
文件sortdata.txt中存放一组正整数组成的升序表。程序功能是：输入一个不低于3位的正整数，不改变各数字之间的顺序关系，用削峰法删除其中三个数字后，得到一个值最小的新整数；查找新整数在上述升序表中是否存在，若存在输出它的序号。请在答题卡上写出①～④表示的内容以完善程序。
削峰法删除数字：一串数字，从最左侧开始，连续升序或降序的部分作为一段。若该段数字降序排列，删除最左侧的一个大数字后，新组成一个最小数；反之，该段数字升序排列，删除该段最右侧的一个大数字后，新组成一个最小数。

完整程序代码
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define DEL 3
int main()
{
    int get_min(char strn[],int);
    int find(int);
    char strn[20];
    int newn,m;
    gets(strn);
    newn=get_min(strn,DEL);
    printf("最小整数:%d\n",newn);
    m=find(newn);
    if(m>=0)printf("在有序表中的序号:%d\n",m+1);
    else printf("有序表中不存在该数");
}
//用削峰法删除其中三个数字后，得到一个值最小的新整数
int get_min(char strn[],int deln)
{
    int num,lenth,i,k,dn;
    lenth=strlen(strn);
    for(dn=1; ①  ;dn++)
    {
        i=0;
        while(strn[i]<=strn[i+1]&&i<lenth-dn)
            i++;
        for(k=i;k<lenth-dn;k++)
            ②  ;
    }
    num=0;
    for(k=0;k<=lenth-deln-1;k++)
        num=num*10+strn[k]-0x30;
    return(num);
}

//查找新整数在升序表中的序号
int find(int num)
{
    FILE *fpd;
    int a[100],p,h=0,b=0;
    if((fpd=fopen("sortdata.txt","r+"))==NULL)
    {
        printf("cannot open file.\n");
        exit(0);
    }
    while(!feof(fpd))
    {
        fscanf(fpd,"%d",&a[b]);
        b++;
    }
    fclose(fpd);
    b--;
    while( ③ )
    {
        p=(h+b)/2;
        if(num>a[p])h=p+1;
        else b=p;
    }
    if(num==a[b]) ④ ;
    else return(-1);
}