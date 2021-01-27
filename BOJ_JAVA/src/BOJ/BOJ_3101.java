package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3101 {
    static int n, m, x = 1, y = 1;
    static long allSum = 1;
    static long[] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        init();
        char[] input = br.readLine().toCharArray();

        for (int i = 0; i < m; i++) {
            switch (input[i]) {
                case 'U':
                    if (x > n)
                        ++y;
                    --x;
                    break;
                case 'D':
                    if (x >= n)
                        --y;
                    ++x;
                    break;
                case 'L':
                    if (x <= n)
                        --y;
                    --x;
                    break;
                case 'R':
                    if (x < n)
                        ++y;
                    ++x;
                    break;
            }
            allSum += calc(x, y);
        }
        System.out.println(allSum);
    }
    private static void init() {
        dp = new long[n * 2 + 1];
        for (int i = 1; i < n * 2; ++i) {
            dp[i] = dp[i - 1] + chk(i);
        }
    }
    private static long calc(int x, int y) {
        long res = 0;
        if (x % 2 == 1) {
            res = dp[x - 1] + y;
        } else {
            res = dp[x] - y + 1;
        }
        return res;
    }
    private static long chk(int i) {
        return i > n ? n - i % n : i;
    }
}
