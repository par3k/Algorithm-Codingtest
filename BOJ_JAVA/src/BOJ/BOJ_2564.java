package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_2564 {
    static class Pair {
        int dir, x, y;

        public Pair(int dir, int c, int r, int dis) {
            this.dir = dir;

            if (dir == 1) { // 북
                this.x = dis;
                this.y = 0;
            } else if (dir == 2) { // 남
                this.x = dis;
                this.y = c;
            } else if (dir == 3) { // 서
                this.x = 0;
                this.y = dis;
            } else { // 동
                this.x = r;
                this.y = dis;
            }
        }
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());

        ArrayList<Pair> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int dir = Integer.parseInt(st.nextToken());
            int dis = Integer.parseInt(st.nextToken());
            Pair p = new Pair(dir, c, r, dis);
            arr.add(p);
        }

        st = new StringTokenizer(br.readLine());
        int d = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        Pair dong = new Pair(d, c, r, v);
        int tmp = 0;
        int ans = 0;

        if (d == 1) {
            tmp = 2;
        } else if (d == 2) {
            tmp = 1;
        } else if (d == 3) {
            tmp = 4;
        } else {
            tmp = 3;
        }

        for(Pair p : arr) {
            if (p.dir == tmp) {
                if (p.dir == 1 || p.dir == 2) {
                    ans += Math.min(dong.y + p.y + dong.x + p.x, dong.y + p.y + r - dong.x + r - p.x);
                } else {
                    ans += Math.min(c - dong.y + c - p.y + dong.x + p.x, dong.y + p.y + dong.x + p.x);
                }
            } else {
                ans += Math.abs(dong.y - p.y) + Math.abs(dong.x - p.x);
            }
        }
        System.out.println(ans);
        br.close();
    }
}
