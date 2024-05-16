#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    int b;

    printf("Digite o valor de \"A\":");
    scanf("%d", &a);
    getchar();

    printf("Digite o valor de \"B\":");
    scanf("%d", &b);
    getchar();

    if (a < b)
    {
        printf("\nResp: A menor que B\n\n");
    }

    else if (a > b)
    {
        printf("\nResp: A maior que B\n\n");
    }

    else
    {
        printf("\nResp: A igual B\n\n");
    }
    
    

    system("PAUSE");
    return 0;
}