package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_15649 {
    private static int[] ans;
    private static boolean[] check;

    private static void recursive(int idx,int n,int m) {
        if (idx == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
        }

        for (int i = 1; i < n + 1; i++) {
            if (check[i]) {
                continue;
            }

            check[i] = true;
            ans[idx] = i;
            recursive(idx + 1, n, m);
            check[i] = false;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        check = new boolean[8];
        ans = new int[8];

        recursive(0, N, M);

    }
}
