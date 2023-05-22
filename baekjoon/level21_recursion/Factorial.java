import java.util.Scanner;

class Factorial {    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        if(N == 1) {
            System.out.println(1);
        } else {
            System.out.println(N * Factorial(N-1));
        }
    }
    public int Factor() {
        
    }
}