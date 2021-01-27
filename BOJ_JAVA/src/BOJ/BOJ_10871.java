package BOJ;

import java.io.*;

public class BOJ_10871 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");

        int n = Integer.parseInt(str[0]);
        int x = Integer.parseInt(str[1]);

        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++){
            int a = Integer.parseInt(input[i]);
            if (a < x){
                System.out.print(a + " ");
            }
        }
        br.close();
    }
}
