package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1244 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean swList[] = new boolean[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < N; i++) {
            char stat = st.nextToken().charAt(0);
            if(stat == '1') swList[i] = true;
        }

        int StudentNum = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < StudentNum; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int place = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                for (int j = 0; place * j - 1 < N; j++) {
                    int nPlace = place * j - 1;
                }
            }
        }
    }
}
