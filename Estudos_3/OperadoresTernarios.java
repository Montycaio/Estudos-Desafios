package Estudos_3;

public class OperadoresTernarios {
    public static void main(String[] args) {
        int A = 5;
        String b;

        b = (A == 5) ? "Verdadeiro" : "Falso";
        System.out.println("Resultado: " + b);

        b = (A == 7) ? "Verdadeiro" : "Falso";
        System.out.println("Resultado: " + b);

        b = (A > 5) ? "Atrasado" : (A < 5) ? "Adiantado" : "Chegou no Horário";
        System.out.println("Resultado: " + b);
    }
    
}
