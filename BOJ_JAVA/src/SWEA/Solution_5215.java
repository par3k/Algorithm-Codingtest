package SWEA;

import java.io.*;
import java.util.StringTokenizer;

public class Solution_5215 {
    private static int[] score;
    private static int[] calorie;
    private static int N, L;
    private static int max;


    private static void hambug(int cnt, int sum, int cal) {
        if (cal > L) return;
        if (cnt == N) {
            if (cal <= L) {
                if (max < sum) {
                    max = sum;
                }
            }
            return;
        }
        hambug(cnt + 1, sum + score[cnt], cal + calorie[cnt]);
        hambug(cnt + 1, sum, cal);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc < T + 1; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            max = 0;
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            score = new int[N];
            calorie = new int[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                score[i] = Integer.parseInt(st.nextToken());
                calorie[i] = Integer.parseInt(st.nextToken());
            }
            hambug(0, 0, 0);
            bw.write("#" + tc + " " + max + "\n");
        } // end tc
        br.close();
        bw.flush();
        bw.close();
    }
}
