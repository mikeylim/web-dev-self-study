import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt();
        if ((userInput % 4 == 0 && userInput % 100 != 0) || (userInput % 4 == 0 && userInput % 400 == 0)) {
            System.out.println(1);
        } else {
            System.out.println(2);
        }
    }
}