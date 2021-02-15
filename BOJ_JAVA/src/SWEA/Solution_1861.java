package SWEA;

import java.io.*;
import java.util.StringTokenizer;

public class Solution_1861 {
    private static int[][] graph;
    private static int N, idx, ans;
    private static int[] dx = {-1, 0, 1, 0};
    private static int[] dy = {0, 1, 0, -1};

    private static void dfs(int x, int y, int cnt, int start) {
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                if ((graph[nx][ny] == graph[x][y] + 1)) {
                    dfs(nx, ny, cnt + 1, start);
                }
            }
        }

        if(cnt > ans) { // 카운트 한 것이 기존의 값보다 많다면
            ans = cnt; // 업데이트
            idx = start; // 카운트 시작한 방번호도 업데이트
        }
        if(cnt == ans) { // 만약 방 갯수가 기존의 것과 같다면
            idx = Math.min(idx, start); // 방번호가 작은 쪽으로 업데이트
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc < T + 1; tc++) {
            N = Integer.parseInt(br.readLine());

            graph = new int[N][N];
            idx = 0;
            ans = 0;

            for (int i = 0; i < N; i++) {
                StringTokenizer st =new StringTokenizer(br.readLine());
                for (int j =0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dfs(i, j, 1, graph[i][j]);
                }
            }
            bw.write("#" + tc + " " + idx + " " + ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
