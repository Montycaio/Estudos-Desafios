import java.util.Scanner;

public class foodZoo implements Escape {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int animal, quantidade_animal, valor_comida, resp = 0;

        System.out.println("\nFOOD-ZOO");
        System.out.println("The best program to calculate food for the animals in the zoo.");

        for (resp = 0; resp <= 1;) {
            System.out.println("\nLIST OF ZOO ANIMALS\n");
            System.out.println("1: Lion");
            System.out.println("2: Leopard");
            System.out.println("3: Giraffe");
            System.out.println("4: Tiger");
            System.out.println("5: Capybara");
            System.out.println("6: Wolf");
            System.out.println("7: Monkey");
            System.out.println("8: Zebra");
            System.out.println("9: Alligator");
            System.out.println("10: Elephant");

            System.out.println("\nEnter the Animal: ");
            animal = scanner.nextInt();
            scanner.nextLine();

            while (animal > 10) {
                System.out.println("\nAnimal not registered, please check the list of zoo animals\n");
                return;
            }

            System.out.println("\nEnter the Number of animals: ");
            quantidade_animal = scanner.nextInt();
            scanner.nextLine();

            System.out.println("\nEnter the Cost per kilo of food: ");
            valor_comida = scanner.nextInt();
            scanner.nextLine();

            // Quantity of food per animal
            int quantd_comida_animal = valor_comida / quantidade_animal;

            // Quantity per day
            int quantd_diaria = quantd_comida_animal * quantidade_animal;

            // Quantity per month
            int quantd_mes = (quantd_comida_animal * quantidade_animal) * 30;

            // Estimated cost per month
            int valor_mensal = ((quantd_comida_animal * quantidade_animal) * 30) * valor_comida;

            if (animal == 1) {
                System.out.println("\nLion:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            } else if (animal == 2) {
                System.out.println("\nLeopard:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            } else if (animal == 3) {
                System.out.println("\nGiraffe:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            } else if (animal == 4) {
                System.out.println("\nTiger:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            } else if (animal == 5) {
                System.out.println("\nCapybara:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            } else if (animal == 6) {
                System.out.println("\nWolf:");
                System.out.println("Individual food quantity: " + quantd_comida_animal + " Kg");
                System.out.println("Food quantity per day: " + quantd_diaria + " kg");
                System.out.println("Food quantity per month: " + quantd_mes + " kg");
                System.out.println("Estimated cost per month: " + valor_mensal + " reais\n");
                System.out.println("\nPerform a new calculation? 1:Yes | 2: No");
                resp = scanner.nextInt();
                scanner.nextLine();
            }
        }
    }
}

