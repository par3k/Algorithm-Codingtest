package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_15653 {
    private static char[][] graph;
    private static int N, M;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static boolean[][][][] visited;
    private static Queue<Pair> queue;
    private static int Redx, Redy, Bluex, Bluey;

    private static int bfs() {
        while (!queue.isEmpty()) {
            Pair blue, red;

            if (queue.peek().ty == 'B') {
                blue = queue.poll();
                red = queue.poll();
            } else {
                red = queue.poll();
                blue = queue.poll();
            }

            boolean blueFin, redFin, afterR;
            int bx, by, rx, ry;
            int bnx, bny, rnx, rny;

            for (int i = 0; i < 4; i++) {
                blueFin = false;
                redFin = false;
                afterR = false;

                bx = blue.x;
                by = blue.y;
                rx = red.x;
                ry = red.y;

                while (true) {
                    bnx = bx + dx[i];
                    bny = by + dy[i];
                    if (bnx == rx && bny == ry) afterR = true;
                    if (graph[bnx][bny] == '#') break;
                    if (graph[bnx][bny] == 'O') {
                        blueFin = true;
                        break;
                    }
                    bx = bnx;
                    by = bny;
                }

                while (true) {
                    rnx = rx + dx[i];
                    rny = ry + dy[i];
                    if (graph[rnx][rny] == '#') break;
                    if (graph[rnx][rny] == 'O') {
                        redFin = true;
                        break;
                    }
                    rx = rnx;
                    ry = rny;
                }

                if (blueFin) continue;
                if (redFin) return red.time + 1;

                if (bx == rx && by == ry) {
                    if (afterR) {
                        bx -= dx[i];
                        by -= dy[i];
                    } else {
                        rx -= dx[i];
                        ry -= dy[i];
                    }
                }
                if (visited[rx][ry][bx][by]) continue;
                visited[rx][ry][bx][by] = true;

                queue.offer(new Pair(bx, by, blue.time + 1, 'B'));
                queue.offer(new Pair(rx, ry, red.time + 1,  'R'));
            }
        }
       return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new char[N][M];
        visited = new boolean[N][M][N][M];

        queue = new LinkedList<>();

        for (int i = 0 ; i < N; i++) {
            char[] c = br.readLine().toCharArray();
            for (int j = 0 ; j < M; j++) {
                if(c[j] == 'R') {
                    graph[i][j] = '.';
                    Redx = i;
                    Redy = j;
                    queue.offer(new Pair(i, j, 0, c[j]));
                } else if (c[j] == 'B') {
                    graph[i][j] = '.';
                    Bluex = i;
                    Bluey = j;
                    queue.offer(new Pair(i, j, 0, c[j]));
                } else {
                    graph[i][j] = c[j];
                }
            }
        }

        visited[Redx][Redy][Bluex][Bluey] = true;
        System.out.println(bfs());
    }

    static class Pair {
        int x, y, time;
        char ty;

        public Pair(int x, int y, int time, char ty) {
            this.x = x;
            this.y = y;
            this.time = time;
            this.ty = ty;
        }
    }
}
