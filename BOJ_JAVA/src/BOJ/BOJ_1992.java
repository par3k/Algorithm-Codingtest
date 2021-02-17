package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1992 {
    private static StringBuilder sb = new StringBuilder();
    private static char[][] graph;
    private static int N;

    private static void Recursive (int size, int x, int y) {
        int val = graph[y][x];
        boolean flag = false;
        for (int i = y; i < y + size; i++){
            for (int j = x; j < x + size; j++) {
                if (val != graph[i][j]) flag = true;
            }
        }

        if (!flag) {
            sb.append(graph[y][x]);
            return;
        }

        sb.append('(');
        Recursive(size / 2, x, y);
        Recursive(size / 2, x + size / 2, y);
        Recursive(size / 2, x, y + size / 2);
        Recursive(size / 2, x + size / 2, y + size / 2);
        sb.append(')');
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new char[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            graph[i] = st.nextToken().toCharArray();
        }
        Recursive(N, 0, 0);
        System.out.println(sb);
        br.close();
    }
}