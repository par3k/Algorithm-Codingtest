package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2527 {
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int x1, y1, x2, y2, tx1, ty1, tx2, ty2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());

            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());

            tx1 = Integer.parseInt(st.nextToken());
            ty1 = Integer.parseInt(st.nextToken());
            tx2 = Integer.parseInt(st.nextToken());
            ty2 = Integer.parseInt(st.nextToken());

            sb.append(check(x1, y1, x2, y2, tx1, ty1, tx2, ty2) + "\n");
        }

        System.out.print(sb);
        br.close();
    }


    private static String check(int x1, int y1, int x2, int y2, int tx1, int ty1, int tx2, int ty2) {
        if ((x2 == tx1 && y2 == ty1) || (x1 == tx2 && y2 == ty1) || (x2 == tx1 && y1 == ty2) || (x1 == tx2 && y1 == ty2)) {
            return "c";
        } else if ((x2 == tx1 && y2 != ty1) || (x1 == tx2 && y2 != ty1) || (x2 != tx1 && y1 == ty2) || (x1 != tx2 && y1 == ty2)) {
            return "b";
        } else if (x2 < tx1 || tx2 < x1 || y2 < ty1 || ty2 < y1) {
            return "d";
        } else {
            return "a";
        }
    }
}