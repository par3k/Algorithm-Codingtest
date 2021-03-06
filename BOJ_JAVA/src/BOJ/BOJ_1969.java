package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1969 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] arr = new String[n];
        int[][] alphabet = new int[m][26];

        for (int i = 0; i< n; i++) {
            arr[i] = br.readLine();
            for (int j = 0 ; j < m; j++) {
                alphabet[j][arr[i].charAt(j) - 'A']++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < m; i++) {
            int max = -123456789;
            int idx = 0;

            for (int j = 0; j < 26; j++) {
                if (alphabet[i][j] > max){
                    max = alphabet[i][j];
                    idx = j;
                }
            }
            sb.append((char) (idx + 'A'));
        }
        System.out.println(sb.toString());

        int ans = 0;
        for (int i = 0;  i< n; i++) {
            for (int j = 0 ; j < m; j++) {
                if (sb.charAt(j) != arr[i].charAt(j)) ans++;
            }
        }
        System.out.println(ans);
        br.close();
    }
}
