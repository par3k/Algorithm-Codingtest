package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1987 {
    private static int R, C, ans = -123456789;
    private static boolean[] visited;
    private static char[][] graph;

    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static void dfs(int x, int y, int m) {
        visited[graph[x][y] - 'A'] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];

            if (0 <= nx && nx < R && 0 <= ny && ny < C){
                if (!visited[graph[nx][ny] - 'A']) {
                    dfs(nx, ny, m + 1);

                }
            }
        }
        visited[graph[x][y] - 'A'] = false;
        ans = Math.max(ans, m);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];
        visited = new boolean[26];

        for (int i = 0 ; i < R; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < C; j++) {
                graph[i][j] = tmp.charAt(j);
            }
        }
        dfs(0, 0, 1);
        System.out.println(ans);

        br.close();
    }
}
