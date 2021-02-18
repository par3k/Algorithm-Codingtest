package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1247 {
    private static int T, N, ans;
    private static boolean[] visited;
    private static Point home, company, customer[];

    private static void Permutation(int depth, Point p, int dist) {
        if (depth == N) {
            dist += Math.abs(p.x - home.x) + Math.abs(p.y - home.y);
            ans = Math.min(ans, dist);
        }
        if (dist >= ans) return;

        for (int i = 0; i < N; i++) {
            if(!visited[i]) {
                visited[i] = true;
                Permutation(depth + 1, customer[i], dist + Math.abs(p.x - customer[i].x) + Math.abs(p.y - customer[i].y));
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            home = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            company = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            customer = new Point[N];
            for (int i = 0; i < N; i++) {
                customer[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }

            visited = new boolean[N];
            ans = 123456789;

            Permutation(0, company, 0);

            System.out.println("#" + tc + " " + ans);

        }
        br.close();
    }

    static class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}

