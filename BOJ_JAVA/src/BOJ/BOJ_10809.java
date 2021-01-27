package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10809 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        byte[] s = br.readLine().getBytes();
        byte[] alpha = new byte[26];
        for (int i = 0; i < alpha.length; i++) {
            alpha[i] = -1;
        }

        for (int i = 0; i < s.length; i++) {
            if (alpha[s[i] - 'a'] == -1) {
                alpha[s[i] - 'a'] = (byte)i;
            }
        }
        for (int ans : alpha) {
            System.out.println(ans + " ");
        }
    }
}
