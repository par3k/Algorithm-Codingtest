package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class BOJ_1261 { // 알고스팟
    private static int m, n;
    private static int[][] graph;
    private static int[][] count;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static void bfs() {
        Deque<Node> queue = new LinkedList<>();
        queue.offer(new Node(0, 0));
        count[0][0] = 0;

        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            int x = node.x;
            int y = node.y;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (count[nx][ny] == -1) {
                        if (graph[nx][ny] == 0) {
                            count[nx][ny] = count[x][y];
                            queue.offerFirst(new Node(nx, ny));
                        } else {
                            count[nx][ny] = count[x][y] + 1;
                            queue.offer(new Node(nx, ny));
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        m = Integer.parseInt(line[0]);
        n = Integer.parseInt(line[1]);

        graph = new int[n][m];
        count = new int[n][m];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = Character.getNumericValue(input.charAt(j));
                count[i][j] = -1;
            }
        }

        bfs();

        StringBuilder sb = new StringBuilder();
        sb.append(count[n][m]);
        System.out.print(sb);
        br.close();
    }

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
