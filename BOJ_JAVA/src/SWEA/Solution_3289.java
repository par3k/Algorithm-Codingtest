package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3289 {
    private static int n, m;
    private static int[] parent, rank;

    private static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    private static void union(int a, int b) {
        int fa = find(a);
        int fb = find(b);

        if (rank[fa] < rank[fb]) {
            parent[fa] = fb;
        } else {
            parent[fb] = fa;
            if (rank[fa] == rank[fb]) {
                rank[fa]++;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++){
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            parent = new int[n + 1];
            rank = new int[n + 1];
            for (int i = 1; i < n + 1; i++) {
                parent[i] = i;
                rank[i] = 0;
            }

            for (int i = 0 ; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int cmd = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (cmd == 0) { // 유니온
                    union(a, b);
                } else if (cmd == 1) { // 파인드
                    int f_a = find(a);
                    int f_b = find(b);
                    sb.append((f_a == f_b) ? 1 : 0);
                }
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }
}
