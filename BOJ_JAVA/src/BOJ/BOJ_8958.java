package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < n; i++) {
            char[] a = br.readLine().toCharArray();
            int cnt = 0;
            int ans = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[j] == 'O') {
                    cnt++;
                    ans += cnt;
                }
                if (a[j] == 'X') {
                    cnt = 0;
                }
            }
            System.out.println(ans);
        }
    br.close();
    }
}
