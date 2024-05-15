#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=0, b=0, c=0, d=0;

    a++;

    b--;

    c=1;

    c += a;

    d -= c;

    printf(" a= %d\n b= %d\n c= %d\n d= %d\n",a,b,c,d);


    system("PAUSE");
    return 0;
}