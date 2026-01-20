package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_30999 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int result = 0;
        for (int i = 0; i < n; i ++) {
            String vote = br.readLine();

            int agreeCnt = 0;
            for (int j = 0; j < m; j ++) {
                if (vote.charAt(j) == 'O') {
                    agreeCnt++;
                }
            }
            if (agreeCnt > m/2) {
                result++;
            }
        }
        System.out.println(result);
        br.close();
    }
}
