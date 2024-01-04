public package Estudos_2;

class CriaConta {

    public static void main(String[] args) {
        
        Conta primeiraConta = new Conta();
        primeiraConta.saldo = 100;

        System.out.println("Primeira Conta: " + primeiraConta.saldo);
    }
}