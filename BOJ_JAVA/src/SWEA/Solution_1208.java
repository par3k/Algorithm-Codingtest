package SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1208 {
    private static int[] ans = new int[10];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 0; tc < 10; tc++) {
            int[] arr = new int[100];
            int N = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < 100; i++){
                arr[i] = Integer.parseInt(st.nextToken()); // 상자값 입력
            }


            Arrays.sort(arr);
            for (int i = 0; i < N; i++) {
                arr[0]++;
                arr[99]--;
                Arrays.sort(arr);
            }
            ans[tc] = arr[99] - arr[0];

        }

        for (int i = 0; i < 10; i++) {
            System.out.println("#" + (i + 1) + " " + ans[i]);
        }

    }// main
}// class-end