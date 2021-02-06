package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_11403 {
    private static int[][] graph;
    private static boolean[] visited;
    private static int N;

    private static void dfs(int x, int y) {
        visited[y] = true;
        graph[x][y] = 1;

        for (int i =0 ; i < N; i++) {
            if (graph[y][i] == 1 && visited[i] == false) {
                dfs(x, i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited[j] = false;
            }
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 1 && visited[j] == false) {
                    dfs(i, j);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j= 0; j <N; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }
}
