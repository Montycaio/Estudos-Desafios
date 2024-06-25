public class principal {
    public static void main(String[] args) {
        carro c1 = new carro();
        c1.potencia = 10;
        c1.nome = "Uno";
        c1.velocidade = 0;
        
        carro c2 = new carro();
        c2.potencia = 10;
        c2.nome = "Corsa";
        c2.velocidade = 0;

        c1.acelerar();
        c1.acelerar();
        c1.acelerar();
        c1.acelerar();
        c1.frear();
        
        c2.acelerar();
        c2.acelerar();
        c2.frear();


        c1.imprimir();
        c2.imprimir();
    }
}
