package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2559 {
    private static int[] arr, tmp;
    private static int N;

    private static void func(int depth, int k, int start, int idx) {
        if (k == N + 1) return;
        int ans = 0;
        for (int i = start; i <= k; i++) {
            ans += arr[i];
            tmp[idx] = ans;
        }
        func(depth + 1, k + 1, start + 1, idx + 1);

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        arr = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        tmp = new int[N - K + 1];
        func(0, K, 1, 0);

        Arrays.sort(tmp);
        System.out.println(tmp[tmp.length - 1]);


    }
}