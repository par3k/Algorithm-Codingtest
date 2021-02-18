package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());



        for (int i = 0; i < N; i++) {
            char[] str = br.readLine().toCharArray();
            int ans = 0;
            for (int j = 0; j < str.length; j++) {
                if (str[j] == 'O') {
                    ans = ans + 1;
                } else if (str[j] == 'X') {
                    ans--;
                    if (ans < 0) ans = 0;
                }
            }
            System.out.println(ans);
        }

    }
}
