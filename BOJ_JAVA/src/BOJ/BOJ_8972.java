package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_8972 {
    private static int[] dx = {1, 1, 1, 0, 0, 0, -1, -1, -1};
    private static int[] dy = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
    private static int R, C;
    private static char[][] graph;
    private static Node myArduino;
    private static LinkedList<Node> crazyArduino = new LinkedList<>();;

    private static boolean myArduinoMove(int dir) {
        int nx = myArduino.x + dx[dir];
        int ny = myArduino.y + dy[dir];

        if (graph[nx][ny] == 'R') return false;
        else {
            myArduino.x = nx;
            myArduino.y = ny;
            return true;
        }
    }

    private static boolean crazyArduinoMove() {
        int[][] tmp_graph = new int[R][C];
        int numOfCrazy = crazyArduino.size();

        for (int i = 0 ; i< numOfCrazy; i++) {
            int x = crazyArduino.peek().x;
            int y = crazyArduino.poll().y;

            int min = 123456789;
            int minX = 0;
            int minY = 0;

            for (int d = 0; d < 9; d++) {
                if (d == 4) continue;
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                    int shortDistance = Math.abs(myArduino.x - nx) + Math.abs(myArduino.y - ny);
                    if (shortDistance < min) {
                        min = shortDistance;
                        minX = nx;
                        minY = ny;
                    }
                }
            }
            if (minX == myArduino.x && minY == myArduino.y) return false;
            tmp_graph[minX][minY] += 1;
        }

        for (int i = 0 ; i < R; i++) {
            for (int j = 0; j <C; j++) {
                if (tmp_graph[i][j] == 1) {
                    crazyArduino.add(new Node(i, j));
                }
            }
        }
        return true;
    }

    private static void reDraw() {
        graph = new char[R][C];
        for (int i = 0; i < R; i++) {
            Arrays.fill(graph[i], '.');
        }
        graph[myArduino.x][myArduino.y] = 'I';

        for (int i = 0 ; i < crazyArduino.size(); i++) {
            Node p = crazyArduino.poll();
            graph[p.x][p.y] = 'R';
            crazyArduino.add(p);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];
        for (int i = 0; i < R; i++) { // 그래프 입력하기
            graph[i] = br.readLine().toCharArray();
        }

        String tmp = br.readLine();
        int[] dir = new int[tmp.length()];
        for (int i = 0 ;i < tmp.length(); i++) { // cmd 입력하기
            dir[i] = tmp.charAt(i) - '0';
        }

        for (int i = 0 ; i < R; i++) {
            for (int j = 0 ; j < C; j++) {
                if (graph[i][j] == 'R') { // 그래프에서 미친 아두이노 좌표 저장
                    crazyArduino.add(new Node(i, j));
                }
                if (graph[i][j] == 'I') { // 그래프에서 내 아두이노 좌표 저장
                    myArduino = new Node(i, j);
                }
            }
        }

        int kraj = 0;
        for (int i = 0; i < dir.length; i++) {
            if (dir[i] != 5) {
                if (!myArduinoMove(dir[i] - 1)) {
                    kraj = i + 1;
                    break;
                }
            }

            if (!crazyArduinoMove()) {
                kraj = i + 1;
                break;
            }
            reDraw();
        }
        if (kraj != 0) {
            sb.append("kraj ").append(kraj);
        } else {
            for (int i = 0; i < R; i++) {
                for (int j = 0 ; j <C; j++) {
                    sb.append(graph[i][j]);
                }
                sb.append("\n");
            }
        }
        System.out.print(sb.toString());
        br.close();
    }

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
