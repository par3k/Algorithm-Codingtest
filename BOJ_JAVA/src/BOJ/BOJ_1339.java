package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1339 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] alpha = new int[26];

        int ans = 0;
        int val = 9;

        for (int i = 0 ;i < N; i++) {
            char[] arr = br.readLine().toCharArray();
            int pos = (int) Math.pow(10, arr.length - 1);

            for (int j =0 ; j < arr.length; j++) {
                alpha[arr[j] - 'A'] += pos;
                pos /= 10;
            }
        }

        Arrays.sort(alpha);

        for (int i = alpha.length - 1; i >= 0; i--) {
            if (val == 0) break;
            ans += alpha[i] * val--;
        }
        System.out.println(ans);

    }
}
