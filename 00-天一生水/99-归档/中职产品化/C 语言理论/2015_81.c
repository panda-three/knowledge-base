// ; 81．下列程序的功能是在键盘上输入学生3门课的成绩，然后查找出平均成绩不及格的学生并删除。在题81答题处填写合适的内容以完善程序。
  # include <stdio.h>
  # define N 50
  void main()
  {
    float scores[N][3],avestu[N];
    int i，j，k，mm；
    /*1- -输入学生成绩*／
    printf(" 输入成绩：\n ")；
for（i=0；i<N；i+ +）
    for(j=0;  ①  ；j++)
    scanf(" %f",&scores[i][j]);
/*2——计算学生平均成绩*／
for(i=0；i<N；i+ +)
{
    avestu[i]=  ②  ；
    for(j=0；j<3；j++)
      avestu[i]+=scores[i][j];
    avestu[i]/=3；

/* 3——显示学生单科及平均成绩*／
printf("学生成绩表：\n")；
  for（i=0；i<N；i++）
    {
    for(j=0；j<3；j++)
    printf（" %8. 2f" ，  ③  )；
    printf(" %8. 2f\n" ,avestu[i]);
    
printf("＼n")；
／* 4——查找并删除平均成绩不及格学生记录*／
mm=N-l;
for(i=mm;i>=O;i——)
  if(avestu[1]<60)
    {
      mm= mm-l;
      for（j=0；j<=mm；j+ +）
    {
       for(k=0；k<3；k++)
         scores[j][k]= scores[j+l][k];
       avestu[j]=  ④  ；
      }
    }
/* 5 ——输出平均成绩及格学生成绩*／
for（i=0；i<=mm；i++）
{
    for(j=0；j<3；j++)
    printf(”%8. 2f" ,scores[i][j]);
    printf(“%\n" ,avestu[il);
}
}