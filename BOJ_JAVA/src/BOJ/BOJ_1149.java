package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1149 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N + 1][3];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Math.min(arr[i - 1][1], arr[i - 1][2]) + Integer.parseInt(st.nextToken());
            arr[i][1] = Math.min(arr[i - 1][0], arr[i - 1][2]) + Integer.parseInt(st.nextToken());
            arr[i][2] = Math.min(arr[i - 1][0], arr[i - 1][1]) + Integer.parseInt(st.nextToken());
        }

        int ans = 1234567890;
        for (int i = 0 ; i < 3; i++) {
            ans = Math.min(ans, arr[N][i]);
        }
        System.out.print(ans);
        br.close();
    }
}
