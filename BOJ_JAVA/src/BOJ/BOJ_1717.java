package BOJ;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1717 {
    private static int[] parent;

    private static int Find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = Find(parent[x]);
    }

    private static void Union(int a, int b) {
        a = Find(a);
        b = Find(b);
        if (a == b) return;
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);

        parent = new int[n + 1];
        for (int i = 0 ; i  < n + 1; i++) {
            parent[i] = i;
        }

        for (int i = 0 ; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 0) {
                Union(b, c);
            } else {
                if (Find(b) == Find(c)) {
                    bw.write("YES" + "\n");
                } else {
                    bw.write("NO" + "\n");
                }
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
