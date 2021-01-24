import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class BOJ_10820 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;
        int[] ans;

        while ((input = br.readLine()) != null) {
            ans = new int[4];

            for (int i = 0; i < input.length(); i++) {
                int code = input.charAt(i);

                if (code >= 97 && code <= 122) {
                    ans[0] += 1;
                }

                if (code >= 65 && code <= 90) {
                    ans[1] += 1;
                }

                if (code >= 48 && code <= 57) {
                    ans[2] += 1;
                }

                if (code == 32) {
                    ans[3] += 1;
                }
            }
            for (int i : ans) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}
