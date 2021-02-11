package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_15652 {
    private static int N, M;
    private static int[] arr;
    static BufferedWriter bw =  new BufferedWriter(new OutputStreamWriter(System.out));

    private static void Recursive(int depth, int start) throws IOException {
        if (depth == M) {
            for (int i = 0; i < arr.length; i++) {
                bw.write(arr[i] + " ");
            }
            bw.write("\n");
            return;
        }

        for (int i = start; i <= N; i++) {
            arr[depth] = i;
            Recursive(depth + 1, i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[M];

        Recursive(0, 1);

        br.close();
        bw.flush();
        bw.close();
    }
}
