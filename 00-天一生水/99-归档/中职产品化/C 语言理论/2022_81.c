// 下列程序的功能是 :输入不含空格的字符串,寻找并输出字符串中出现次数最多的字母,大 小写视作同一字母,不统计非字母符导;
// 若出现次数最多的字母有多个,输出其中 ASCII 码值 最小的字母。
#include <stdio.h>
#include <ctype.h>
int main()
{
    char ch, s[1100], amount[27] = {0};
    int i, max = 0, c;
    scanf("%s", s); /* 把字符串 s 转换为小写字母 ,统计各字母出现次数*/
    for(i = 0; s[i] != '\0'; i++)
    {
        ch = tolower(s[i]);
        if(ch >= 'a' && ch <= 'z')
            amount[ch - 'a' + 1]++;
    }
    /*寻找并输出出现次数最多的字母*/
    for(i = 1; i <27; i++)
    {
        if(amount[i]>max)
        {
            c=i-1+'a';
            max = amount[i];
        }
    }
    if(max > 0)
        printf("%c\n", c );
    else
        printf("No\n");
    return 0;
}
