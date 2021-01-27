package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ_2870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<BigInteger> arr = new ArrayList<>();
        String[] line;

        for (int i = 0; i < N; i++) {
            line = br.readLine().split("\\D");
            for (int j = 0; j < line.length; j++) {
                if (!line[j].equals("")) arr.add(new BigInteger(line[j]));
            }
        }

        arr.sort(null);
        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }
        br.close();
    }
}
