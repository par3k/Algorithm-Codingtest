package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_26068 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int result = 0;

        for (int i = 0; i < n; i++) {
            String[] expireDateArr = br.readLine().split("-");
            int dDay = Integer.parseInt(expireDateArr[1]);
            if (dDay <= 90) {
                result ++;
            }
        }

        System.out.println(result);
        br.close();
    }
}
