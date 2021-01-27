package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2675 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st= new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            String S = st.nextToken();

            for (int j = 0; j < S.length(); j++) {
                for (int a = 0; a < R; a++) {
                    System.out.print(S.charAt(j));
                }
            }

            System.out.println();
        }
    }
}
