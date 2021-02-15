package BOJ;

import java.util.Scanner;

public class BOJ_11328 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int [] alpha = new int[26];
            char [] word1 = sc.next().toCharArray();
            char [] word2 = sc.next().toCharArray();

            for (char ch : word1) alpha[ch - 97]++;
            for (char ch : word2) alpha[ch - 97]--;

            boolean flag = true;

            for (int j : alpha) {
                if (j != 0) {
                    flag = false;
                }
            }
            System.out.println(flag ? "Possible" : "Impossible");
        }
    }
}
