package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_16918 { // 봄버맨
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static int r, c, n;
    private static char[][] graph;
    private static Deque<Node> queue;

    private static void allBombSet() {
        for (int i = 0; i <r; i++) {
            for (int j = 0; j < c; j++) {
                if (graph[i][j] != 'O') graph[i][j] = 'O';
            }
        }
    }

    private static void bomb() {
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int x = node.x;
            int y = node.y;

            graph[x][y] = '.';

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                    if (graph[nx][ny] == 'O') graph[nx][ny] = '.';
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken()) - 1;
        graph = new char[201][201];

        for (int i = 0; i < r; i++) {
            String a = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = a.charAt(j);
            }
        }


        while (n > 0){
            queue = new LinkedList<>();
            for (int i = 0 ; i < r; i++) {
                for (int j = 0 ; j < c; j++) {
                    if (graph[i][j] == 'O')
                        queue.offer(new Node(i, j));
                }
            }
            allBombSet();
            n--;
            bomb();
            n--;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                sb.append(graph[i][j]);
            }
            sb.append("\n");
        }
        System.out.print(sb);
        br.close();
    }

    private static class Node{
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
