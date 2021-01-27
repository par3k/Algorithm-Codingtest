package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        double sum = 0;
        int max = Integer.MIN_VALUE;
        double ans;

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        for (int i = 0; i < arr.length; i++) {
            sum += (double) arr[i] / max * 100;
        }

        ans = sum / (double) N;
        System.out.println(ans);
        br.close();
    }
}
