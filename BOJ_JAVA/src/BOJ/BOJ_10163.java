package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10163 {
    private static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        graph = new int[101][101];
        int[] ans = new int[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());


            for (int xX = x; xX < x + a; xX++) {
                for (int yY = y; yY < y + b; yY++) {
                    graph[xX][yY] = i + 1;
                }
            }
        }

        for (int chk = 1; chk <= N; chk++) {
            int cnt = 0;
            for (int i = 0; i < 101; i++) {
                for (int j = 0; j < 101; j++) {
                    if (graph[i][j] == chk) {
                        cnt++;
                    }
                }
            }
            ans[chk - 1] = cnt;
        }

        for (int i : ans) {
            System.out.println(i);
        }

        br.close();
    }
}
