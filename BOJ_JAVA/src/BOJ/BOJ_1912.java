package BOJ;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_1912 {
    private static int max (int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Integer> dp = new ArrayList<>();
        dp.add(arr[0]);

        for (int i = 0; i < N - 1; i++) {
            dp.add(max((dp.get(i) + arr[i + 1]), arr[i + 1]));
        }

        int ans = -123456789;
        for (int i = 0 ; i < N; i++) {
            ans = max(ans, dp.get(i));
        }

        bw.write(ans +"\n");
        br.close();
        bw.flush();
        bw.close();
    }
}
