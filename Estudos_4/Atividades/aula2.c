#include <stdio.h>
#include <stdlib.h>

//Este é o projeto da aula

int main ()
{
    int numero; // Isto é uma variável
    
    
    printf("Digite um numero: "); //imprime a frase na tela
    scanf("%d",&numero); //lê o numero que o usuário digita
    getchar(); //limpa o buffer do teclado do PC

    printf("O numero e igual a: %d\n\n",numero); //imprime o numero digitado.

    system("PAUSE");
    return 0;
}