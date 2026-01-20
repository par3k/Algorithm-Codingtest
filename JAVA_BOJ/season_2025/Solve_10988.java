package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_10988 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        /**
         * l e v e l (length : 5) = 5/2 + 1
         * b e a k j o o n (length : 8)
         */
        boolean flag = false;
        int length = input.length();
        for (int i = 0 ; i < length / 2 ; i++) {
            if (input.charAt(i) != input.charAt(length - 1 - i)) {
                flag = true;
                break;
            }
        }

        if (flag) {
            System.out.println(0);
        } else {
            System.out.println(1);
        }

        br.close();
    }
}
