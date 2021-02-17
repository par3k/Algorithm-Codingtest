package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_17135 {
    private static int[] dx = {0, -1, 0};
    private static int[] dy = {-1, 0, 1};
    private static int n, m, d, ans = 0;
    private static int[][] graph;
    private static boolean[] chk;

    private static void Combination(int depth, int start) {
        if (depth == 3) {
            int[][] tmpGraph = new int[n + 1][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    tmpGraph[i][j] = graph[i][j];
                }
            }
            bfs(tmpGraph);
            return;
        }

        for (int i = start; i < m; i++) {
            if (!chk[i]) {
                chk[i] = true;
                Combination(depth + 1, i);
                chk[i] = false;
            }
        }
    }

    private static void bfs(int[][] arr) {
        int cnt = 0;
        for (int i = n; i > 0; i--) {
            int archerIdx = 0;
            Queue<Pair> queue = new LinkedList<>();
            for (int j = 0; j < m; j++) {
                if (chk[j]) {
                    arr[i][j] = 2;
                    queue.add(new Pair(i - 1, j, 1, archerIdx++));
                } else {
                    arr[i][j] = 0;
                }
            }

            boolean[] enemyFind = new boolean[3];
            boolean[][][] visited = new boolean[n][m][3];
            boolean[][] alreadyFind = new boolean[n][m];
            ArrayList<Pair> list = new ArrayList<>();

            while (!queue.isEmpty()) {
                Pair p = queue.poll();
                int x = p.x;
                int y = p.y;
                int idx = p.idx;
                int depth = p.depth;
                if (enemyFind[idx]) continue;

                if (arr[x][y] == 1){
                    enemyFind[idx] = true;
                    if (!alreadyFind[x][y]) {
                        alreadyFind[x][y] = true;
                        list.add(p);
                        cnt++;
                    }
                    continue;
                }
                if (!enemyFind[idx]) {
                    visited[x][y][idx] = true;
                    for (int j = 0; j < 3; j++) {
                        int nx = x + dx[j];
                        int ny = y + dy[j];

                        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                            if (!visited[nx][ny][idx] && depth < d) {
                                queue.add(new Pair(nx, ny, depth + 1, idx));
                            }
                        }
                    }
                }
            }

            for (int j = 0; j < list.size(); j++) {
                Pair p = list.get(j);
                arr[p.x][p.y] = 0;
            }
        }
        ans = Math.max(ans, cnt);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        graph = new int[n + 1][m];
        chk = new boolean[m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        Combination(0, 0);
        System.out.println(ans);

    }

    static class Pair {
        int x, y, depth, idx;

        public Pair(int x, int y, int depth, int idx) {
            this.x = x;
            this.y = y;
            this.depth = depth;
            this.idx = idx;
        }
    }
}
