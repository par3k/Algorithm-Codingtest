import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_11328 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cases = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < cases ; i++) {
            String[] inputArr = br.readLine().split(" ");

            boolean result = solve(inputArr);

            if (result) {
                System.out.println("Impossible");
            } else {
                System.out.println("Possible");
            }
        }
    }

    private static boolean solve(String[] arr) {
        boolean result = false;
        int[] alphabet = new int[26];
        char[] word1 = arr[0].toCharArray();
        char[] word2 = arr[1].toCharArray();

        for (char chr : word1) {alphabet[chr - 'a']++;}
        for (char chr : word2) {alphabet[chr - 'a']--;}

        for (int i = 0; i < 26; i++) {
            if (alphabet[i] != 0) {
                result = true;
            }
        }
        return result;
    }
}
