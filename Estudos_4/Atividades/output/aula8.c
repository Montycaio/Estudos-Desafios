#include <stdio.h>
#include <stdlib.h>

int main()
{
    int opcao, valor;

    printf("\nConversor Bases Numericas\n\n");
    printf("1: Decimal para Hexadecimal\n");
    printf("2: Hexadecimal para Decimal\n");
    printf("\n\nInforme a opcao:#");
    scanf("%d", &opcao);
    getchar();

    if (opcao == 1)
    {
        printf("Informe um numero:");
        scanf("%d", &valor);
        getchar();
        printf("\n\"%d\" em Hexadecimal sera: \"%x\"\n\n.",valor,valor);
    }

   else if (opcao ==2)
    {
        printf("Informe um numero:");
        scanf("%x", &valor);
        getchar();
        printf("\n\"%x\" em Decimal sera: \"%d\"\n\n.",valor,valor);

    }

    else
    {
        printf("\nOpcao Invalida.\n\n");
    }
    

    system("PAUSE");
    return 0;
}