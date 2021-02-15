package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2999 {
    private static int R, C;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        int len = arr.length;

        for (int i = 1; i < len; i++) {
            if (len % i == 0 && i <= len / i) {
                R = Math.max(R, i);
                C = len / R;
            }
        }
        if (R == 0 && C == 0) {
            R = 1;
            C = 1;
        }

        int idx = 0;

        char[][] graph = new char[R][C];

        for (int i = 0; i < C; i++) {
            for (int j = 0; j < R; j++) {
                graph[j][i] = arr[idx++];
            }
        }

        for(int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(graph[i][j]);
            }
        }
    }
}
