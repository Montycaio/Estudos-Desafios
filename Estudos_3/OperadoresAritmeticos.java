package Estudos_3;

public class OperadoresAritmeticos {

    public static void main(String[] args) {
        
        int x = 9;
        int y = 2;

        System.out.printf("x + y = %d\n", x + y);
        System.out.printf("x - y = %d\n", x - y);
        System.out.printf("x * y = %d\n", x * y);
        System.out.printf("x / y = %d\n", x / y); // Divisão inteira com trun
        System.out.printf("x / y = %2.2f\n", x / (double)y); // Divisão normal
        System.out.printf("x %% y = %d\n", x % y);

    }
    
}
