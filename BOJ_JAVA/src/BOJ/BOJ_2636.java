package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2636 {
    private static int N, M;
    private static int[][] graph;
    private static boolean[][] visited;
    private static Queue<Node> queue;

    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static int bfs(int leftCheese) {
        while (!queue.isEmpty()){
            Node node = queue.poll();
            int x = node.x;
            int y = node.y;

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    if (graph[nx][ny] == 1) {
                        graph[nx][ny] = 2;
                        leftCheese--;
                    } else{
                        queue.offer(new Node(nx, ny));
                    }
                }
            }
        }
        return leftCheese;
    }

    private static void remove() {
        for (int i = 0 ; i < N; i++) {
            for (int j = 0 ; j< M; j++) {
                if (graph[i][j] == 2) {
                    graph[i][j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        M = Integer.parseInt(line[1]);

        graph = new int[N][M];
        int leftCheese = 0;
        for (int i = 0 ; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) leftCheese++;
            }
        }

        queue = new LinkedList<>();
        int cnt = 0;
        int tmp = leftCheese;

        while (leftCheese != 0) {
            visited = new boolean[N][M];
            queue.offer(new Node(0, 0));
            visited[0][0] = true;

            leftCheese = bfs(leftCheese);
            if (leftCheese != 0) tmp = leftCheese;
            cnt++;
            remove();
        }

        StringBuilder sb = new StringBuilder();
        sb.append(cnt).append("\n").append(tmp);
        System.out.println(sb);
        br.close();
    }
    private static class Node{
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
