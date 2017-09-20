#include <stdio.h>

//feedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfeedfee

int main(){

        int x, p, l, w, c;

        l = w = c = 0;

        while ((x = getc(stdin)) != EOF){

                if(0 <= x && x < 256)

                        c++;

                if((x == ' ' || x == '\n' || x == '\t') && p != x)

                        w++;

                if(x == '\n')

                        l++;

                p = x;

        }

        printf("%d/%d/%d\n", l, w, c);

}
