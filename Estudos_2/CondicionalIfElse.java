package Estudos_2;

import java.util.Scanner;

public class CondicionalIfElse {
    public static void main(String[] args) {
        int A;
        String B;
        String C;
        Scanner texto = new Scanner(System.in);

        System.out.println("Informe o horário que chegou: ");
        A = texto.nextInt();


        if (A == 5) {
            B = "Condição 1";
        }
        else if (A > 5){
            B = "Condição 2";
        }
        else {
            B = "Condição 3";
        }

        System.out.println(B);

        if (A == 5){
            C = "Você chegou no horário da reunião";
        }
        else if (A > 5){
            C = "Você chegou atrasado na reunião";
        }
        else {
            C = "Você chegou adiantado na reunião";
        }

        System.out.println(C);

        texto.close();
    }
}
