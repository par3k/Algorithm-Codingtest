package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_6378 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String input = br.readLine();

            if (input.equals("0")) {
                break;
            }

            while (input.length() > 1) {
                int sum = 0;

                for (char c : input.toCharArray()) {
                    sum += c - '0';
                }
                input = String.valueOf(sum);
            }
            System.out.println(input);
        }
        br.close();
    }
}
