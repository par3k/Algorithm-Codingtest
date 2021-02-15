package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11729 {
    static int from = 1;
    static int aux = 2;
    static int to = 3;
    static int cnt = 0;
    static StringBuilder sb = new StringBuilder("");
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        hanoi(N, from, to, aux);
        System.out.println(cnt);
        System.out.println(sb);

    }

    private static void hanoi(int N, int from, int to, int aux) {
        cnt++;
        if (N == 1) {
            sb.append(from + " " + to + "\n");
            return;
        }
        hanoi(N - 1, from, aux, to);
        sb.append(from + " " + to + "\n");
        hanoi(N - 1, aux, to, from);
    }
}
