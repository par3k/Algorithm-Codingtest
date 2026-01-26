package season_2026;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_9996 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (char c : br.readLine().toCharArray()) {
            if (c == '*') {
                sb.append(' ');
            } else {
                sb.append(c);
            }
        }

        String[] patternArr = sb.toString().split(" ");
        String pattern1 = patternArr[0];
        String pattern2 = patternArr[1];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            boolean checkFlag = true;
            boolean checkFlag2 = true;

            if (input.length() < pattern1.length() + pattern2.length()) {
                System.out.println("NE");
                continue;
            }

            if (!input.startsWith(pattern1)) {
                checkFlag = false;
            }

            if (!input.endsWith(pattern2)) {
                checkFlag2 = false;
            }

            if (checkFlag && checkFlag2) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
        }

        br.close();
    }
}
