package Estudos_3;

import java.util.Random;

public class GeradorNumerico {

    public static void main(String[] args) {
        Random aleatorio = new Random();

        int valor = aleatorio.nextInt(19) +1;

        System.out.println("Número gerado: " + valor);
    }
    
}
