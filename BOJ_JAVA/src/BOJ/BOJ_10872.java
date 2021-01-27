package BOJ;

import java.io.*;

public class BOJ_10872 {

    public static int pactorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return pactorial(n - 1) * n;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(pactorial(N));

    }
}
