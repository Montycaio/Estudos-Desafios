package Estudos_2;

import java.util.Scanner;

public class ContadorWhile2 {
    public static void main(String[] args) {
        Scanner Entrada = new Scanner(System.in);
        String nome;
        
        System.out.println("Digite seu nome: ");
        nome = Entrada.nextLine();


        while (!nome.equals("s")) {
            System.out.println("Seja-bem vindo " + nome);
            System.out.println("Digite seu nome ou s para sair");
            nome = Entrada.nextLine();
        }

        Entrada.close();
        
    }
}
