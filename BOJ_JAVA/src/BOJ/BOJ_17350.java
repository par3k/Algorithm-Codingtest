package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_17350 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String [] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }
        int ans = 0;
        for (int i = 0 ; i < N; i++) {
            if (arr[i].equals("anj")) {
                ans++;
            }
        }
        if (ans > 0) {
            System.out.println("뭐야;");
        } else {
            System.out.println("뭐야?");
        }
    }
}
