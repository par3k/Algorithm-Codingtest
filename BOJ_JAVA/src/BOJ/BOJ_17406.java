package BOJ;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17406 {
    private static int N, M, K;
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};
    private static int[][] graph;

    private static void rotate(int start_x, int start_y, int end_x, int end_y, int depth) {
        for (int i = 0; i < depth; i++) {
            int x = start_x + i;
            int y = start_y + i;
            int dir = 0;
            int tmp = graph[x][y];

            while (dir < 4) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (x <= nx && nx < end_x && y <= ny && ny < end_y) {
                    graph[x][y] = graph[nx][ny];
                    x = nx;
                    y = ny;
                } else {
                    dir++;
                }
            }

            graph[i + 1][i] = tmp;
        }
    }



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());

            rotate(r - s, c - s, r + s, c + s, s);
        }

        for (int i = 0; i <N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }
}
