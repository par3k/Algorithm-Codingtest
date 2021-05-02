package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_5515 {
    private static int m, d, diff, ans;
    private static int[] days = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
                diff = 0;
                ans = 4;
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());

            if (m == 1) diff = d - 1;
            else {
                for (int i = 2; i < m; i++) {
                    diff += days[i];
                }
                diff = diff + 30 + d;
            }
            int tmp = diff % 7;
            if (tmp <= 2) {
                ans += tmp;
            } else {
                ans = ans + tmp - 7;
            }
            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}
