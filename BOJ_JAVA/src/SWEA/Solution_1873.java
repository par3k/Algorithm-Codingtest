package SWEA;

import java.io.*;

public class Solution_1873 {
    private static char[][] graph;
    private static int H, W, x, y, dir;
    private static int[] dx = {-1, 1, 0, 0}; // U D L R
    private static int[] dy = {0, 0, -1, 1};

    private static boolean check(int x, int y) {
        if  (x < 0 || x >= H || y < 0 || y >= W) return false;
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            String[] a = br.readLine().split(" ");
            H = Integer.parseInt(a[0]);
            W = Integer.parseInt(a[1]);

            graph = new char[H][W];

            for (int i = 0; i < H; ++i) { // 그래프에 데이터 입력
                graph[i] = br.readLine().toCharArray();
            }

            x = -12345;
            y = -12345;
            dir = -12345;

            for (int i = 0; i < H; ++i) { // 그래프에서 탱크 위치, 바라보고 있는 방향 찾기
                for (int j = 0; j < W; ++j) {
                    char tank = graph[i][j];
                    if (tank == '^') {
                        x = i; y = j; dir = 0;
                        break;
                    } else if (tank == 'v') {
                        x = i; y = j; dir = 1;
                        break;
                    } else if (tank == '<') {
                        x = i; y = j; dir = 2;
                        break;
                    } else if (tank == '>') {
                        x = i; y = j; dir = 3;
                        break;
                    }
                }
            }

            graph[x][y] = '.'; // 탱크가 있는 현재 자리도 평지

            int N = Integer.parseInt(br.readLine());
            char[] cmd = br.readLine().toCharArray();

            for (int i = 0 ; i < N; ++i) {
                char command = cmd[i];
                switch (command) {
                    case 'S':
                        int target_X = x;
                        int target_Y = y;

                        while (true) {
                            target_X += dx[dir];
                            target_Y += dy[dir];

                            if (!check(target_X, target_Y)) break;

                            char tmp = graph[target_X][target_Y];
                            if (tmp == '#') break; // 강철벽은 못 깸
                            if (tmp == '*') { // 벽돌벽이면
                                graph[target_X][target_Y] = '.'; // 평지가 됨
                                break;
                            }
                        }
                        break;

                    case 'U':
                        dir = 0;
                        int nX1 = x + dx[dir]; // 커맨드가 위일경우 탱크의 위쪽 좌표로 nX1, nY1 지정
                        int nY1 = y + dy[dir];

                        if (!check(nX1, nY1)) break; // 맵 밖이면 아무것도 안함
                        if (graph[nX1][nY1] == '.') { // 탱크 위의 위치가 평지면
                            x += dx[dir]; // 탱크 이동
                            y += dy[dir];
                        }
                        break;

                    case 'D':
                        dir = 1;
                        int nX2 = x + dx[dir];
                        int nY2 = y + dy[dir];

                        if (!check(nX2, nY2)) break;
                        if (graph[nX2][nY2] == '.') {
                            x += dx[dir];
                            y += dy[dir];
                        }
                        break;

                    case 'L':
                        dir = 2;
                        int nX3 = x + dx[dir];
                        int nY3 = y + dy[dir];

                        if (!check(nX3, nY3)) break;
                        if (graph[nX3][nY3] == '.') {
                            x += dx[dir];
                            y += dy[dir];
                        }
                        break;

                    case 'R':
                        dir = 3;
                        int nX4 = x + dx[dir];
                        int nY4 = y + dy[dir];

                        if (!check(nX4, nY4)) break;
                        if (graph[nX4][nY4] == '.') {
                            x += dx[dir];
                            y += dy[dir];
                        }
                        break;
                } // switch-case end
            } // command for end

            switch (dir) { // 탱크 머리 돌리기
                case 0: graph[x][y] = '^'; break;
                case 1: graph[x][y] = 'v'; break;
                case 2: graph[x][y] = '<'; break;
                case 3: graph[x][y] = '>'; break;
            }

            System.out.print("#" + tc + " ");
            for (int i = 0 ; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    System.out.print(graph[i][j]);
                }
                System.out.println();
            }
        } // tc end
        br.close();
    } // psvm end
} // class end
