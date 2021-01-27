package BOJ;

import java.io.*;

public class BOJ_11653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int i = 2;
        while ( n != 1) {
            if (n % i == 0) {
                n /= i;
                System.out.println(i);
            } else {
                i ++;
            }
        }
        br.close();
    }
}
