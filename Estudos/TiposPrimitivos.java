package Estudos;
public class TiposPrimitivos {
    public static void main(String[] args){
        System.out.println("Hello World");

        int valorA = 20; // Números inteiros

        int valorB = 20;  // Números inteiros

        double numeroDecimal = 5.5; //Números Decimais

        boolean tipoBooleano = true; //Verdadeiro ou Falso

        char letra = 'C'; //Caracteres

        String nome = "Caio"; //Texto

        int total = valorA + valorB; // Soma entre valor A e valor B

        Object objeto = new Object(); //Objeto

        System.out.printf("A soma total = %d\n", total);
        System.out.println("Números decimais: " + numeroDecimal);
        System.out.println("Tipo Booleano" + tipoBooleano);
        System.out.println("Tipo char: " + letra);
        System.out.println("Tipo String: " + nome);
        System.out.println("Tipo Objeto" + objeto);

    }
}