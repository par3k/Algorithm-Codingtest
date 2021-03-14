package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_3040 {

    private static int[] tmp, arr, ans;
    private static void Combination(int depth, int start, int sum) {
        if (depth == 7 && sum == 100) {
            ans = tmp.clone();
            return;
        } else if (depth == 7) return;

        for (int i = start; i < 9; i++) {
            tmp[depth] = arr[i];
            Combination(depth + 1, i + 1, sum + arr[i]);
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[9];
        tmp = new int[7];
        ans = new int[7];

        for (int i = 0; i  < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Combination(0, 0, 0);
        for (int i : ans) {
            System.out.println(i);
        }
        br.close();

    }
}
