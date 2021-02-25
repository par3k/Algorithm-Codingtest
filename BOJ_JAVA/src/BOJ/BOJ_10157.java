package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10157 {
    private static int[] dx = {-1, 0, 1, 0};
    private static int[] dy = {0, 1, 0, -1};
    private static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int c = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());
        graph = new int[r][c];

        if (c * r < k) {
            System.out.println(0);
            System.exit(0);
        }
        int x = r - 1;
        int y = 0;
        int i = 0;
        int cnt = 1;

        while (cnt != k) {
            graph[x][y] = cnt;
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= r || ny >= c || graph[nx][ny] != 0) {
                i++;
                if (i == 4) i = 0;
                nx = x + dx[i];
                ny = y + dy[i];
            }
            x = nx;
            y = ny;
            cnt++;
        }
        sb.append(y+1).append(" ").append(r-x);
        System.out.println(sb);
        br.close();
    }
}
