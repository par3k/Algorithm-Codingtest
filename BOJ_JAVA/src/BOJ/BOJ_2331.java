package BOJ;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_2331 {
    private static int A, P;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());

        List<Integer> list = new ArrayList<>();
        list.add(A);

        while (true) {
            int tmp = list.get(list.size() - 1);
            int result = 0;

            while (tmp != 0) {
                result += (int) Math.pow(tmp % 10, (double) P);
                tmp /= 10;
            }

            if (list.contains(result)) {
                int ans = list.indexOf(result);
                bw.write(ans + "\n");
                break;
            }
            list.add(result);
        }
        bw.flush();
        bw.close();
        br.close();
    }

}
