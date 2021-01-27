package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_5622 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();
        char arr[] = s.toCharArray();

        int ans = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 'A' || arr[i] == 'B'|| arr[i] =='C'){
                ans += 2;
            } else if (arr[i] == 'D' || arr[i] == 'E'|| arr[i] =='F') {
                ans += 3;
            } else if (arr[i] == 'G' || arr[i] == 'H'|| arr[i] =='I') {
                ans += 4;
            } else if (arr[i] == 'J' || arr[i] == 'K'|| arr[i] =='L') {
                ans += 5;
            } else if (arr[i] == 'M' || arr[i] == 'N'|| arr[i] =='O') {
                ans += 6;
            } else if (arr[i] == 'P' || arr[i] == 'Q'|| arr[i] =='R' || arr[i] == 'S') {
                ans += 7;
            } else if (arr[i] == 'T' || arr[i] == 'U'|| arr[i] =='V') {
                ans += 8;
            } else if (arr[i] == 'W' || arr[i] == 'X'|| arr[i] =='Y' || arr[i] == 'Z') {
                ans += 9;
            }
        }
        System.out.println(ans + arr.length);
    }
}
