package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solve_33709 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList addrList = new ArrayList();

        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();

        int result = 0;
        int idx = 0;

        for (int i = 0; i < N; i++) {
            if (str.charAt(i) == '.' || str.charAt(i) == '#' || str.charAt(i) == ':' || str.charAt(i) == '|') {
                result += Integer.parseInt(str.substring(idx ,i));
                idx = i + 1;
            }
        }
        result += Integer.parseInt(str.substring(idx ,N));

        System.out.println(result);
    }
}
