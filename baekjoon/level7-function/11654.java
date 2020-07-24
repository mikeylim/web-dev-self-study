import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char inputString = sc.next().charAt(0);
        int asciiNum = (int) inputString;
        System.out.println(asciiNum);
    }
}