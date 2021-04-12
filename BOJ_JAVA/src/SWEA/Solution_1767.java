package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_1767 {
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int N, maxCore, coreNum, ans;
    private static int[][] graph;
    private static ArrayList<Pair> arr;

    // 길이 체크
    private static int wireChk (int x, int y, int i) {
        int len = 0;
        while (true) {
            x += dx[i];
            y += dy[i];

            if (0 > x || x >= N || 0 > y || x >= N) {
                return len;
            } else if (graph[x][y] != 0) {
                return 0;
            }
            len++;
        }
    }

    // dfs 한방향으로만 가야되
    private static void dfs(int idx, int cnt, int len) {
        if (idx == coreNum) return;
        if (maxCore > cnt + (coreNum - idx)) return;

        if (cnt > maxCore) {
            ans = len;
            maxCore = cnt;
        } else if (cnt == maxCore) {
            ans = Math.min(ans, len);
        }

        Pair p  = arr.get(idx);
        int x = p.x;
        int y = p.y;

        for (int i = 0; i < 4; i++) {

            int wireLen = wireChk(x, y, i);
            if (wireLen > 0) {
                makeSet(x, y, i, 2);
                dfs(i + 1, cnt + 1, len + wireLen);
                makeSet(x, y, i, 0);
            }
        }

    }

    private static void makeSet (int x, int y, int i, int val) {
        while (true) {
            x += dx[i];
            y += dy[i];
            if (x < 0 || x >= N || y < 0 || y >= N) return;
            graph[x][y] = val;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            graph = new int[N][N]; // 0 ~ 4 까지 가는 5X5 배열 생성
            arr = new ArrayList<>();
            coreNum = 0;
            maxCore = 0;

            for (int i = 0 ; i< N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0 ;j < N ; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());

                    if (i == 0 || j == 0 || i == N - 1 || j == N - 1) { // 가장자리 스킵
                        continue;
                    } else if (graph[i][j] == 1) { // 코어가 몇 개인지 새주기 와 값 넣어 주기
                        arr.add(new Pair(i, j));
                        coreNum++;
                    }
                }
            } // 입력 for 끝

            dfs(0, 0, 0);
            System.out.println("#" + tc + " " + ans);
        } // tc 루프 끝
        br.close();
    }

    static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
