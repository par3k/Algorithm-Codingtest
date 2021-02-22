package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_13300 {
    private static int[][] students;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] students = new int[6][2];

        for (int t = 1; t <= N; t++) {
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());
            students[Y - 1][S]++;
        }

        // 로직
        int ans = 0;

        for (int i = 0 ; i < 6; i++) {
            for (int j = 0; j < 2; j++) {
                ans += (students[i][j] / K + (students[i][j] % K == 0? 0 : 1));
            }
        }

        // 출력
        System.out.println(ans);
    }
}
