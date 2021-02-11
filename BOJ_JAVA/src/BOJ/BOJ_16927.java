package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_16927 {
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};
    private static int[][] graph;
    private static int[][] visited;
    private static int N, M, R;
    private static int sX, sY, eX, eY;

    private static int dfs(int x, int y, int idx) {
        visited[x][y]++;
        int nx = x + dx[idx];
        int ny = y + dy[idx];

        if (nx < sX || ny < sY || nx > eX || ny > eY) {
            idx++;
            nx = x + dx[idx];
            ny = y + dy[idx];
        }

        if (visited[nx][ny] == visited[x][y]) {
            int tmp = graph[x][y];
            graph[x][y] = graph[nx][ny];
            return tmp;
        }

        int tmp = graph[x][y];
        graph[x][y] = dfs(nx, ny, idx);
        return tmp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        graph = new int[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j  = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        sX = 0;
        sY = 0;
        eX = N - 1;
        eY = M - 1;

        int n = N;
        int m = M;

        for (int i = 0; ; i++) {
            for (int j = 0; j < R % ((n - 1) * 2 + (m - 1) * 2); j++) {
                dfs(i, i, 0);
            }

            sX++;
            sY++;
            eX--;
            eY--;
            n -= 2;
            m -= 2;

            if (sX > eX || sY > eY) break;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(graph[i][j] + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }
}
