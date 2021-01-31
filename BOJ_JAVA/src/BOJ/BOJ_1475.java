package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1475 {
    public static int[] num = new int[10];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        for (int i = 0; i < s.length(); i++) {
            num[(s.charAt(i)) - '0']++;
        }
        num[6] = (num[6] + num[9] + 1) / 2;
        num[9] = 0;

        int max = 0;
        for (int i = 0 ; i < 10; i++) {
            max = Math.max(num[i], max);
        }
        System.out.println(max);
    }
}
