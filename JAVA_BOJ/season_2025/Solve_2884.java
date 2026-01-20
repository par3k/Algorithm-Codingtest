package season_2025;

import java.util.Scanner;

public class Solve_2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();

        if (hour == 0 && minute < 45) {
            hour = 24;
        }

        if (minute < 45) {
            hour-=1;
            minute+=15;
        } else {
            minute-=45;
        }
        System.out.println(hour + " " + minute);
    }
}
