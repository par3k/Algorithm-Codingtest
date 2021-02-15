package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_16956 {
    private static int R, C;
    private static char[][] graph;

    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];
        boolean flag = true;

        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                graph[i][j] = str.charAt(j);
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graph[i][j] == 'W') {
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = i + dx[dir];
                        int ny = j + dy[dir];

                        if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                            if (graph[nx][ny] == '.') {
                                graph[nx][ny] = 'D';
                            } else if (graph[nx][ny] == 'S') {
                                flag = false;
                            }
                        }
                    }
                }
            }
        }

        if (!flag) {
            System.out.println(0);
        } else {
            System.out.println(1);
            for (int i =0 ; i < R; i++) {
                for (int j =0; j < C; j++) {
                    System.out.print(graph[i][j]);
                }
                System.out.println();
            }
        }
    }
}
