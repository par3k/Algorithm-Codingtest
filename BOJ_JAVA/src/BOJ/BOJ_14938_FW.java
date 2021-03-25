package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_14938_FW {
    private static final int INF = (int) 1e9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[] items = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        int[][] graph = new int[N + 1][N + 1];
        for (int i = 0; i <= N; i++) {
            Arrays.fill(graph[i], INF);
        }

        for (int i = 1 ; i <= N; i++) {
            graph[i][i] = 0;
        }


        for (int i = 0 ; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a][b] = graph[b][a] = c; // 양방향으로 데이터를 넣어준다
        }


        for (int z = 1; z < N + 1; z++) { // Floyd - Warshall
            for (int a = 1; a < N + 1; a++) {
                for (int b = 1; b < N + 1; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][z] + graph[z][b]);
                }
            }
        }

        int ans = 0;
        for (int i = 1; i <= N; i++) {
            int tmp = 0;
            for (int j = 1; j <= N; j++) {
                if (graph[i][j] <= M) tmp += items[j - 1];
            }
            ans = Math.max(ans, tmp);
        }
        System.out.println(ans);
        br.close();
    }
}

