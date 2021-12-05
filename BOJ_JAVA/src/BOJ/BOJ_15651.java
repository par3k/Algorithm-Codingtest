package BOJ;

import java.util.Arrays;
import java.util.Scanner;

class Boj_15651 {
    private static int[] arr = new int[2];
    private static int N, M;
    private static void Recursive (int depth) {
        if (depth == 2) {
            for (int i = 0; i <depth; i++) {
                System.out.println(Arrays.toString(arr));
            }
        }
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                arr[depth] = i;
                Recursive(depth + 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.next());
        M = Integer.parseInt(sc.next());

        Recursive(0);
    }
}
