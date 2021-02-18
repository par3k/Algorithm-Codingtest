package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1592 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];
        int ans = 0;
        int idx = 1;
        arr[1] = 1;

        while (true) {
            idx = (arr[idx] % 2 == 1) ? (idx + l) : (idx - l);

            if (idx > n) {
                idx %= n;
            } else if (idx < 1){
                idx += n;
            }

            arr[idx]++;
            ans++;

            if (arr[idx] == m) break;
        }
        System.out.println(ans);
        br.close();

    }
}
