package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_2001 {
    private static int M;
    private static int[][] arr;

    private static int calc(int x, int y) {
        int tmp = 0;
        for (int i = x; i < x + M; i++) {
            for (int j = y; j < y + M; j++) {
                tmp += arr[i][j];
            }
        }
        return tmp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc =1; tc < T + 1; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            arr = new int[N][N];

            for (int i =0 ; i < N; i++) {
                String[] a = br.readLine().split(" ");
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(a[j]);
                }
            }
            int sum = 0;
            for (int i = 0; i <= N - M; i++) {
                for (int j = 0; j <= N - M; j++) {
                    sum = Math.max(sum, calc(i, j));
                }
            }
            System.out.println("#" + tc + " " + sum);
        }
    }
}
