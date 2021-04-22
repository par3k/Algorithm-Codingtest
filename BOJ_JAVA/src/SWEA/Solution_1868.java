package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_1868 { // 파핑파핑 지뢰찾기
    private static char[][] graph;
    private static int[][] mineCNT;
    private static int[] dx = {-1, 1, 0, 0, 1, 1, -1, -1}; // 8방
    private static int[] dy = {0, 0, -1, 1, 1, -1, 1, -1};
    private static int N, ans;

    private static void click(int i, int j) {
        int current = mineCNT[i][j];
        mineCNT[i][j] = -1;

        if (current == 0) {
            for (int d = 0; d < 8; d++) {
                int nx = i + dx[d];
                int ny = j + dy[d];
                if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                    if (graph[nx][ny] != '*' && mineCNT[nx][ny] != -1) {
                        click(nx, ny);
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc ++){
            N = Integer.parseInt(br.readLine());
            graph = new char[N][N];
            ans = 0;
            mineCNT = new int[N][N];
            for (int i = 0 ; i < N; i++) {
                graph[i] = br.readLine().toCharArray();
            } // 그래프 입력

            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < N; j++) {
                    if (graph[i][j] == '.') {
                        int cnt = 0;
                        for (int d= 0; d < 8; d++) {
                            int nx = i + dx[d];
                            int ny = j + dy[d];
                            if (0 <= nx && nx < N && 0 <= ny && ny < N) {
                                if (graph[nx][ny] == '*') {
                                    cnt++;
                                }
                            }
                        }
                        mineCNT[i][j] = cnt;
                    }
                }
            } // 맵에 지뢰 갯수 세기

            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ; j < N ;j ++) {
                    if (mineCNT[i][j] == 0 && graph[i][j] != '*') {
                        click(i, j);
                        ans++;
                    }
                }
            }

            for (int i = 0 ; i < N; i++) {
                for (int j = 0 ;j  < N ; j++) {
                    if (mineCNT[i][j] > 0 && graph[i][j] != '*') {
                        ans++;
                    }
                }
            }
            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        } // tc end
        System.out.print(sb);
        br.close();
    }
}
