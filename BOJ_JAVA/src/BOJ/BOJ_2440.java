package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2440 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for (int k = N; k > i; k--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}