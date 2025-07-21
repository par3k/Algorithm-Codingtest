import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_32929 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if (n % 3 == 0) {
            System.out.println('S');
        } else if (n % 3 == 1) {
            System.out.println('U');
        } else if (n % 3 == 2) {
            System.out.println('O');
        }
        br.close();
    }
}
