#include <stdio.h>
#include <conio.h>
#include <string.h>

   void main()
   {
       void wtext(FILE * fp) ;
       void rtext ( FILE * fp) ;
        ①   ;
       fp=fopen("score. dat","w") ;
       wtext(fp) ;
       fclose(fp) ;
       fp=fopen("score. dat","r") ;
       rtext( fp) ;
        ②  ;
   }
   /*1——写字符串到文件*／
   void wtext(FILE* fp)
  {
     char strc[60],cc[2]="#"；
     do{
         gets( strc)；
         if( strcmp( ③ )= =0）
             return;
         fputs(strc,fp)；
         fputc('\n',fp)；
         }while(l)；
  }
  /* 2- -从文件读字符串到屏幕*／
  void rtext( FILE* fp)
  {
       char ch;
       while( !feof(fp)
    {
       ch= fgetc(  ④  )；
       putchar(ch) ;
   } getch() ;
  } 