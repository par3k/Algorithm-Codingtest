import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_11721 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < input.length() + 1; i++) {
            sb.append(input.charAt(i - 1));
            if (i % 10 == 0) {
                sb.append("\n");
            }
        }
        System.out.println(sb.toString());
        br.close();
    }
}
