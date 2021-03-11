package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1949 {
    private static int N, K, maxLen, maxHigh;
    private static int[][] graph;
    private static boolean[][] visited;
    private static int[] dx = {-1 ,1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static void DFS(int x, int y, int h, int l, int cnt) {
        for (int dir = 0; dir < 4; dir++) {
            if (maxLen < l) maxLen = l;

            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
               if (h <= graph[nx][ny]) {
                   if (cnt == 0) {
                       if (h > graph[nx][ny] - K) {
                           visited[nx][ny] = true;
                           DFS(nx, ny, h - 1, l + 1, cnt + 1);
                           visited[nx][ny] = false;
                       }
                   }
               } else {
                   visited[nx][ny] = true;
                   DFS(nx, ny, graph[nx][ny], l + 1, cnt);
                   visited[nx][ny] = false;
               }
            }
        }
    }

    private static void Solution() {
        for (int i = 0; i < N; i++) {
            for (int j = 0 ;j  < N; j++) {
                if (graph[i][j] == maxHigh) {
                    visited[i][j] = true;
                    DFS(i, j, maxHigh, 1, 0);
                    visited[i][j] = false;
                }
            }
        }
    }

    private static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            String[] line = br.readLine().split(" ");
            N = Integer.parseInt(line[0]);
            K = Integer.parseInt(line[1]);
            maxLen = maxHigh = 0;
            graph = new int[N][N];
            visited = new boolean[N][N];

            for (int i = 0 ; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if (maxHigh < graph[i][j]) {
                        maxHigh = graph[i][j];
                    }
                }
            }
            Solution();
            sb.append("#").append(tc).append(" ").append(maxLen).append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }

    public static void main(String[] args) throws Exception {
        input();
    }
}
