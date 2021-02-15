package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_20299 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        int totalCnt = 0;

        for (int i = 0 ; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a >= M && b >= M && c >= M) {
                if (a + b + c >= S) {
                    totalCnt++;
                    sb.append(a).append(" ").append(b).append(" ").append(c).append(" ");

                }
            }
        }

        bw.write(totalCnt + "\n");
        bw.write(sb.toString());

        br.close(); // 스캐너 닫음
        bw.flush();
        bw.close();
    }
}
