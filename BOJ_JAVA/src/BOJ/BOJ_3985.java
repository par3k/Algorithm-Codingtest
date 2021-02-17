package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_3985 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        boolean[] chk = new boolean[L + 1];
        int[] perhaps = new int[N];
        int[] actually = new int[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int From = Integer.parseInt(st.nextToken());
            int To = Integer.parseInt(st.nextToken());
            perhaps[i] = To - From + 1;

            for (int j = From; j <= To; j++) {
                if (!chk[j]) {
                    chk[j] = true;
                    actually[i]++;
                }
            }

        }

        int perIdx = 0;
        int actIdx = 0;
        int perMax = 0;
        int actMax = 0;

        for (int i = 0; i < N; i++) {
            if (perhaps[i] > perMax) {
                perMax = perhaps[i];
                perIdx = i + 1;
            }
        }

        for (int i = 0; i < N; i++) {
            if (actually[i] > actMax) {
                actMax = actually[i];
                actIdx = i + 1;
            }
        }

        System.out.println(perIdx);
        System.out.println(actIdx);
        br.close();
    }
}
