package SSAFY;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 순열 {
    private static int N;
    private static int[] input, nums;
    private static boolean[] isSelected;

    private static void Permutation(int depth, int flag) {
        if (depth == N) {
            System.out.println(Arrays.toString(nums));
            return;
        }
//        for (int i = 0 ; i < N; i++) {
//            if (isSelected[i]) continue;
//            nums[depth] = input[i];
//            isSelected[i] = true;
//            Permutation(depth + 1);
//            isSelected[i] = false;
//        }
        for (int i = 0 ; i < N; i++) {
            if ((flag & 1 << i) != 0) continue;
            nums[depth] = input[i];
            Permutation(depth+1, flag | 1<<i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        input = new int[N];
        nums = new int[N];
        isSelected = new boolean[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
//        Permutation(0);
        Permutation(0, 0);
        br.close();
    }
}
