import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_11365 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            String input = br.readLine();
            if (input.equals("END")) break;

            int length = input.length();
            for (int i = length - 1; i >= 0; i--) {
                sb.append(input.charAt(i));
            }
            sb.append('\n');
        }
        System.out.println(sb);
        br.close();
    }
}
