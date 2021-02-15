package BOJ;

import java.util.Scanner;

public class BOJ_2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int result = A * B * C;
        int[] ans = new int[10];

        while (result > 0) {
            ans[result % 10]++;
            result /= 10;
        }

        for (int i : ans) {
            System.out.println(i);
        }

        sc.close();
    }
}
