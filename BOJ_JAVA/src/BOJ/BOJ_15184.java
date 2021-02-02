package BOJ;

import java.io.*;
import java.util.Locale;

public class BOJ_15184 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().toUpperCase(Locale.ROOT);

        int[] cnt = new int[26];

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') cnt[s.charAt(i) - 'A']++;
        }

        for (int i = 0; i < 26; i++) {
            System.out.print((char) (i + 65) + " | ");
            while (cnt[i] != 0) {
                System.out.print('*');
                cnt[i]--;
            }
            System.out.println();
        }
    }
}