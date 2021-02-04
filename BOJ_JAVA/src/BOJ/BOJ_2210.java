package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2210 {
    private static int[][] graph;
    private static int[] arr;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int ans;

    private static void dfs(int x, int y, String str) {
        if (str.length() == 6 && arr[Integer.parseInt(str)] == 0) {
            arr[Integer.parseInt(str)] = 1;
            ans++;
            return;
        } else {
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < 5 && 0 <= ny && ny < 5) {
                    if (str.length() != 6) {
                        dfs(nx, ny, str + graph[nx][ny]);
                    }
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        graph = new int[5][5];
        arr = new int[1000000];
        String str = "";

        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if (0 <= nx && nx < 5 && 0 <= ny && ny < 5) {
                        if (str.length() != 6) {
                            dfs(nx, ny, str + graph[nx][ny]);
                        }
                    }
                }
            }
        }
        System.out.println(ans);
        br.close();
    }
}
