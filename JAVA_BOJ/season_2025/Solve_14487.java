package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_14487 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");

        int sum = 0;
        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(input[i]);
            if (Integer.parseInt(input[i]) > maxVal) {
                maxVal = Integer.parseInt(input[i]);
            }
        }

        int result = sum - maxVal;
        System.out.println(result);

        br.close();
    }
}
