package BOJ;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_10951 {
    public static void main(String args[]) throws Exception {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            String line = br.readLine();
            // if(line == null) {//이클립스에서 작동하지 않음
            if (line == null || line.equals("")) {
                break;
            }
            st = new StringTokenizer(line);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(a + b + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}