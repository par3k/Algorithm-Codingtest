package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_6808 {
    private static int size = 9, win, lose;
    private static int[] gyuNum, inNum, in_tmp;
    private static boolean[] numSelect;
    private static boolean[] isSelect;

    private static void Permutation(int depth) {
        if (depth == 9) {
            int a = 0, b = 0;

            for (int i  =0; i < size; i++) {
                if (gyuNum[i] > in_tmp[i]) {
                    a += gyuNum[i] + in_tmp[i];
                } else {
                    b += gyuNum[i] + in_tmp[i];
                }
            }

            if (a > b) { // 규형 기준
                win++;
            } else if (a < b) {
                lose++;
            }

            return;
        }

        for (int i = 0; i < size; i++) {
            if (isSelect[i]) continue;

            in_tmp[depth] = inNum[i];
            isSelect[i] = true;
            Permutation(depth + 1);
            isSelect[i] = false;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            gyuNum = new int[size];
            in_tmp = new int[size];
            inNum = new int[size];
            numSelect = new boolean[2 * size + 1];
            isSelect = new boolean[2 * size + 1];
            win = 0;
            lose = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 9; i++) {
                gyuNum[i] = Integer.parseInt(st.nextToken());
                numSelect[gyuNum[i]] = true;
            }

            int cnt = 0;
            for (int i = 1; i <= size * 2; i++) {
                if (!numSelect[i]) {
                    inNum[cnt++] = i;
                }
            }

            Permutation(0);

            sb.append("#").append(tc).append(" ").append(win).append(" ").append(lose).append("\n");
        }
        System.out.println(sb);
        br.close();
    }
}
