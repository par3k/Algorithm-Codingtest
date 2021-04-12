package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3307 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int ans=  0;

        for (int tc =1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0 ;i  < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            int[] dp = new int[N];

            for (int i = 0; i < N; i++) {
                dp[i] = 1;

                for (int j = 0 ; j < i; j++) {
                    if (arr[i] > arr[j]) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
            }
            for (int i = 0  ; i <N; i++) {
                ans = Math.max(ans, dp[i]);
            }
            System.out.println("#" + tc + " " + ans);
            ans = 0;
        }
        br.close();
    }
}
