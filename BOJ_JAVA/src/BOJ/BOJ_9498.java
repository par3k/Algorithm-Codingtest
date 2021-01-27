package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_9498 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        if (100 >= n && n >= 90) {
            System.out.print('A');
        } else if (90 > n && n >= 80) {
            System.out.print('B');
        } else if (80 > n && n >= 70) {
            System.out.print('C');
        } else if (70 > n && n >= 60) {
            System.out.print('D');
        } else {
            System.out.print('F');
        }
    }
}
