package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1463 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[1000001];

        for (int i = 2; i < N + 1; i++) {
            dp[i] = dp[i - 1] + 1;

            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
        }
        sb.append(dp[N]).append("\n");
        System.out.print(sb);
        br.close();
    }
}
