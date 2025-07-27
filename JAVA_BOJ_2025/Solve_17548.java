import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_17548 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int e_cnt = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == 'e') {
                e_cnt++;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append("h");
        for (int i = 0; i < e_cnt * 2; i++) {
            sb.append("e");
        }
        sb.append("y");

        System.out.println(sb.toString());
        br.close();
    }
}
