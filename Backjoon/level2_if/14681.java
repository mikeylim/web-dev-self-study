import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int point_one = sc.nextInt();
        int point_two = sc.nextInt();
        if (point_one > 0 && point_two > 0) {
            System.out.println(1);
        } else if (point_one < 0 && point_two > 0) {
            System.out.println(2);
        } else if (point_one < 0 && point_two < 0) {
            System.out.println(3);
        } else if (point_one > 0 && point_two < 0) {
            System.out.println(4);
        }
    }
}