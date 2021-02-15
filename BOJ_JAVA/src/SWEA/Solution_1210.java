package SWEA;

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Queue;
import java.util.LinkedList;

public class Solution_1210 {
    private static int[][] graph;
    private static int[] dx = {0, 0, -1};
    private static int[] dy = {-1, 1, 0};

    private static class Pair {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int tc = 1; tc <= 10; tc++) {
            int T = Integer.parseInt(br.readLine());
            graph = new int[100][100];
            Pair c = null;

            for(int i=0; i<100; i++) {
                String[] input = br.readLine().split(" ");

                for(int j=0; j<100; j++) {
                    graph[i][j] = Integer.parseInt(input[j]);

                    if(graph[i][j]==2)
                        c = new Pair(i, j);
                }
            }
            bfs(T, c);
        }
    }

    public static void bfs(int T, Pair end) {
        Queue<Pair> queue = new LinkedList<>();
        boolean[][] visited = new boolean[100][100];

        visited[end.x][end.y] = true;
        queue.add(new Pair(end.x, end.y));

        while(!queue.isEmpty()) {
            Pair tmp = queue.poll();

            if(tmp.x==0) {
                System.out.println("#"+T+" "+tmp.y);
                break;
            }

            for(int i=0; i<3; i++) {
                int nx = tmp.x+dx[i];
                int ny = tmp.y+dy[i];

                if(nx<0 || nx>=100 || ny<0 || ny>=100 || graph[nx][ny]==0 || visited[nx][ny]) continue;

                visited[nx][ny] = true;

                queue.add(new Pair(nx, ny));

                break;
            }
        }
    }
}