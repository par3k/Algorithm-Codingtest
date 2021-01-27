package BOJ;

import java.io.*;

public class BOJ_3052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[50];

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(br.readLine());
            int tmp = n % 42;
            arr[tmp]++;
        }

        int cnt = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] >= 1) {
                cnt ++;
            }
        }

        System.out.println(cnt);
    }
}
