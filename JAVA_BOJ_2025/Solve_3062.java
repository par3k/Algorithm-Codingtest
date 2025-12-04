import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_3062 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String input = br.readLine();

            String tmp = "";
            for (int j = input.length() - 1; j >= 0; j--) {
                tmp += input.charAt(j);
            }

            String sumValStr = String.valueOf(Integer.parseInt(input) + Integer.parseInt(tmp));

            // 대칭인지 확인
            boolean result = false;
            int range = sumValStr.length() / 2;
            for (int k = 0; k < range; k++) {
                if (sumValStr.charAt(k) == sumValStr.charAt(sumValStr.length() - k - 1)) {
                    result = true;
                } else {
                    result = false;
                    break;
                }
            }

            if (result) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }
        br.close();
    }
}
