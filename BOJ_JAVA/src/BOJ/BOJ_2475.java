package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[5];
        for (int i =0 ; i < 5; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int ans = 0;
        for (int i : arr) {
            ans += Math.pow(i, 2);
        }

        ans = ans % 10;
        System.out.println(ans);
    }
}
