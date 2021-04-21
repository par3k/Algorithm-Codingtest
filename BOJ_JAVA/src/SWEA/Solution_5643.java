package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_5643 { // 키순서
    private static int N, M, from_, to_;
    private static final int INF = (int) 1e9;
    private static int[][] path;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            M = Integer.parseInt(br.readLine());
            path = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    path[i][j] = INF;
                }
            }

            for (int i = 0 ; i < M;i ++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                from_ = Integer.parseInt(st.nextToken());
                to_ = Integer.parseInt(st.nextToken());
                path[from_ - 1][to_ - 1] = 1;
            }


            for (int k = 0; k < N; k++) {
                for (int i = 0 ; i  < N; i++) {
                    for (int j = 0 ; j < N; j++) {
                        if (path[i][k] + path[k][j] == 2) {
                            path[i][j] = 1;
                        }
                    }
                }
            }

            int[] answer = new int[N];
            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < N; j++) {
                    if (path[i][j] == 1) {
                        answer[i]++;
                        answer[j]++;
                    }
                }
            }

            int tmp = 0;
            for (int i = 0 ; i < N; i++) {
                if (answer[i] == (N - 1)) {
                    tmp++;
                }
            }
            sb.append("#").append(tc).append(" ").append(tmp).append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}
