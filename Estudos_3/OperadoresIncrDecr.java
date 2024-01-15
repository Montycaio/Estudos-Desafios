package Estudos_3;

public class OperadoresIncrDecr {
    
    public static void main(String[] args) {
        
        int num = 10;
        int result = 0;

        System.out.println("Valor original: " + result);
        result = num++;
        System.out.println("Valor de num após o incremento: " + num);
        System.out.println("Valor de result após o incremento: " + result);

        num = 10;
        result = 0;

        result = ++num;
        System.out.println("Valor de num após o incremento: " + num);
        System.out.println("Valor de result após o incremento: " + result);

    }

}
