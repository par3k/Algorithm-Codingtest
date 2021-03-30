package SSAFY;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 부분집합 {
    private static int N;
    private static int[] input;
    private static boolean[] isSelected;

    private static void Powerset(int depth) {
        if (depth == N) {
            for (int i = 0 ; i < N; i++) {
                System.out.print((isSelected[i] ? input[i] : "X") + "\t");
            }
            System.out.println();
            return;
        }
        isSelected[depth] = true;
        Powerset(depth + 1);
        isSelected[depth] = false;
        Powerset(depth + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        input = new int[N];
        isSelected = new boolean[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        Powerset(0);
        br.close();
    }
}
