package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1940 {
    private static int status;
    private static int accel;
    private static int distance;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            distance = 0;
            accel = 0;

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                status = Integer.parseInt(st.nextToken());

                switch (status) {
                    case 1:
                        int a = Integer.parseInt(st.nextToken());
                        accel += a;
                        distance += accel;
                        break;
                    case 2:
                        int b = Integer.parseInt(st.nextToken());
                        accel -= b;
                        if (accel < 0) accel =0;
                        distance += accel;
                        break;
                    case 0:
                        distance += accel;
                        break;
                }
            }
            System.out.println("#" + tc + " " + distance);
        }

    }
}
