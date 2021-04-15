package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_15685 { // 드래곤 커브
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, -1, 0, 1};
    private static int N, x, y, d, g;
    private static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[101][101];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            g = Integer.parseInt(st.nextToken());
            graph[x][y] = 1;
            int[] arr_g = new int[(int) Math.pow(2, g)];
            arr_g[0] = d;
            for (int j = 0 ; j< g; j++) {
                for (int k = (int) Math.pow(2, j); k < (int) Math.pow(2, j + 1); k++) {
                    arr_g[k] = (arr_g[(int) Math.pow(2, j + 1) - (k + 1)] + 1) % 4;
                }
            }
            for (int k : arr_g) {
                x += dx[k];
                y += dy[k];
                graph[x][y] = 1;
            }
        }

        int answer = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0 ; j <100; j++) {
                if (graph[i][j] == 1) {
                    if (graph[i + 1][j] == 1 && graph[i][j + 1] == 1 && graph[i + 1][j + 1] == 1) {
                        answer++;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(answer);
        System.out.println(sb);
        br.close();
    }
}
