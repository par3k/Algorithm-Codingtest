package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2477 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[6];
        for (int i = 0 ; i < 6; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int w = 0;
        int h = 0;

        for (int i = 0; i < 6; i++) {
            if (i % 2 == 0) {
                if (w < arr[i]) {
                    w = arr[i];
                }
            } else {
                if (h < arr[i]) {
                    h = arr[i];
                }
            }
        }

        int w2 = 0;
        int h2 = 0;

        for (int i = 0; i < 6; i++) {
            if (i % 2 == 0) {
                if (h == arr[(i + 5) % 6] + arr[(i + 1) % 6]) {
                    w2 = arr[i];
                }
            } else {
                if (w == arr[(i + 5) % 6] + arr[(i + 1) % 6]) {
                    h2 = arr[i];
                }
            }
        }

        System.out.println(((w * h) - (w2 * h2)) * N);
        br.close();
    }
}
