package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10819 {
    private static int N;
    private static int[] input, tmp;
    private static boolean[] chk;
    private static ArrayList<Integer> arr;

    private static void Permutation(int depth) {
        if (depth == N) {
            int sum = 0;

            for (int i = 2 ; i < N + 1; i++) {
                sum += Math.abs(tmp[i - 2] - tmp[i - 1]);
            }
            arr.add(sum);
            return;
        }

        for(int i=0; i<N; i++) {
            if(chk[i])continue;

            chk[i]=true;
            tmp[depth]=input[i];

            Permutation(depth+1);
            chk[i]=false;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        input = new int[N];
        tmp = new int[N];
        chk = new boolean[N];
        arr = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        Permutation(0);

        int max = -123456789;

        for (int i = 0 ; i <arr.size(); i++) {
            max = Math.max(arr.get(i), max);
        }

        System.out.println(max);

        br.close();
    }
}
