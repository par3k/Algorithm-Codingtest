package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3234 {

    private static int N, ans;
    private static int[] input, res;
    private static boolean[] chk;

    private static void Permutation(int depth) {
        if (depth == N) {
            check(0, 0, 0);
            return;
        }

        for (int i = 0 ; i < N; i++) {
            if (chk[i]) continue;
            chk[i] = true;
            res[depth] = input[i];
            Permutation(depth + 1);
            chk[i] = false;
        }
    }

    private static void check(int idx, int sumLeft, int sumRight) {
        if (idx == N) {
            ans++;
            return;
        }
        check(idx + 1, sumLeft + res[idx], sumRight);
        if (sumRight + res[idx] <= sumLeft) check(idx + 1, sumLeft, sumRight + res[idx]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            input = new int[N];
            chk = new boolean[N + 1];
            res = new int[N];
            ans = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                input[i] = Integer.parseInt(st.nextToken());
            }

            Permutation(0);
            System.out.println("#" + tc + " " + ans);
        }
    }
}
