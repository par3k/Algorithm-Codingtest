package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_19622 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Pair[] arr = new Pair[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int capacity = Integer.parseInt(st.nextToken());
            arr[i] = new Pair(start, end, capacity);
        }


        int[] dp = new int[N];
        int ans = -123456789;
        dp[0] = arr[0].capacity;

        if (N >= 1) {
            ans = dp[0];
        }

        if (N >= 2) {
            dp[1] = arr[1].capacity;
        }

        for (int i = 2; i < N; i++) {
            dp[i] = arr[i].capacity + ans;
            ans = Math.max(ans, dp[i - 1]);
        }
        ans = Math.max(ans, dp[N - 1]);
        System.out.println(ans);
        br.close();
    }
}

class Pair {
    int start;
    int end;
    int capacity;

    public Pair(int start, int end, int capacity) {
        this.start = start;
        this.end = end;
        this.capacity = capacity;
    }
}