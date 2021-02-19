package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_8320 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = i; i * j <= N; j++) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}
