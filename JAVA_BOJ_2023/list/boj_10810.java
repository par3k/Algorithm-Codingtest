package list;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class boj_10810 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            hashMap.put(i + 1, 0);
        }

        for (int tc = 0; tc < m; ++tc) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            int idx = i;
            while (idx <= j) {
                hashMap.put(idx, k);
                idx++;
            }
        }

        for (int i = 1; i <= n; ++i) {
            sb.append(hashMap.get(i)).append(" ");
        }
        System.out.println(sb.toString());
    }
}
