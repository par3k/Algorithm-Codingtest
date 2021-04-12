package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_무선충전 {
    private static int M, A;
    private static int[] dx = {0, 1, 0, -1, 0};
    private static int[] dy = {0, 0, 1, 0, -1};
    private static StringTokenizer st;
    private static ArrayList<Node> arr;
    private static int[] moveA, moveB;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            String[] line = br.readLine().split(" ");
            M = Integer.parseInt(line[0]);
            A = Integer.parseInt(line[1]);

            st = new StringTokenizer(br.readLine());
            moveA = new int[M];
            for (int i = 0; i < M; i++) {
                moveA[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            moveB = new int[M];
            for (int i = 0; i < M; i++) {
                moveB[i] = Integer.parseInt(st.nextToken());
            }

            arr = new ArrayList<>();
            for (int i = 0; i < A; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());

                arr.add(new Node(x, y, c, p));
            }

            int answer = charge();
            System.out.println("#" + tc + " " + answer);
        }
        br.close();
    }

    private static int charge() {
        int x1 = 1;
        int y1 = 1;

        int x2 = 10;
        int y2 = 10;

        int sum = getMax(x1, y1, x2, y2);

        for (int time = 0; time < M; time++) {
            x1 += dx[moveA[time]];
            y1 += dy[moveA[time]];

            x2 += dx[moveB[time]];
            y2 += dy[moveB[time]];

            sum += getMax(x1, y1, x2, y2);
        }

        return sum;
    }

    private static int getMax(int x1, int y1, int x2, int y2) {
        int[][] amount = new int[2][A];

        for (int i = 0; i< A; i++) {
            amount[0][i] = check(x1, y1, i);
        }

        for (int i = 0; i < A; i++) {
            amount[1][i] = check(x2, y2, i);
        }

        int res = 0;
        for (int i = 0; i < A; i++) {
            for (int j = 0 ; j < A; j++) {
                int sum = amount[0][i] + amount[1][j];

                if (i == j && amount[0][i] == amount[1][j]) {
                    sum /= 2;
                }

                if (sum > res) {
                    res = sum;
                }
            }
        }

        return res;
    }

    private static int check(int x, int y, int num) {
        int a = Math.abs(x - arr.get(num).x);
        int b = Math.abs(y - arr.get(num).y);
        int dist = a + b;

        if (dist <= arr.get(num).c) {
            return arr.get(num).p;
        } else {
            return 0;
        }
    }

    private static class Node{
        int x, y, c, p;

        public Node(int x, int y, int c, int p) {
            this.x = x;
            this.y = y;
            this.c = c;
            this.p = p;
        }
    }

}