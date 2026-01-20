package season_2026;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Solve_30402 {
    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean flag = false;
        for (int i = 0; i < 15 && !flag; i++) {
           List<String> rowList = List.of(br.readLine().split(" "));

            for (String s : rowList) {
                if (flag) break;
                if (s.equals("w")) {
                    System.out.println("chunbae");
                    flag = true;
                    break;
                } else if (s.equals("b")) {
                    System.out.println("nabi");
                    flag = true;
                    break;
                } else if (s.equals("g")) {
                    System.out.println("yeongcheol");
                    flag = true;
                    break;
                }
            }
       }
        br.close();
    }
}
