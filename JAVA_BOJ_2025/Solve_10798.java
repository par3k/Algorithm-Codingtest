import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solve_10798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] arr = new char[5][15];

        for (int i = 0 ; i < 5; i++) {
            String input = br.readLine();

            for (int j = 0 ; j <input.length() ; j++) {
                arr[i][j] = input.charAt(j);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < 15; j++) {
            for (int i = 0; i < 5; i++) {
                if (arr[i][j] != 0) {
                    sb.append(arr[i][j]);
                }
            }
        }
        System.out.println(sb.toString());
        br.close();
    }
}
