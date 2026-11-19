/*
计算机应用专业综合理论试卷 招录考试程序填空题

招录考试中考生记录表如题76表所示，存储于文件grade.dat中。现有 A、B、C 三个单位，每个单位录用不超过5名工作人员。根据招录规则，编程输出 A、B、C三个单位的录用名册文件。请在答题卡上写出①～④表示的内容以完善程序。
招录规则： (1) 总分=笔试成绩+面试成绩。 (2) 根据总分由高到低按序录用；若总分相同，面试成绩高者优先录用。(注：考生总分相同，则面试成绩不同) (3) 同一考生的两个志愿，先选择第1志愿录用；若第1志愿招录满，选择第2志愿录用；若两个志愿均招录满，该考生落选。

计算机应用专业综合理论试卷 第 8页(共 14 页)

题76表

姓名	第1志愿	第2志愿	笔试成绩	面试成绩
谢小包	C	A	75	72
叶佳文	A	B	76	81
*/	
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 5
void get_rank(char na[][3][20],int gd[][3],int);
int main()
{
    FILE * fp, * fp1, * fp2, * fp3;
    int len=0,i,k;
    int gd[200][3]={0},ct[3]={0};
    char nv[200][3][20];
    if(! (  ①  =fopen("grade.dat","r+")))
    {
        printf("无法打开文件! \n");
        exit(0);
    }
    while(! feof(fp))
    {
        fscanf(fp,"%s%s%s",nv[len][0],nv[len][1],nv[len][2]);
        fscanf(fp,"%d%d",&gd[len][0],&gd[len][1]);
        //总分=笔试成绩+面试成绩
        gd[len][2]=gd[len][0]+gd[len][1];
        len++;
    }
    ②;
    if(! ((fp1=fopen("A.txt","w"))&&(fp2=fopen("B.txt","w"))&&
    (fp3=fopen("C.txt","w"))))
    {
        printf("无法打开文件! \n");
        exit(0);
    }
    i=0;
    /* 录用:同一考生的两个志愿,先选择第1志愿录用;若第1志愿招录满,选择第2志愿录用;若两个志愿均招录满,该考生落选。 */
    while((ct[0]<MAX||ct[1]<MAX||ct[2]<MAX)&& ③ )
    {
        for(k=1;k<=2;k++)
        {
            switch(nv[i][k][0])
            {
                case 'A':if(ct[0]<5){fprintf(fp1,"%s ",nv[i][0]);ct[0]++;k++;}break;
                case 'B':if(ct[1]<5){fprintf(fp2,"%s ",nv[i][0]);ct[1]++;k++;}break;
                case 'C':if(ct[2]<5){fprintf(fp3,"%s ",nv[i][0]);ct[2]++;k++;}break;
            }
        }
        i++;
    }
    fclose(fp);fclose(fp1);fclose(fp2);fclose(fp3);
}
//排名:根据总分由高到低按序录用;若总分相同,面试成绩高者优先录用。
void get_rank(char nv[][3][20],int gd[][3],int size)
{
    int i,j,k,p,gt;
    char nt[20];
    for(i=0;i<size-1;i++)
    {
        p=i;
        for(j=i+1;j<=size-1;j++)
        {
            if( ④ )
                p=j;
            else if(gd[p][2]==gd[j][2]&&gd[p][1]<gd[j][1])
                p=j;
            if(p!= i)
            {
                for(k=0;k<=2;k++)
                {
                    strcpy(nt,nv[p][k]);strcpy(nv[p][k],nv[i][k]);strcpy(nv[i][k],nt);
                    gt=gd[p][k];gd[p][k]=gd[i][k];gd[i][k]=gt;
                }
            }
        }
    }
}