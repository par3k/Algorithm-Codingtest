package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_5427 {
    private static int w, h, step;
    private static boolean flag;
    private static char[][] graph;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static Queue<Node> queue, fire_queue;

    private static void logic() {
        while (!fire_queue.isEmpty() || !queue.isEmpty()) {
            int fqlen = fire_queue.size();
            for (int s = 0; s < fqlen; s++) {
                Node f = fire_queue.poll();

                for (int d = 0; d < 4; d++) {
                    int nx = f.x + dx[d];
                    int ny = f.y + dy[d];

                    if (0 <= nx && nx < h && 0 <= ny && ny < w) {
                        if (graph[nx][ny] == '.' || graph[nx][ny] == '@') {
                            graph[nx][ny] = '*';
                            fire_queue.add(new Node(nx, ny));
                        }
                    }
                }
            }

            int qlen = queue.size();
            if (qlen > 0) {
                step++;

                for (int s = 0; s < qlen; s++) {
                    Node n = queue.poll();

                    for (int d = 0; d < 4; d++) {
                        int nx = n.x + dx[d];
                        int ny = n.y + dy[d];

                        if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                            flag = true;
                            return;
                        }

                        if (graph[nx][ny] == '.') {
                            graph[nx][ny] = '@';
                            queue.add(new Node(nx, ny));
                        }
                    }
                }
            } else {
                return;
            }
        }
    }


    public static void main (String[]args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            graph = new char[h][w];
            flag = false;
            step = 0;

            for (int i = 0; i < h; i++) {
                graph[i] = br.readLine().toCharArray();
            }

            queue = new ArrayDeque<>();
            fire_queue = new ArrayDeque<>();


            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (graph[i][j] == '@') {
                        queue.add(new Node(i, j));
                    }
                    if (graph[i][j] == '*') {
                        fire_queue.add(new Node(i, j));
                    }
                }
            }
            logic();
            System.out.println(flag == true ? step : "IMPOSSIBLE");
        }
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