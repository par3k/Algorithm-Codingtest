package BOJ;

import java.io.*;

public class BOJ_14650 {
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ans = 0;

        dfs(0, 0, N);
        System.out.println(ans);
        br.close();
    }

    public static void dfs(int n, int sum, int finish) {
        for (int i = 0; i < 3; i++) {
            if (n == 0 && i == 0) continue;

            if (n == finish) {
                if (sum % 3 == 0) {
                    ans++;
                    return;
                }
            } else {
                dfs(n + 1, sum + i, finish);
            }
        }
    }
}
