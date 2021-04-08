package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14502 {
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static int N, M, ans = 0;
    private static int[][] graph, tmp;

    private static void virus(int x, int y) {
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (tmp[nx][ny] == 0) {
                    tmp[nx][ny] = 2;
                    virus(nx, ny);
                }
            }
        }
    }

    private static int cntSafeArea() {
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tmp[i][j] == 0) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private static void dfs(int wall) {
        if (wall == 3) { // 기저 조건 : 벽이 3개를 치는 경우 그래프를 복사해서 tmp에 저장하고 그것에 바이러스를 풀어서 0의 갯수 샌다.
            for (int i = 0 ; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    tmp[i][j] = graph[i][j];
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (tmp[i][j] == 2) {
                        virus(i, j);
                    }
                }
            }
            ans = Math.max(ans, cntSafeArea());
            return;
        }

        for (int i = 0 ; i < N; i++) {
            for (int j =0 ; j < M; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;

                    dfs(wall + 1);
                    graph[i][j] = 0;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        N = Integer.parseInt(str[0]);
        M = Integer.parseInt(str[1]);

        graph = new int[N][M];
        tmp = new int[N][M];

        for (int i = 0 ; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0 ;j  < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);
        System.out.println(ans);
        br.close();
    }
}
