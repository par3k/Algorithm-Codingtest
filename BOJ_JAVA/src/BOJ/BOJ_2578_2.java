package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2578_2 {
    private static int[][] arr;
    private static ArrayList<Integer> cmd;
    private static StringTokenizer st;

    private static int bingoCheck(int x, int y) {
        int cnt = 0;

        for (int i = 0; i < 5; i++) {
            int rowCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (arr[i][j] == -1) rowCnt++;
            }
            if (rowCnt == 5) cnt++;
        }

        for (int i = 0; i < 5; i++) {
            int colCnt = 0;
            for (int j = 0; j < 5; j++) {
                if (arr[j][i] == -1) colCnt++;
            }
            if (colCnt == 5) cnt++;
        }

        int crossCnt = 0;
        for (int i = 4; i >= 0; i--) {
            if (arr[4 - i][i] == -1) crossCnt++;
            if (crossCnt == 5) cnt++;
        }

        int crossCnt2 = 0;
        for (int i = 0; i < 5; i++) {
            if (arr[i][i] == -1) crossCnt2++;
            if (crossCnt2 == 5) cnt++;
        }

        return cnt;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        arr = new int[5][5];

        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        cmd = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                cmd.add(Integer.parseInt(st.nextToken()));
            }
        }

        int cnt = 0;
        for (int i = 0; i < 25; i++) {
            int tmp = cmd.get(i);
            cnt++;

            for (int x = 0; x < 5; x++) {
                for (int y = 0; y < 5; y++) {
                    if (arr[x][y] == tmp) {
                        arr[x][y] = -1;

                        if (bingoCheck(x, y) >= 3) {
                            System.out.println(cnt);
                            return;
                        }
                    }
                }
            }
        }
        br.close();
    }
}
