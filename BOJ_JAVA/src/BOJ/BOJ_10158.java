package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10158 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(br.readLine());

        int a = (p + t) / w;
        int b = (q + t) / h;
        int x =0, y = 0;

        if (a % 2 == 0) {
            x = (p + t) % w;
        } else {
            x = w - (p + t) % w;
        }

        if (b % 2 == 0) {
            y = (q + t) % h;
        } else {
            y = h - (q + t) % h;
        }
        System.out.println(x + " " + y);
        br.close();
    }
}
