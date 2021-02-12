package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_15649 {
    private static int N, M;
    private static int[] arr;
    private static boolean[] check;
    private static BufferedWriter bw =  new BufferedWriter(new OutputStreamWriter(System.out));

    private static void recursive(int depth, int start) throws IOException {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                bw.write(arr[i] + " ");
            }
            bw.write("\n");
            return;
        }

        for (int i = start; i <= N; i++) {
            if (check[i]) continue;

            arr[depth] = i;
            check[i] = true;
            recursive(depth + 1, start + 1);
            check[i] = false;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        check = new boolean[N + 1];


        recursive(0, 1);

        br.close();
        bw.flush();
        bw.close();
    }
}
