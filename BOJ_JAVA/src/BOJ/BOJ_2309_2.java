package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_2309_2 {
    private static int[] arr, num, ans;

    private static void Combination(int depth, int start, int sum) {
        if (depth == 7 & sum == 100) {
            ans = num.clone();
            return;
        } else if (depth == 7) return;

        for (int i = start; i < 9; i++) {
            num[depth] = arr[i];
            Combination(depth + 1, i + 1,sum + arr[i]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        arr = new int[9];
        num = new int[7];

        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Combination(0, 0, 0);
        Arrays.sort(ans);
        for (int i : ans) System.out.println(i);
        br.close();
    }
}
