#include <stdio.h>
#include <stdlib.h>

    /*Rascunho de fórmulas:

    //Quantidade de kilo por animal
    valor_comida / quantidade_animal;

    //Quantidade por dia
    valor_comida * quantidade_animal;

    //Quantidade por mês
    (valor_comida * quantidade_animal)*30;

    //Valor estimado por mês
    ((valor_comida * quantidade_animal)*30)*valor_comida;*/

int main()
{
    int animal, quantidade_animal, valor_comida, resp = 0;

    printf("\nFOOD-ZOO\n");
    printf("O melhor programa para realizar calculo de comida dos animais do zoologico.\n");

    for (resp = 0; resp <= 1;)
    {
    
    printf("\nLISTA DE ANIMAIS DO ZOO\n\n");
    printf("1: Leao\n");
    printf("2: Leopardo\n");
    printf("3: Girafa\n");
    printf("4: Tigre\n");
    printf("5: Capivara\n");
    printf("6: Lobo\n");
    printf("7: Macaco\n");
    printf("8: Zebra\n");
    printf("9: Jacare\n");
    printf("10: Elefante\n");


    printf("\nInforme o Animal: \n");
    scanf("%d", &animal);
    getchar();

    while (animal > 10)
    {
        printf("\nAnimal nao registrado, favor verificar lista de animais do zoologico\n\n");
        return 0;
    }

    printf("\nInforme a Quantidade de animais: \n");
    scanf("%d", &quantidade_animal);
    getchar();

    printf("\nInforme o Custo por kilo de comida: \n");
    scanf("%d", &valor_comida);
    getchar();
    
    //Quantidade de kilo por animal
    int quantd_comida_animal = valor_comida / quantidade_animal;

    //Quantidade por dia
    int quantd_diaria = quantd_comida_animal * quantidade_animal;

    //Quantidade por mês
    int quantd_mes = (quantd_comida_animal * quantidade_animal)*30;

    //Valor estimado por mês
    int valor_mensal = ((quantd_comida_animal * quantidade_animal)*30)*valor_comida;


    if (animal == 1)
    {
        printf("\nLeao:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }
    
    else if (animal == 2)
    {
        printf("\nLeopardo:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }
    
    else if (animal == 3)
    {
        printf("\nGirafa:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }

    else if (animal == 4)
    {
        printf("\nTigre:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }

    else if (animal == 5)
    {
        printf("\nCapivara:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }
    
    else if (animal == 6)
    {
        printf("\nLobo:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }
    
    else if (animal == 7)
    {
        printf("\nMacaco:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }

    else if (animal == 8)
    {
        printf("\nZebra:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }

    else if (animal == 9)
    {
        printf("\nJacare:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }
    
    else if (animal == 10)
    {
        printf("\nElefante:\n");
        printf("Quantidade de comida individual: %d Kg\n", quantd_comida_animal);
        printf("Quantidade de comida por dia: %d kg\n", quantd_diaria);
        printf("Quantidade de comida por mes: %d kg\n", quantd_mes);
        printf("Custo estimado por mes: %d reais\n\n", valor_mensal);
        printf("\nRealizar novo calculo? 1:Sim | 2: Nao\n");
        scanf("%d", &resp);
        getchar();
    }

    else
    {
        
    }

    }

    system("PAUSE");
    return 0;
}