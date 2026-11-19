// ; 下列程序实现旳是将键盘中输入旳字符串写入文献"score.dat"中并显示输出，用"#"作为字符串输入结束旳标志。
#include <stdio.h>
// #include <conio.h>
#include <string.h>

void wtext(FILE *fp);
void rtext(FILE *fp);

int main()
{
    FILE *fp;
    
    fp = fopen("score.dat", "w");
    wtext(fp);
    fclose(fp);
    
    fp = fopen("score.dat", "r");
    rtext(fp);
    fclose(fp);
    
    return 0;
}

void wtext(FILE *fp)
{
    char strc[60], cc[2] = "#";
    do
    {
        gets(strc);
        if(strcmp(strc,cc) == 0)
            return;
        fputs(strc, fp);
        fputc('\n', fp);
    } while(1);
}

void rtext(FILE *fp)
{
    char ch;
    while(!feof(fp))
    {
        ch = fgetc(fp);
        putchar(ch);
    }
    getch();
}
