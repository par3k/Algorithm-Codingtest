package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14502_2 {
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int n, m, ans = 0;
    private static int[][] graph, tmp;

    private static int cntSafeArea() {
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tmp[i][j] == 0) {
                    res++;
                }
            }
        }
        return res;
    }

    private static void spreadVirus(int x, int y) {
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (tmp[nx][ny] == 0) {
                    tmp[nx][ny] = 2;
                    spreadVirus(nx, ny);
                }
            }
        }
    }

    private static void dfs(int wall) {
        if (wall == 3) { // stop condition
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    tmp[i][j] = graph[i][j];
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (tmp[i][j] == 2) {
                        spreadVirus(i, j);
                    }
                }
            }

            int cnt = cntSafeArea();
            ans = ans < cnt ? cnt : ans;
            return;
        }

        for (int i = 0 ; i < n; i++) { // set the wall
            for (int j = 0 ;j  <m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    wall++;
                    dfs(wall);
                    graph[i][j] = 0;
                    wall--;
                }
            }
        }
    }

    private static void Solution() {
        StringBuilder sb = new StringBuilder();
        dfs(0);
        sb.append(ans).append("\n");
        System.out.println(sb);

    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        tmp = new int[n][m];

        for (int i = 0 ; i <n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j <m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        } // graph
        br.close();
    }

    public static void main(String[] args) throws IOException {
        input();
        Solution();
    }

    private static class Node{
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
