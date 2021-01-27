package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2908 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        while (st.hasMoreElements()) {
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            int AA = ((A % 10) * 100) + (((A / 10) % 10) * 10) + (A / 100);
            int BB = ((B % 10) * 100) + (((B / 10) % 10) * 10) + (B / 100);

            if (AA > BB) {
                System.out.println(AA);
            } else {
                System.out.println(BB);
            }
        }
    }
}
