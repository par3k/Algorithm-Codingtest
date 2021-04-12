package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Solution_보급로 {
    private static int N;
    private static char[][] graph;
    private static int[][] memory;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringBuilder sb = new StringBuilder();
            N = Integer.parseInt(br.readLine());
            graph = new char[N][];
            memory = new int[N][N];

            for (int i = 0 ; i < N; i++) {
                graph[i] = br.readLine().toCharArray();
                Arrays.fill(memory[i], Integer.MAX_VALUE / 2);
            }

            Queue<Node> queue = new LinkedList<>();
            memory[0][0] = 0;
            queue.offer(new Node(0, 0, 0)); // 초기화

            while (!queue.isEmpty()) {
                Node tmp = queue.poll();

                for (int k = 0; k < 4; k++) {
                    int x = tmp.x + dx[k];
                    int y = tmp.y + dy[k];

                    if (0 <= x && x < N && 0 <= y && y < N) {
                        int time = tmp.val + Integer.parseInt("" + graph[x][y]);
                        if (memory[x][y] > time) {
                            memory[x][y] = time;
                            queue.offer(new Node(x, y, memory[x][y]));
                        }
                    }
                }
            }

            sb.append("#").append(tc).append(" ").append(memory[N-1][N-1]);
            System.out.println(sb);
        }
        br.close();
    }

    private static class Node{
        int x, y, val;

        public Node(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }
}
