package SWEA;

import java.io.*;
import java.util.StringTokenizer;

public class SWEA_1859 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] dayPrice = new int[N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                dayPrice[N - i- 1] = Integer.parseInt(st.nextToken());
            }

            long ans = 0;
            long now_Max = dayPrice[0];

            for (int i = 1; i < N; i ++) {
                if (now_Max > dayPrice[i]) {
                    ans += now_Max - dayPrice[i];
                } else {
                    now_Max = dayPrice[i];
                }
            }
            bw.write("#" + tc + " " + ans + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
