import java.util.Scanner;

public class Solve5585 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int sum_cnt = 0;
        int origin = 1000 - n;
        int[] coins = {500, 100, 50, 10, 5, 1};

        for (int i = 0; i < coins.length; i++) {
            sum_cnt += origin / coins[i];
            origin %= coins[i];
        }

        System.out.println(sum_cnt);

        sc.close();
    }
}
