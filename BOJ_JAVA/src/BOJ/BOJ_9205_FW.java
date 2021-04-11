package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_9205_FW {
    private static final int INF = (int) 1e9;
    private static int N, M;
    private static int[][] location;
    private static int[][] distance;

    private static void mapping() {
        for (int i = 0; i < M; i++) {
            for (int j = 0 ;j < M; j++) {
                int dis = Math.abs(location[i][0] - location[j][0]) + Math.abs(location[i][1] - location[j][1]);
                distance[i][j] = dis > 1000 ? INF : 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            M = N + 2;
            location = new int[M][2];
            distance = new int[M][M];

            for (int i = 0 ; i < M ; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                location[i][0] = Integer.parseInt(st.nextToken());
                location[i][1] = Integer.parseInt(st.nextToken());
            }
            mapping();

            for (int k = 0; k < M; k++) {
                for (int i = 0;  i <M; i ++) {
                    if (k == i) continue;
                    for (int j = 0 ; j < M; j ++) {
                        if (distance[i][j] > distance[i][k] + distance[k][j]) {
                            distance[i][j] = distance[i][k] + distance[k][j];
                        }
                    }
                }
            }
            System.out.println(distance[0][M - 1] == INF ? "sad" : "happy");
        }
        br.close();
    }
}
