package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 페르마의 소정리
// a ^(p - 1) = 1 (mod p)
// a ^(p - 2) = a ^-1 (mod p)
// (r! (n - r)!) ^ (1234567891 - 2) = (r! (n - r)!) ^ -1

// nCr = n! / r! (n - r)! = n! * (r! (n - r)!) ^-1

public class Solution_5607 {
    private static final int MOD = 1234567891;

    private static long fermat(long n, int x) {
        if (x == 0) return 1;
        long tmp = fermat(n, x/2);
        long result = (tmp * tmp) % MOD;
        if (x % 2 ==0){
            return result;
        } else {
            return (result * n) % MOD;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
            String[] line = br.readLine().split(" ");
            int n = Integer.parseInt(line[0]);
            int r = Integer.parseInt(line[1]);

            long fac[] = new long[n + 1];
            fac[0] = 1;

            for (int i = 1; i <= n; i++) {
                fac[i] = (fac[i - 1] * i) % MOD;
            }

            long bottom = (fac[r] * (fac[n - r])) % MOD;
            long reBottom = fermat(bottom, MOD - 2);


            sb.append("#").append(tc).append(" ").append((fac[n] * reBottom) % MOD).append("\n");
        }
        System.out.println(sb);
        br.close();
    }
}
