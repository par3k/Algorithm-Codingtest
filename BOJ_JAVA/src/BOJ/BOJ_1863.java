package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_1863 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int ans = 0;
        Stack<Integer> s = new Stack<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            int h = Integer.parseInt(st.nextToken());
            while (!s.isEmpty() && s.peek() > h) {
                ans++;
                s.pop();
            }
            if (!s.isEmpty() && s.peek() == h) continue;
            s.push(h);
        }
        while (!s.isEmpty() && s.peek() > 0) {
            ans++;
            s.pop();
        }
        System.out.println(ans);
    }
}
