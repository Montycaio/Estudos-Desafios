package Estudos_2;

import java.util.Scanner;

public class Login {
    public static final String Caio = null;

    public static void main(String[] args) {
        String log;
        int password;
        Scanner texto = new Scanner(System.in);
        

        System.out.println("Login:");
        log = texto.nextLine();

        System.out.println("Seja bem-vindo " + log + "\ninforme sua senha, porfavor.");

        password = texto.nextInt();

        if (password == 2405){
        System.out.println("Acesso Autorizado!");
        }
        else {
        System.out.println("Acesso Negado!");
        }

        texto.close();
    }
}
