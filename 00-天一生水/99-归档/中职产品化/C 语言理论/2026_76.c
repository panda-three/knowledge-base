/*
文件gz.txt中存储的是按照姓名升序排列的收人记录，结构如题76图所示：每条记录包含姓名和收人，每个人可能有多条收人记录。文件中无空白记录行，编程实现：输人姓名，统计其名下总收人。请在答题卡上写出①~④表示的内容以完善程序。
Jack 300
Kate 450
Kate 400
Rose 350……
*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//搜索姓名(xm)在有序表(name)中的位置
int search(char xm[],char name[][20],int n)
{
    int head=0,tail=n-1,mid,ret=-1;
    while(head<=tail){
        mid=head+(tail-head)/2;
        if(__①__)
            head=mid+1;
        else
            tail=mid-1;
    }
    if(strcmp(name[tail],xm)==0) ret=tail;
    return ret;
}
int main()
{
    __②__ *fgz;
    char name[100][20]={},fname[20];
    int sr[100]=(0),n=0,sum=0;
    if((fgz=fopen("gz.txt","r"))==NULL){
        puts("File cannot open!\n");exit(0);
    }
    while(!feof(fgz)){
        fscanf(fgz,"%s  %d",name[n],&sr[n]);n++;
    }
    fclose(fgz);
    scanf("%s",fname);
    int regn=search(fname,name,n);
    if(regn!=-1){
        while(strcmp(name[regn],fname)==0)
            regn--;
        __③__;
        while(strcmp(name[regn],fname)==0){
            sum+=sr[regn];regn++;
        }
        printf("%s名下总收人:%d\n",fname,__④__);
    }else
        printf("查无此人:%s\n",fname);
    return 0;
}
~第12页(共14页)