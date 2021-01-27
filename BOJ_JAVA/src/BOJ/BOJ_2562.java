package BOJ;

import java.util.Scanner;

public class BOJ_2562 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i, place;

        i = 1;
        place = 1;

        while (i < 9) {
            int new_n = sc.nextInt();
            i ++;
            if (new_n > n) {
                n = new_n;
                place = i;
            }
        }
        System.out.println(n);
        System.out.println(place);
    }
}