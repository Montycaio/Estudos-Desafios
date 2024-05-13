 #include <stdio.h>
 #include <stdlib.h>

//Caso seja inserido a variavél antes do main, será considerada GLOBAL.
//Sendo utilizada em todo o programa.

 int main()
 {
    int numero01 = 15;

    float numero02 = 22.5;

    char caractere = 'C';

    printf("%d\n\n", numero01);
    printf("%.2f\n\n", numero02);
    printf("%c\n\n", caractere);

    system("PAUSE");
    return 0;
 }