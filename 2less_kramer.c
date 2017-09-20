#include<stdio.h>
int main(){int x,p,l=0,w=0,c=0;while((x=getc(stdin))!=EOF){if(0<=x&&x<256)c++;if((x==' '||x=='\n'||x=='\t')&&p!=x)w++;if(x=='\n')l++;p=x;}printf("%d/%d/%d\n",l,w,c);}
