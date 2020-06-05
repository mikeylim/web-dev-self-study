import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String time[] = sc.nextLine().split(" ");
        int h = Integer.parseInt(time[0]);
        if (h == 0) {
            h = 24;
        }
        int m = Integer.parseInt(time[1]);
        int inputTimeInMin = h * 60 + m;
        int alarmTimeInMin = inputTimeInMin - 45;

        h = alarmTimeInMin / 60;
        m = alarmTimeInMin % 60;
        System.out.println(h + " " + m);
    }
}