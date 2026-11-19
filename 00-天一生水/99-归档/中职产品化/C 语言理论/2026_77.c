/*
### 题77：保留手机号正确率最高的问卷作答记录
77. 问卷包含八条四个选项的单选题，用户凭手机号可以多次完整作答；作答记录保存在文件`asw.txt`中，结构如题77图所示：每条记录包含手机号和答案。问卷参考答案按题目顺序保存在文件`key.txt`中。编程实现：文件`asw.txt`中每个手机号仅保留一条正确率最高的记录。请在答题卡上写出①~④表示的内容以完善程序。

题77图示例：
| 手机号       | 答案       |
|--------------|------------|
| 13615164777  | ABCABCDD   |
| 18920686220  | ACCACCBC   |
| 17952667096  | BCCACDBC   |
| 18920686220  | AACCDADD   |
| ……           |            |
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define M 50
#define N 8
//获取问卷作答记录，统计正确答案数
int __①__(char tel[][12],char asw[][N+1],int yes[])
{
    FILE *fa,*fk;
    char key[N+1];
    int i=0,p;
    if((fa=fopen("asw.txt","r")) ==NULL||(fk=fopen("key.txt","r")) ==NULL){
        printf("File cannot open!\n");exit(0);
    }
    fscanf(fk,"%s",key);
    while(!feof(fa)){
        fscanf(fa,"%s  %s",tel[i],asw[i]);
        if(strlen(tel[i])!=0){
            for(p=0;asw[i][p]!='\0'&&key[p]!='\0';p++)
                if(__②__)
                    yes[i]++;
            i++;
        }
    }
    fclose(fa);fclose(fk);
    return i;
}
//根据手机号和正确答案数降序排序
void sort(char tel[][12],char asw[][N+1],int yes[],int ct)
{
    int i,j,t;
    char s1[12],s2[N+1];
    for(i=0;i<ct-1;i++)
        for(j=1;j<ct-i;j++)
            if(__③__ ||strcmp(tel[j-1],tel[j])==0&&yes[j-1]<yes[j]){
                strcpy(s1,tel[j-1]);strcpy(tel[j-1],tel[j]);strcpy(tel[j],s1);
                strcpy(s2,asw[j-1]);strcpy(asw[j-1],asw[j]);strcpy(asw[j],s2);
                t=yes[j-1];yes[j-1]=yes[j];yes[j]=t;
            }
}
int main()
{
    FILE *fp;
    char teln[M][12]={},asw[M][N+1]={};
    int yes[M]={0},i,m,n,p,ct;
    ct=get_rec(teln,asw,yes);
    sort(teln,asw,yes,ct);
    for(i=0;i<ct;i++){
        p=i;
        while(strcmp(teln[i],teln[p+1])==0&&p+1<ct)
            p++;
        for(m=i+1,n=p+1;n<ct&&i<p;m++,n++){
            strcpy(teln[m],teln[n]);
            strcpy(asw[m],asw[n]);
            yes[m]=yes[n];
        }
        __④__;
    }
    if((fp=fopen("asw.txt","w"))==NULL){
        printf("File cannot open!\n");exit(0);
    }
    for(i=0;i<ct;i++)
        fprintf(fp,"%s  %s\n",teln[i],asw[i]);
    fclose(fp);
    return 0;
}
