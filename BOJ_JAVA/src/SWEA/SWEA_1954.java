package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_1954 {
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};

    private static int N;
    private static int[][] graph;

    public static int[][] snail() {
        graph = new int[N][N];
        Pair p = new Pair(0, 0);
        int val = 1;
        int dir = 0;

        while (true) {
            graph[p.x][p.y] = val++;
            if (val > N * N) break;

            int nx = p.x + dx[dir];
            int ny = p.y + dy[dir];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                dir = (dir + 1) % 4;
                nx = p.x + dx[dir];
                ny = p.y + dy[dir];
            }

            if (graph[nx][ny] != 0) {
                dir = (dir + 1) % 4;
                nx = p.x + dx[dir];
                ny = p.y + dy[dir];
            }

            p.x = nx;
            p.y = ny;
        }
        return graph;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc < T + 1; tc++) {
            N = Integer.parseInt(br.readLine());
            snail();
            System.out.println("#" + tc);

            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    System.out.print(graph[x][y] + " ");
                }
                System.out.println();
            }
        }
    }
}

class Pair {
    int x, y;
    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}