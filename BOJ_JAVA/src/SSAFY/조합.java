package SSAFY;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 조합 {
    private static int N, R;
    private static int[] input, num;

    private static void Combination(int depth, int start) {
        if (depth == R) {
            System.out.println(Arrays.toString(num));
            return;
        }

        for (int i = start; i < N; i++) {
            num[depth] = input[i];
            Combination(depth + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        R = Integer.parseInt(br.readLine());
        input = new int[N];
        num = new int[R];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
        Combination(0, 0);
        br.close();
    }
}
