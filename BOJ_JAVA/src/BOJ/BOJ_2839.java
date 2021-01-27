package BOJ;

import java.io.*;

public class BOJ_2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = 0;
        int x = 0;

        for (int i = n / 5; i >= 0; i--) {
            if ((n - 5 * i) % 3 == 0) {
                x = (n - 5 * i) / 3;
                ans = i + x;
                break;
            } else {
                ans = -1;
            }
        }
        System.out.println(ans);
    }
}
