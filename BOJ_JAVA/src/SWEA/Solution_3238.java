package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 페르마의 소정리
// a ^(p - 1) = 1 (mod p)
// a ^(p - 2) = a ^-1 (mod p)
// (r! (n - r)!) ^ (1234567891 - 2) = (r! (n - r)!) ^ -1

// nCr = n! / r! (n - r)! = n! * (r! (n - r)!) ^-1

public class Solution_3238 {
    private static long n, r;
    private static int MOD;

    private static long fermat(long n, long r) {
        long result = 1;
        while (r > 0){
            if ((r % 1) == 1) {
                result *= n;
                result %= MOD;
            }
            n *= n;
            n %= MOD;
            r /= 2;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
            String[] line = br.readLine().split(" ");
            n = Long.parseLong(line[0]);
            r = Long.parseLong(line[1]);
            MOD = Integer.parseInt(line[2]);

            long fac[] = new long[100000];
            fac[0] = 1;

            for (int i = 1; i <= MOD; i++) {
                fac[i] = (fac[i - 1] * i) % MOD;
            }
            long result = 1;
            while (n > 0 || r > 0) {
                long a = n % MOD;
                long b = r % MOD;

                if (a < b) result = 0;
                if (result == 0) break;

                result *= fac[(int) a];
                result %= MOD;
                result *= fermat((fac[(int) b] * fac[(int) a - (int) b]) % MOD, MOD - 2);
                result %= MOD;

                n /= MOD;
                r /= MOD;
            }


            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.println(sb);
        br.close();
    }
}
