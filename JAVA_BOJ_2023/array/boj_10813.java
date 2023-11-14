package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_10813 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<Integer> list = new ArrayList<>(N);

        for (int i = 1; i <= N; ++i) {
            list.add(i);
        }

        for (int idx = 0; idx < M; ++idx) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;

            int tmp = list.get(i);
            list.set(i, list.get(j));
            list.set(j, tmp);
        }
        for (int i = 0; i < list.size(); ++i) {
            System.out.print(list.get(i) + " ");
        }
    }
}
