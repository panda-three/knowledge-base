// ; 下列程序的功能是：将存放在文件“1．txt”中的数字读出并用选择法排序。请在答题卡上相应位置完善程序。
# include <stdio.h>
# include <stdlib.h>
void main()
{
    FILE *fp;
    int i,j ,min,temp,a[10] ;
    if（（fp = fopen( "1. txt" , "r")））= = NULL)
    {
    printf( " can't open file !  \n") ;
    exit(0) ;
    }
    for(i=O;i<10;i++)
    fscanf(①,”%d”,&a[i]);
    printf("初始数据为:\n") ;
    for(i=0 ;i<10 ;1++)
    printf("%5d",a[i]) ;
    printf( "\n") ;
    for(i=0；i<10,i++)
    {
    ②;
    for(j=i+1；  ③  ；j++)
    if(a[min]>a[j])④;
    temp=a[i] ;
    a[min] = temp ;
    printf(“\n排序之后的数据为：\n”)；
    for(i=O;i<10;i++)
    printf(“%5d”，a[i])；
    printf(“\n”)；
}