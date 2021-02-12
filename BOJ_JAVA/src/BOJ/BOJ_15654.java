package BOJ;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_15654 {
    private static int N, M;
    private static int[] arr;
    private static boolean[] chk;
    private static int[] tmp;
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static void Recursive(int depth) throws IOException{
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                bw.write(tmp[i] + " ");
            }
            bw.write("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (chk[i]) continue;

            tmp[depth] = arr[i - 1];
            chk[i] = true;
            Recursive(depth + 1);
            chk[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        chk = new boolean[N + 1];
        tmp = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        Recursive(0);

        br.close();
        bw.flush();
        bw.close();
    }
}
