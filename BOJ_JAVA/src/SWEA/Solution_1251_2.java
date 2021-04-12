package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1251_2 {

    private static int N;
    private static double E;
    private static long[][] graph;
    private static StringTokenizer st;
    private static BufferedReader br;


    private static void Solution() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());

        for (int t = 1; t <= TC; t++) {
            N = Integer.parseInt(br.readLine());

            int x[] = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0 ; i < N; i++) {
                x[i] = Integer.parseInt(st.nextToken());
            }

            int y[] = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0 ; i < N; i++) {
                y[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < N; j++) {
                    graph[i][j] = graph[j][i] = getDist(x[i], x[j], y[i], y[j]);
                }
            }
            E = Double.parseDouble(br.readLine());
            System.out.println("#" + t + " " + makeMST());
        }
    }

    private static long makeMST() {
        long[] minEdge = new long[N];
        boolean[] visited = new boolean[N];

        Arrays.fill(minEdge, Integer.MAX_VALUE);
        minEdge[0] = 0;
        long result = 0; // 최소 신장트리 비용
        int cnt = 0; // 정점 갯수

        while (true) {
            // 신장 트리의 포함되지 않은 정점 중 최소 간선비용의 정점선택
            long min = Integer.MAX_VALUE;
            int minNo = 0;
            for (int i = 0 ; i < N; i++) {
                if (!visited[i] && min > minEdge[i]) {
                    minNo = i;
                    min = minEdge[i];
                }
            }
            visited[minNo] = true; // 정점이 신장트리에 포함됨
            result += min; // 비용에도 가중치 +

            if (++cnt == N) break; // cnt도 누적되다 N개에 도달하면 while 빠져나옴

            for (int i = 0; i < N; i++) {
                if (!visited[i] && minEdge[i] > graph[minNo][i]) {
                    minEdge[i] = graph[minNo][i];
                }
            } // 전체중 최소를 구하려면 하나씩 하나씩 비교해서 최솟값을 구해야 한다.
        }
        return result;
    }


    private static long getDist(int x1, int x2, int y1, int y2) {
        return (long) Math.pow(x1 - x2, 2) + (long) Math.pow(y1 - y2, 2);
    }

    public static void main(String[] args) throws IOException{

        Solution();
    }

}
