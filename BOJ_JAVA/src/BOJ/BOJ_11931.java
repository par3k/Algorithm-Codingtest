package BOJ;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;

public class BOJ_11931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Integer[] num = new Integer[Integer.parseInt(br.readLine())];
        for (int i = 0; i < num.length; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(num, Collections.reverseOrder());
        for (int i = 0; i < num.length; i++) {
            bw.write(num[i] + "\n");
        }
        br.close();
        bw.flush();
    }
}
