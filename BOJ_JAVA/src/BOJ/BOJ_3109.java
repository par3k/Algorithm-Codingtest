package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3109 {
    private static int[] dx = {-1, 0, 1};
    private static int[] dy = {1, 1, 1};
    private static int R, C, ans;
    private static char[][] graph;
    private static boolean flag;

    private static void dfs(int x, int y) {
        if (y == C - 1){
            flag = true;
            ans++;
            return;
        }

        for (int i = 0 ; i <3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                if (graph[nx][ny] == '.') {
                    graph[x][y] = 'x';
                    dfs(nx, ny);
                    if (flag) return;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            graph[i] = st.nextToken().toCharArray();
        }

        for (int i = 0; i < R; i++) {
            flag = false;
            dfs(i, 0);
        }
        System.out.println(ans);

        br.close();

    }
}
