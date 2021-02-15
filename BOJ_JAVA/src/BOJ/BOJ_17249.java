package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_17249 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int [] arr  = new int[2];
        int tmp_left = 0;
        int tmp_right = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                tmp_left = i;
            }
            if (s.charAt(i) == ')') {
                tmp_right = i;
            }
        }

        for (int i = 0 ; i < tmp_left; i++) {
            if (s.charAt(i) == '@') {
                arr[0]++;
            }
        }

        for (int i = s.length() - 1; i > tmp_right; i--) {
            if (s.charAt(i) == '@') {
                arr[1]++;
            }
        }
        System.out.println(arr[0] + " " + arr[1]);
    }
}
