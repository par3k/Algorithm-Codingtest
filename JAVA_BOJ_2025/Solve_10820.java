import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_10820 {
    public static void main(String[] args) throws IOException {
        String capital = "ABCDEFGHIJKLNMOPQRSTUVWXYZ";
        String small = "abcdefghijklmnopqrstuvwxyz";
        String number = "0123456789";

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        while ((input = br.readLine()) != null) {
            int[] result = new int[4];

            for (int i = 0; i < input.length(); i++) {
                if (small.contains(input.substring(i, i + 1))) {
                    result[0]++;
                } else if (capital.contains(input.substring(i, i + 1))) {
                    result[1]++;
                } else if (number.contains(input.substring(i, i + 1))) {
                    result[2]++;
                } else {
                    result[3]++;
                }
            }

            for (int i : result) {
                System.out.print(i + " ");
            }
            System.out.println();
        }

    }
}
