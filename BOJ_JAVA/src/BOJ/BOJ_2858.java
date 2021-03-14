package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2858 {
    private static int R, B;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        for (int i = 3; i < 2000; i++) {
            for (int j = 3; j < i + 1; j++) {
                int tmp = (i * 2) + ((j - 2) * 2);
                if ((tmp == R) && ((i * j) - tmp) == B) {
                    System.out.println(i + " " + j);
                }
            }
        }
        br.close();
    }


    /*
    10 2 >> 4 3
    12 3 >> 5 3
    14 4 >> 6 3
    16 9 >> 5 5
     */
}
