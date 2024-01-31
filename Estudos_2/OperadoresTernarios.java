package Estudos_2;

public class OperadoresTernarios {
    public static void main(String[] args) {
        int A = 8;
        String b;

        b = (A == 8) ? "Verdadeiro" : "Falso";
        System.out.println("Resultado: " + b);

        b = (A == 7) ? "Verdadeiro" : "Falso";
        System.out.println("Resultado: " + b);

        b = (A > 8) ? "Atrasado" : (A < 5) ? "Adiantado" : "Chegou no Horário";
        System.out.println("Resultado: " + b);
    }
    
}
