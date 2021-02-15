package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1010 {
    private static int N, M;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            dp = new int[N + 1][M + 1];
            for (int n = 2; n <= N; n++) {
                dp[n][1] = 0;
            }
            for (int m = 1; m <= M; m++) {
                dp[1][m] = m;
            }

            for (int x = 2; x <= N; x++) {
                for (int y = 2; y <= M; y++) {
                    dp[x][y] = dp[x][y - 1] + dp[x - 1][y - 1];
                }
            }
            System.out.println(dp[N][M]);
        }
    }
}
