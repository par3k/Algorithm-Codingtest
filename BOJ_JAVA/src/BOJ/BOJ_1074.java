package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1074 {
    private static int N, r, c, cnt;
    private static void Recursive(int N, int r, int c) {
        int l = (int) Math.pow(2, N - 1);
        if (r >= l) cnt += Math.pow(4, N - 1) * 2;
        if (c >= l) cnt += Math.pow(4, N - 1);
        if (r > 0 || c > 0) {
            Recursive(N - 1, r >= l ? r - l : r, c >= l ? c - l : c);
        } else {
            return;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        Recursive(N, r, c);

        System.out.println(cnt);
    }
}
