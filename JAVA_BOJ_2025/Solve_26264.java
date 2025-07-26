import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_26264 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String input = br.readLine();

        int bcnt = 0;
        int scnt = 0;

        for (int i = 0; i < input.length(); i++) {
            if (input.substring(i, i + 1).equals("b")) {
                bcnt++;
            } else if (input.substring(i, i + 1).equals("s")) {
                scnt++;
            }
        }

        if (bcnt> scnt) {
            System.out.println("bigdata?");
        } else if (bcnt < scnt) {
            System.out.println("security!");
        } else {
            System.out.println("bigdata? security!");
        }

        br.close();
    }
}
