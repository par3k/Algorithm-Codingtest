package BOJ;

import java.io.*;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.StringTokenizer;

public class BOJ_15666 {
    private static int N, M;
    private static int[] arr;
    private static int[] tmp;
    private static LinkedHashSet<String> ans;

    private static void Recursive(int depth, int start){
        if (depth == M) {
            StringBuilder sb = new StringBuilder();
            for (int i : tmp) sb.append(i).append(' ');
            ans.add(sb.toString());
            return;
        }

        int num = 0;
        for (int i = start; i < N; i++) {
            if (num == arr[i]) continue;
            tmp[depth] = arr[i];
            Recursive(depth + 1, i);
            num = arr[i];
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        tmp = new int[M];
        ans = new LinkedHashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        Recursive(0, 0);
        ans.forEach(System.out::println);
        br.close();
    }
}