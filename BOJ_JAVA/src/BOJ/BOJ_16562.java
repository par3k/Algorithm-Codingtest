package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_16562 {
    private static int[] tmp, money;

    private static int Find(int x) {
        if (x == tmp[x]) return x;
        return tmp[x] = Find(tmp[x]);
    }

    private static void Union(int x, int y) {
        x = Find(x);
        y = Find(y);

        if (money[x] < money[y]) {
            tmp[y] = tmp[x];
        } else {
            tmp[x] = tmp[y];
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int K = Integer.parseInt(line[2]);

        tmp = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            tmp[i] = i;
        }

        money = new int[N + 1];
        money[0] = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1 ; i <= N; i++) {
            money[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            Union(v, w);
        }

        int ans = 0;
        for (int i = 0; i < N + 1; i++) {
            if (i == tmp[i]) {
                ans += money[i];
            }
        }

        if (K - ans < 0) {
            System.out.println("Oh no");
        } else {
            System.out.println(ans);
        }

        br.close();
    }
}
