package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_1954 {
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc < T + 1; tc++) {
            int N = Integer.parseInt(br.readLine());

            if (N == 1) {
                System.out.println("#" + tc);
                System.out.println(1);
                continue;
            }

            int[][] graph = new int[N][N];

            int x = 0;
            int y = 0;
            int dir = 0;

            for (int i = 0; i < N * N; i++) {
                graph[x][y] = i + 1;
                x += dx[dir];
                y += dy[dir];

                if (x < 0 || x >= N || y < 0 || y >= N) {
                    x -= dx[dir];
                    y -= dy[dir];

                    dir = (dir + 1) % 4;

                    x += dx[dir];
                    y += dy[dir];
                }

                if (graph[x][y] != 0) {
                    x -= dx[dir];
                    y -= dy[dir];

                    dir = (dir + 1) % 4;

                    x += dx[dir];
                    y += dy[dir];
                }
            }
            System.out.println("#" + tc);
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.print(graph[i][j] + " ");
                }
                System.out.println();
            }
        }
    }
}
