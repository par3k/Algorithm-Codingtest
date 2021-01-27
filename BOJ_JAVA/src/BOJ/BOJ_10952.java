package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_10952 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (a == 0  && b == 0){
                br.close();
                break;
            } else {
                System.out.println(a + b);
            }
        }
    }
}
