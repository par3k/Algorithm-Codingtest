package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2961 {
    private static int N, ans;
    private static int[] S, B;
    private static boolean[] flag;

    private static void Permutation(int depth, int sour, int bitter) {
        if (depth == N) {
            if (ans > Math.abs(sour - bitter) && bitter != 0) {
                ans = Math.abs(sour - bitter);
            }
            return;
        }
        flag[depth] = true;
        Permutation(depth + 1, sour * S[depth], bitter + B[depth]);
        flag[depth] = false;
        Permutation(depth + 1, sour, bitter);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        S = new int[N];
        B = new int[N];
        flag = new boolean[N];

        ans = 123456789;

        for (int i = 0 ; i < N; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            S[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
        }
        Permutation(0, 1, 0);
        System.out.println(ans);
    }
}
