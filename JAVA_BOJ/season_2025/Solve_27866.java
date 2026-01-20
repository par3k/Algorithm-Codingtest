package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solve_27866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> inputList = new ArrayList<>();

        for (int i = 0; i < 2; ++i) {
           String inputline = br.readLine();
           inputList.add(inputline);
        }

        String str = inputList.get(0);
        int idx = Integer.parseInt(inputList.get(1));

        for (int i = 0; i < str.length(); i++) {
            if (i == idx - 1) {
                System.out.println(str.charAt(i));
            }
        }
    }
}
