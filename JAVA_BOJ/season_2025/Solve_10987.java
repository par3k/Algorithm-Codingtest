package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_10987 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        String[] list = {"a", "e", "i", "o", "u"};
        int answer = 0;
        for (int i = 0; i < input.length(); i++) {
            for (int j = 0; j < list.length; j++) {
                if (input.charAt(i) == list[j].charAt(0)) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
