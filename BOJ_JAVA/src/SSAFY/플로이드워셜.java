import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 플로이드워셜 {
    private static final int INF = 123456789;
    private static int N, M;
    private static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        N = Integer.parseInt(line[0]);
        M = Integer.parseInt(line[1]);
        graph = new int[501][501];

        for (int i = 0 ; i <= N; i++) {
            Arrays.fill(graph[i], INF);
        }

        for (int i = 0 ; i <= N; i++){
            for (int j = 0 ; j <= N; j++) {
                if (i == j) graph[i][j] = 0;
            }
        }

        for (int i = 0 ; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            graph[from][to] = weight;
        }

        for (int k  = 1; k <= N; k++) {
            for (int a = 1; a <= N; a++) {
                for (int b = 1; b <= N; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (graph[i][j] == INF) {
                    System.out.println("INF");
                } else {
                    System.out.print(graph[i][j] + " ");
                }
            }
            System.out.println();
        }

        br.close();
    }


}
