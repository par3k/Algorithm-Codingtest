package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10867 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[2001];

        for (int i = 0; i < N; i++) {
            arr[Integer.parseInt(st.nextToken()) + 1000]++;
        }

        for (int i = 0; i <= 2000; i++) {
            if (arr[i] > 0) {
                System.out.println(i - 1000);
            }
        }
    }
}
