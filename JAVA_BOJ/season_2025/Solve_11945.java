package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_11945 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            String bung = br.readLine();

            for (int j = M; j >= 1; j--) {
                sb.append(bung.charAt(j - 1));
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }
}
