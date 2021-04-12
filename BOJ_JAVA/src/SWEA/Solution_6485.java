package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_6485 {
    private static int[] arr;

    private static void Check(int a, int b) {
        for (int j = a; j <= b; j++) {
            arr[j]++;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            StringBuilder sb = new StringBuilder();
            arr = new int[5001];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                Check(A, B);
            }

            sb.append("#").append(tc).append(" ");

            int P = Integer.parseInt(br.readLine());
            for (int i = 0; i < P - 1; i++) {
                int tmp = Integer.parseInt(br.readLine());
                sb.append(arr[tmp]).append(" ");
            }
            sb.append(arr[Integer.parseInt(br.readLine())]);
            System.out.println(sb);
        }
        br.close();
    }
}

/*
2
2
1 3
2 5
5
1
2
3
4
5
2
1 100
1 50
5
1
2
3
4
5
 */