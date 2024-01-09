package Estudos_2;

import java.util.Scanner;

public class Scanner {
   
    public static void main(String[] args) {
        
        Scanner texto = new Scanner(System.in);
        String str;
        System.out.println("Entre com seu nome: ");
        str = texto.nextLine();
        System.out.println("Bem-vindo " + str);

        texto.clone();
    }
}
