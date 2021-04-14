package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_5656 { // 벽돌 깨기
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int N, W, H, answer;
    private static int[][] graph;

    private static void copyGraph(int[][] graph, int[][] graph2) {
        for (int i = 0 ; i < H; i++) {
            for (int j = 0 ; j < W; j++) {
                graph2[i][j] = graph[i][j];
            }
        }
    }

    private static int burst(int[][] graph, int x, int y) {
        int cnt = 0;
        Queue<Node> queue = new LinkedList<>();
        if (graph[x][y] > 1) {
            queue.offer(new Node(x, y, graph[x][y]));
        }
        graph[x][y] = 0;
        cnt++;
        // 이부분이 지옥이네
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            for (int d = 0; d < 4; d++) {
                int x2 = node.x;
                int y2 = node.y;
                for (int k = 0; k < node.range - 1; k++) {
                    x2 += dx[d];
                    y2 += dy[d];
                    if (x2 < 0 || x2 >= H || y2 < 0 || y2 >= W || graph[x2][y2] == 0) continue;
                    if (graph[x2][y2] > 1) queue.offer(new Node(x2, y2, graph[x2][y2]));
                    graph[x2][y2] = 0;
                    cnt++;
                }
            }
        }
        return cnt;
    }

    private static void downBrick(int[][] graph) {
        for (int y = 0; y < W; y++) {
            int x = H - 1;
            while(x > 0) {
                if (graph[x][y] == 0) {
                    int nx = x - 1;
                    while(nx > 0 && graph[nx][y] == 0) nx--;
                    graph[x][y] = graph[nx][y];
                    graph[nx][y] = 0;
                }
                x--;
            }
        }
    }

    private static boolean Combination(int depth, int remain, int[][] map) {
        if (remain == 0) {
            answer = 0;
            return true;
        }

        if (depth == N) {
            answer = Math.min(answer, remain);
            return false;
        }

        int[][] newMap = new int[H][W];
        for (int j = 0; j < W; j++) {
            int i = 0;
            while (i < H && map[i][j] == 0) ++i;
            if (i == H) continue;
            copyGraph(map, newMap);
            int burstCnt = burst(newMap, i, j);
            downBrick(newMap);
            if (Combination(depth + 1, remain - burstCnt, newMap)) return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            graph = new int[H][W];
            answer = Integer.MAX_VALUE;

            int totalBrick = 0;
            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j =0; j < W; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if (graph[i][j] > 0) totalBrick++;
                }
            }

            StringBuilder sb = new StringBuilder();
            Combination(0, totalBrick, graph);
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
            System.out.print(sb);
        }
        br.close();
    }
    private static class Node {
        int x, y, range;

        public Node(int x, int y, int range) {
            this.x = x;
            this.y = y;
            this.range = range;
        }
    }
}
