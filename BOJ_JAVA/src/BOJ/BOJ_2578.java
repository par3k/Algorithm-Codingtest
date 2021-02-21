package BOJ;

import java.util.Scanner;

public class BOJ_2578 {
    private static int[][] graph;

    private static int check(int r, int c) {
        int cnt = 0;

        for (int i = 0; i < 5; i++) {
            int rowCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (graph[i][j] == -1) rowCnt++;
            }
            if (rowCnt == 5) cnt++;
        }

        for (int i = 0; i < 5; i++) {
            int colCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (graph[j][i] == -1) colCnt++;
            }
            if (colCnt == 5) cnt++;
        }

        int crossCnt = 0;
        for (int i = 4; i >= 0; i--) {
            if (graph[4 - i][i] == -1) crossCnt++;
            if (crossCnt == 5) cnt++;
        }

        crossCnt = 0;
        for (int i = 0; i < 5; i++) {
            if (graph[i][i] == -1) crossCnt++;
            if (crossCnt == 5) cnt++;
        }

        return cnt;
    }



    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        graph = new int[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        int cnt = 0;


        for (int i = 0; i < 25; i++) {
            int cmd = sc.nextInt();
            cnt++;

            for (int x = 0; x < 5; x++) {
                for (int y = 0; y < 5; y++) {
                    if (graph[x][y] == cmd) {
                        graph[x][y] = -1;

                        if (check(x, y) >= 3) {
                            System.out.println(cnt);
                            return;
                        }
                    }
                }
            }
        }
        sc.close();
    }
}
