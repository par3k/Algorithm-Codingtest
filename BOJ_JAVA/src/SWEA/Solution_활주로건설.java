package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_활주로건설 {
    private static int N, X;
    private static int[][] graph, graph2;

    private static int Solve(int[] arr, int x) {
        int cnt = 1;
        int before = arr[0];

        for (int i = 1 ; i  < arr.length; i++) {
            if (arr[i] < before) {
                if (before - arr[i] > 1) {
                    return 0;
                } else {
                    if ((i + x) > arr.length) {
                        return 0;
                    } else {
                        for (int j = i; j < i + x; j++) {
                            if (arr[j] != arr[i]) {
                                return 0;
                            }
                        }
                        cnt = -x +1;
                    }
                }
            } else if (arr[i] > before) {
                if (arr[i] - before > 1) {
                    return 0;
                } else {
                    if (cnt >= x) {
                        cnt = 1;
                    } else {
                        return 0;
                    }
                }
            } else {
                cnt++;
            }
            before = arr[i];
        }
        return 1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc ++ ){
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            X = Integer.parseInt(st.nextToken());
            graph = new int[N][N];
            graph2 = new int[N][N];


            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0 ; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0 ; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    graph2[j][i] = graph[i][j];
                }
            }


            int answer = 0;
            for (int i = 0 ; i < N; i++) {
                answer += Solve(graph[i], X);
            }

            for (int i = 0 ; i < N; i++) {
                answer += Solve(graph2[i], X);
            }

            StringBuilder sb = new StringBuilder();
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
            System.out.print(sb);
        }
    }
}
