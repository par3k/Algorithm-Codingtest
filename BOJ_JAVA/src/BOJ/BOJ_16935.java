package BOJ;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_16935 {
    private static int N, M, R;
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};
    private static int[][] graph;
    private static ArrayList<Integer> op;

    private static int[][] copy(int[][] arr) {
        int[][] tmp = new int[arr.length][arr[0].length];
        for (int i = 1; i <= arr.length - 1; i++) {
            for (int j = 1; j <= arr[0].length - 1; j++) {
                tmp[i][j] = arr[i][j];
            }
        }
        return tmp;
    }

    private static void one() { // 상하 반전
        for (int i = 1; i <= graph.length / 2; i++) {
            int[] tmp = graph[i];
            graph[i] = graph[graph.length - i];
            graph[graph.length - i] = tmp;
        }
    }

    private static void two() { // 좌우 반전
      for (int i = 1; i <= graph.length; i++) {
          for (int j = 1; j <= graph[i].length / 2; i++) {
              int tmp = graph[i][j];
              graph[i][j] = graph[i][graph[i].length - j];
              graph[i][graph[i].length - j] = tmp;
          }
      }
    }

    private static void three() { // 오른쪽으로 90도 회전
        int[][] tmp = copy(graph);
        N = tmp.length - 1;
        M = tmp[0].length - 1;

        graph = new int[M + 1][N + 1];

        for (int i = 1, j = N; j >= 1; j--, i++) {
            for (int k = 1; k <= M; k++) {
                graph[k][j] = tmp[i][k];
            }
        }
    }

    private static void four() { // 왼쪽으로 90도 회전
        int[][] tmp = copy(graph);
        N = tmp.length - 1;
        M = tmp[0].length - 1;

        graph = new int[M + 1][N + 1];

        for (int i = 1, j = 1; j <= N; j++, i++) {
            for (int k = 1; k <= M; k++) {
                graph[k][j] = tmp[i][M - k + 1];
            }
        }
    }

    private static void five() { // 1 > 2, 2 > 3, 3 > 4, 4 > 1 이동
        int[][] tmp = copy(graph);
        N = tmp.length - 1;
        M = tmp[0].length - 1;

        for (int i = 1; i <= N / 2; i++) { // 1 > 2
            for (int j = 1; j <= M / 2; j++) {
                graph[i][M / 2 + j] = tmp[i][j];
            }
        }

        for (int i = N / 2 + 1; i <= N; i++) { // 3 > 4
            for (int j = M / 2 + 1; j <= M; j++) {
                graph[i][j - M / 2] = tmp[i][j];
            }
        }

        for (int i = 1; i <= N /2; i++) { // 2 > 3
            for (int j = M / 2 + 1; j <= M; j++) {
                graph[i + N / 2][j] = tmp[i][j];
            }
        }

        for (int i = N / 2 + 1; i <= N; i++) { // 4 > 1
            for (int j = 1; j<= M / 2; j++) {
                graph[i - N / 2][j] = tmp[i][j];
            }
        }
    }

    private static void six() { // 1 > 4, 4 > 3, 3 > 2, 2 > 1 이동
        int[][] tmp = copy(graph);
        N = tmp.length - 1;
        M = tmp[0].length - 1;

        for (int i = 1; i <= N / 2; i++) { // 1 > 4
            for (int j = 1; j <= M / 2; j++) {
                graph[i + N / 2][j] = tmp[i][j];
            }
        }

        for (int i = N / 2; i <= N; i++) { // 4 > 3
            for (int j = 1; j <= M / 2; j++) {
                graph[i][M / 2 + j] = tmp[i][j];
            }
        }

        for (int i = N / 2 + 1; i <= N; i++) { // 3 > 2
            for (int j = M / 2 + 1; j <= M; j++) {
                graph[i - N / 2][j] = tmp[i][j];
            }
        }

        for (int i = 1; i <= N / 2; i++) {
            for (int j = M / 2 + 1; j <= M; j++) {
                 graph[i][j - M / 2] = tmp[i][j];
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        graph = new int[N + 1][M + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        op = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < R; i++) {
            op.add(Integer.parseInt(st.nextToken()));
        }

        for (int i : op) {
            switch (i) {
                case 1: one(); break;
                case 2: two(); break;
                case 3: three(); break;
                case 4: four(); break;
                case 5: five(); break;
                case 6: six(); break;
            }
        }

        for (int i = 1; i < graph.length; i++) {
            for (int j = 1; j < graph[i].length; j++) {
                bw.append(graph[i][j] +" ");
            }
            bw.newLine();
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
