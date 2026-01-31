package season_2026;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_19532 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int a = Integer.parseInt(inputs[0]);
        int b = Integer.parseInt(inputs[1]);
        int c = Integer.parseInt(inputs[2]);
        int d = Integer.parseInt(inputs[3]);
        int e = Integer.parseInt(inputs[4]);
        int f = Integer.parseInt(inputs[5]);

        for (int x = -999; x <= 999; x++) {
            for (int y = -999; y <= 999; y++) {
                if ((a * x) + (b * y) == c
                && (d * x) + (e * y) == f) {
                    System.out.println(x + " " + y);
                }
            }
        }

        br.close();
    }
}
