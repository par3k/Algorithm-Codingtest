package BOJ;

import java.io.*;

public class BOJ_2577 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());

        int sum = a * b * c;
        int[] cnt = new int[10];

        while (sum > 0) {
            cnt[sum % 10]++;
            sum /= 10;
        }

        for (int i = 0; i < cnt.length; i++) {
            System.out.println(cnt[i]);
        }
        br.close();
    }
}