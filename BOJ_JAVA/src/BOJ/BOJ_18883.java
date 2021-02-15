package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_18883 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();
        int cnt = 1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (j != 0) {
                    sb.append(' ');
                }
                sb.append(cnt++);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}
