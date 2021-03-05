package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14697 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int ans = 0;
        for (int i = 0 ; i <= 50; i++) {
            for (int j = 0 ; j <= 50; j++) {
                for (int k = 0 ; k <= 50; k++) {
                    if ((a * i) + (b * j) + (c * k) == N) ans = 1;
                }
            }
        }
        System.out.println(ans);
        br.close();
    }
}
