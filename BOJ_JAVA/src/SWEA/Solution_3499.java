package SWEA;

import java.io.*;
import java.util.StringTokenizer;

public class Solution_3499 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int tc= 1; tc < T + 1; tc++) {
            int N = Integer.parseInt(br.readLine());
            String[] a;

            if (N % 2 == 1) {
                a = new String[N / 2 + 1];
            } else {
                a = new String[N / 2];
            }

            String[] b = new String[N / 2];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < a.length; i++) {
                a[i] = st.nextToken();
            }

            for (int i = 0; i < b.length; i++) {
                b[i] = st.nextToken();
            }

            bw.write("#" + tc + " ");
            for (int i = 0; i < b.length; i++) {
                bw.write(a[i] + " " + b[i] + " ");
            }
            if (N % 2 == 1) {
                bw.write(a[N / 2]);
            }
            bw.write("\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
