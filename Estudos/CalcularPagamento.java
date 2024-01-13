package Estudos;

public class CalcularPagamento {
  public static void main(String[] args) {
    try {

      System.out.println("Digite um número:");
      int numeroX = System.in.read();
      int numeroY = 30;

      alterarsoma(numeroX, numeroY);

    } catch (Exception e) {
      
      System.out.println("Erro: " + e.getMessage());
    }

  }

  // Assinatura
  private static void alterarsoma(int numeroX, int numeroY) {

    if (numeroX > 0) {
      numeroX = 100;
    }

    else {
      numeroX = 200;
    }

    int soma = numeroX + numeroY;

    System.out.println(soma);

  }

}