package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1486 {
    private static int N, B, min_height;
    private static int[] arr;

    private static void solution(int idx, int height) { // 부분집합
        if (B <= height && height < min_height) {
            min_height = height;
        }
        if (idx == N) return;
        solution(idx + 1, height);
        solution(idx + 1, height + arr[idx]);

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            String[] line = br.readLine().split(" ");
            N = Integer.parseInt(line[0]);
            B = Integer.parseInt(line[1]);
            min_height = 123456789;

            arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0 ; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            solution(0, 0);
            sb.append("#").append(tc).append(" ").append(min_height - B).append("\n");
        }
        System.out.println(sb);
        br.close();
    }
}
