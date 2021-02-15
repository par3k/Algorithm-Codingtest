package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10820 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        int[] cnt;

        while ((input = br.readLine()) != null) {
            cnt = new int[4];

            for (int i = 0; i < input.length(); i++) {
                int code = input.charAt(i);

                if (code >= 97 && code <= 122) {
                    cnt[0] += 1;
                }
                if (code >= 65 && code <= 90) {
                    cnt[1] += 1;
                }
                if (code >= 48 && code <= 57) {
                    cnt[2] += 1;
                }

                if (code == 32) {
                    cnt[3] += 1;
                }
            }
            for (int i : cnt) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}
