package BOJ;

import java.io.*;

public class BOJ_2747 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N + 1];
        arr[0] = 0;
        arr[1] = 1;

        for (int i = 2; i < N + 1; i++){
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        System.out.println(arr[N]);
    }
}
