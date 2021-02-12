package BOJ;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_15656 {
    private static int N, M;
    private static int[] arr;
    private static int[] tmp;
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static void Recursive(int depth, int start) throws IOException {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                bw.write(tmp[i] + " ");
            }
            bw.write("\n");
            return;
        }

        for (int i = start; i < N; i++) {
            tmp[depth] = arr[i];
            Recursive(depth + 1, i);

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        tmp = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        Recursive(0, 0);

        br.close();
        bw.flush();
        bw.close();
    }
}
