package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_5026 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            String[] strArr = {};

            if (input.contains("+")) {
                strArr = input.split("\\+");
                sb.append(Integer.parseInt(strArr[0]) + Integer.parseInt(strArr[1]));
            } else if (input.equals("P=NP")) {
                sb.append("skipped");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }
}
