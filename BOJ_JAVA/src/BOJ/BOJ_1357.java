package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1357 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int [] arr = new int[2];

        String vote = br.readLine();
        for (int i = 0; i < vote.length(); i++) {
            arr[(vote.charAt(i) - 'A')]++;
        }

        if (arr[0] < arr[1]) {
            System.out.println('B');
        } else if (arr[0] > arr[1]) {
            System.out.println('A');
        } else {
            System.out.println("Tie");
        }

    }
}
