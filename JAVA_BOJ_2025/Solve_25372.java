import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_25372 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (; n > 0; n--) {
            String s = br.readLine();
            if (s.length() >= 6 && s.length() <= 9) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
        br.close();

    }
}
