package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[][] arr = new int[N][N];

            for (int i = 0; i < N; i++) {
                String s = br.readLine();
                for (int j = 0; j < N; j++) {
                    arr[i][j] = s.charAt(j) - '0';
                }
            }

            int ans = 0;
            for (int i = 0; i < N; i++) {
                for (int j = Math.abs(N / 2 - i); j < N - Math.abs(N / 2 - i); j++) {
                    ans += arr[i][j];
                }
            }
            System.out.println("#" + tc + " " + ans);
        }
    }
}