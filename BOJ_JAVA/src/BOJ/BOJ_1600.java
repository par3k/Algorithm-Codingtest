package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1600 {
    private static int K, W, H, ans;
    private static int[][] graph;
    private static int[][][] visited;
    private static Queue<Node> queue;

    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static int[] horse_dx = {2, 1, 2, 1, -2, -1, -2, -1};
    private static int[] horse_dy = {1, 2, -1, -2, 1, 2, -1, -2};

    private static int bfs() {
        while (!queue.isEmpty()) {
            Node monkey = queue.poll();
            int x = monkey.x;
            int y = monkey.y;
            int k = monkey.k;
            int cnt = monkey.cnt;
            if (x == H - 1 && y == W - 1) {
                ans = visited[x][y][k];
                break;
            }

            if (k < K) {
                for (int d = 0; d < 8; d++) {
                    int nx = x + horse_dx[d];
                    int ny = y + horse_dy[d];
                    if (0 <= nx && nx < H && 0 <= ny && ny < W) {
                        if (visited[nx][ny][k + 1] == 0 && graph[nx][ny] == 0) {
                            visited[nx][ny][k + 1] = cnt + 1;
                            queue.offer(new Node(nx, ny, k + 1, cnt + 1));
                        }
                    }
                }
            }

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (0 <= nx && nx < H && 0 <= ny && ny < W) {
                    if (visited[nx][ny][k] == 0 && graph[nx][ny] == 0) {
                        visited[nx][ny][k] = cnt + 1;
                        queue.offer(new Node(nx, ny, k, cnt + 1));
                    }
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        String[] line = br.readLine().split(" ");
        W = Integer.parseInt(line[0]);
        H = Integer.parseInt(line[1]);

        graph = new int[H][W];
        visited = new int[H][W][K + 1];

        for (int i = 0;i < H; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < W; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        ans = -1;
        queue = new LinkedList<>();
        queue.offer(new Node(0, 0, 0, 0));
        visited[0][0][0] = 0;
        System.out.println(bfs());
        br.close();

    }


    private static class Node {
        int x, y, k, cnt;

        public Node(int x, int y, int k, int cnt) {
            this.x = x;
            this.y = y;
            this.k = k;
            this.cnt = cnt;
        }
    }
}
