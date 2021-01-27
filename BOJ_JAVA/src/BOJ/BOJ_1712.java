package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_1712 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());

        if (c <= b) {
            System.out.println("-1");
        } else {
            for (int n = 0; ; n++) {
                long made_price = a + (b * n);
                long selling_price = c * n;

                if (made_price < selling_price) {
                    System.out.println(n);
                    break;
                }
            }
        }
    }
}
