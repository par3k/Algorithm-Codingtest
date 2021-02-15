package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1012 {
    private static int M, N, K;
    private static int[][] graph;
    private static boolean[][] visited;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

//    private static void dfs(int x, int y) {
//       visited[x][y] = true;
//       for (int i =0 ; i < 4; i++) {
//           int nx = x + dx[i];
//           int ny = y + dy[i];
//
//           if (0 <= nx && nx < M && 0 <= ny && ny < N) {
//               if (!visited[nx][ny] && graph[nx][ny] == 1) {
//                   dfs(nx, ny);
//               }
//           }
//       }
//    }

    private static void bfs(int x, int y) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(x, y));
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            x = node.x;
            y = node.y;
            visited[x][y] = true;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < M && 0 <= ny && ny < N) {
                    if (!visited[nx][ny] && graph[nx][ny] == 1) {
                        queue.offer(new Node(nx, ny));
                        visited[nx][ny] = true;
                    }
                }

            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            graph = new int[M][N];
            visited = new boolean[M][N];

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                graph[X][Y] = 1;
            }

            int cnt = 0;
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < N; j++) {
                    if (graph[i][j] == 1 && !visited[i][j]) {
                        cnt++;
                        bfs(i, j);

                    }
                }
            }
            System.out.println(cnt);
        }
    }
}

class Node {
    int x;
    int y;
    public Node (int x, int y) {
        this.x = x;
        this.y = y;
    }
}