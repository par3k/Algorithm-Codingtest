package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Queue<Integer> circle = new LinkedList<>();
        Queue<Integer> ans = new LinkedList<>();

        for (int i = 1; i <= N; i++) {
            circle.add(i);
        }

        int cnt = 1;
        while (!circle.isEmpty()) {
            if (cnt == K) {
                ans.add(circle.poll());
                cnt = 1;
            }
            else {
                circle.add(circle.poll());
                cnt++;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");
        for (int i = 0; i < N - 1; i++) {
            sb.append(ans.poll()).append(", ");
        }
        sb.append(ans.poll()).append(">");
        System.out.println(sb);
    }
}
