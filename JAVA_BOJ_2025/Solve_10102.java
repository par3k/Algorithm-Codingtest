import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_10102 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] voteBox = new int[2];

        int v = Integer.parseInt(br.readLine());
        String input = br.readLine();

        for (int j = 0; j < v; j++) {
            if (input.charAt(j) == 'A') {
                voteBox[0]++;
            } else if (input.charAt(j) == 'B') {
                voteBox[1]++;
            }
        }

        if (voteBox[0] == voteBox[1]) {
            System.out.println("Tie");
        } else if (voteBox[0] > voteBox[1]) {
            System.out.println("A");
        } else {
            System.out.println("B");
        }
    }
}
