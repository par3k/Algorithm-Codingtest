package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_16922 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[] chk = new boolean[100000];

        for (int i = 0 ; i <= N; i++) {
            for (int j = 0 ; j <= N - i; j++) {
                for (int k = 0 ; k <= N - i - j; k++) {
                    int tmp = N - i - j - k;
                    int sum = i + j * 5 + k * 10 + tmp * 50;
                    chk[sum] = true;
                }
            }
        }
        int ans = 0;
        for (int i = 1 ; i < chk.length; i++) {
            if (chk[i]) ans++;
        }
    System.out.println(ans);
    br.close();
    }
}
