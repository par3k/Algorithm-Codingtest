package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class SWEA_1660 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            ArrayList<Integer> arr = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int tmp = Integer.parseInt(st.nextToken());
                arr.add(tmp);
            }

            Collections.sort(arr);
            boolean flag = false;
            for(int i = 0; i < N; i++) {
                int tmp = arr.get(i);
                int sum = K * (tmp / M);
                if(sum < (i + 1))
                    flag = true;
            }

            if (flag) {
                System.out.println("#" + tc + " " + "Impossible");
            } else {
                System.out.println("#" + tc + " " + "Possible");
            }
        }
        br.close();
    }
}
