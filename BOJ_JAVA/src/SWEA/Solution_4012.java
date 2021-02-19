package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_4012 {
    private static int[][] graph;
    private static boolean[] visited;
    private static int N, ans;

    private static void Recursive(int depth, int start) {
        if (N / 2 == depth) {
            checkMin();
            return;
        }

        for (int i = start; i < N; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            Recursive(depth + 1, i + 1); // start : i
            visited[i] = false;
        }
    }

    private static void checkMin() {
        ArrayList<Integer> A = new ArrayList<>();
        ArrayList<Integer> B = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            if (visited[i]) {
                A.add(i);
            } else {
                B.add(i);
            }
        }
        ans = Math.min(Math.abs(addSum(A) - addSum(B)), ans);
    }

    private static int addSum(ArrayList<Integer> tmp) {
        int sum = 0;

        for (int i = 0; i < tmp.size(); i++) {
            for (int j = i; j < tmp.size(); j++) {
                sum += graph[tmp.get(i)][tmp.get(j)] + graph[tmp.get(j)][tmp.get(i)];
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            graph = new int[N][N];
            visited = new boolean[N];
            ans = 1234567890;

            for (int i = 0 ; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            Recursive(0, 0);
            System.out.println("#" + tc + " " +ans);
        }
    }
}
