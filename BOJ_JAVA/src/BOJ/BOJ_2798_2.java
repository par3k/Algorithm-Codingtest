package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2798_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i =0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int ans = 0;
        int tmp;
        for (int i = 0 ; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                for (int k = i + 2; k < N; k++) {
                    if (!(i == j) && !(j == k) && !(i == k)) {
                        tmp = arr[i] + arr[j] + arr[k];
                        if (tmp <= M && ans < tmp) {
                            ans = tmp;
                        }
                    }

                }
            }
        }
        System.out.println(ans);
        br.close();
    }
}
