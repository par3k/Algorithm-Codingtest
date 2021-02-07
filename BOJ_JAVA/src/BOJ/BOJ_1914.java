package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class BOJ_1914 {
    private static void hanoi_tower (int cnt, int from, int aux, int to){
        if (cnt == 1) {
            System.out.println(from + " " + to);
            return;
        }
        hanoi_tower(cnt - 1, from, to, aux);
        System.out.println(from + " " + to);
        hanoi_tower(cnt - 1, aux, from, to);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        BigInteger ans = new BigInteger("1");
        if (N == 1) System.out.println(1);
        else {
            for (int i = 0 ; i <  N; i++) {
                ans = ans.multiply(new BigInteger("2"));
            }
            ans = ans.subtract(new BigInteger("1"));
            System.out.println(ans);
        }
        if (N <= 20) {
            hanoi_tower(N, 1, 2, 3);
        }
    }
}
