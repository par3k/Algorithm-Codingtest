package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10942 {
    private static int N, M, s, e;
    private static int[] arr;
    private static int[][] dp;

    private static int function(int start, int end) {
        if (start >= end) return 1;
        if (dp[start][end] != 0) return dp[start][end];
        if (arr[start] != arr[end]) return 0;
        dp[start][end] = function(start + 1, end - 1);
        return dp[start][end];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N][N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        M = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            sb.append(function(s - 1, e - 1)).append("\n");
        }
        System.out.print(sb.toString());
        br.close();
    }
}
