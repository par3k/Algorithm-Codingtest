package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2851 {
    private static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[10];

        int sum = 0;
        for (int i = 0  ;i < 10; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < 10; i++) {
            sum += arr[i];

            if (sum >= 100) break;
        }

        System.out.println(sum);
        br.close();
    }
}
