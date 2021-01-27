package BOJ;

import java.io.*;

public class BOJ_10870 {
    public static int recursive(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return recursive(n - 1) + recursive(n - 2);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(recursive(n));
    }
}