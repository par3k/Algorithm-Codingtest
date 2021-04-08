package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14889 {
    private static int[][] graph;
    private static int[] select;
    private static int N, ans;

    private static void dfs(int idx, int depth) {
        if (depth == N / 2) {
            int start = 0;
            int link = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0 ; j < N; j ++) {
                    if (select[i] != 0 && select[j] != 0) {
                        start += graph[i][j];
                    } else if (select[i] == 0 && select[j] == 0) {
                        link += graph[i][j];
                    }
                }
            }
            ans = Math.min(ans, Math.abs(start - link));
        }

        for (int i = idx; i < N; i++) {
            if (select[i] != 0) {
                continue;
            }
            select[i] = 1;
            dfs(i + 1, depth + 1);
            select[i] = 0;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];
        select = new int[N];
        ans = 123456789;


        for (int i = 0 ; i < N; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0, 0);
        System.out.println(ans);
        br.close();
    }
}
