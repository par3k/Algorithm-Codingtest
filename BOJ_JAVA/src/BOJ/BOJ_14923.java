package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_14923 {
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int N, M, hx, hy, ex, ey;
    private static int[][] graph;
    private static boolean[][][] visited;

    private static int bfs(){
        int ans = 0;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(hx, hy, 0));
        visited = new boolean[N][M][2];
        visited[hx][hy][0] = true;

        while (!queue.isEmpty()) {
            ++ans;
            int size = queue.size();
            while (size > 0) {
                Node node = queue.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = node.x + dx[i];
                    int ny = node.y + dy[i];

                    if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                        if (graph[nx][ny] == 1) { // 벽을 만나
                            if (node.cnt == 0 && !visited[nx][ny][node.cnt + 1]) { // 마법을 아직 안써
                                if (nx == ex && ny == ey) return ans;
                                queue.offer(new Node(nx, ny, node.cnt + 1));
                                visited[nx][ny][node.cnt + 1] = true;
                            }
                        } else { // 길을 가
                            if (!visited[nx][ny][node.cnt]) {
                                if (nx == ex && ny == ey) return ans;
                                queue.offer(new Node(nx, ny, node.cnt));
                                visited[nx][ny][node.cnt] = true;
                            }
                        }
                    }
                }
                size--;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        M = Integer.parseInt(line[1]);
        graph = new int[N][M];

        StringTokenizer st = new StringTokenizer(br.readLine());
        hx = Integer.parseInt(st.nextToken()) - 1;
        hy = Integer.parseInt(st.nextToken()) - 1;

        st = new StringTokenizer(br.readLine());
        ex = Integer.parseInt(st.nextToken()) - 1;
        ey = Integer.parseInt(st.nextToken()) - 1;

        for (int i = 0 ; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(bfs()).append("\n");
        System.out.print(sb);
        br.close();
    }

    private static class Node {
        int x, y, cnt;

        public Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
