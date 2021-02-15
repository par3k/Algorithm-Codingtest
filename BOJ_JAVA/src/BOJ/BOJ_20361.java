package BOJ;

import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BOJ_20361 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken()) - 1;
        int K = Integer.parseInt(st.nextToken());

        boolean[] arr = new boolean[N];
        for (int i = 0; i < N; i++) {
            arr[X] = true;
        }

        boolean tmp;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken()) - 1;
            int B = Integer.parseInt(st.nextToken()) - 1;

            tmp = arr[A];
            arr[A] = arr[B];
            arr[B] = tmp;
        }

        for (int i = 0; i < N; i++) {
            if (arr[i]) bw.write((i + 1) + "\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}

