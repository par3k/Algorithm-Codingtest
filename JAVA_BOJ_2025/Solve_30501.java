import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_30501 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());

        for (; n > 0; n--) {
            String name = input.readLine();
            if (name.contains("S")) {
                System.out.println(name);
                break;
            }
        }
        input.close();
    }
}
