package BOJ;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_2493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        Stack<Integer> idx = new Stack<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int first = Integer.parseInt(st.nextToken());

        stack.push(first);
        idx.push(1);
        sb.append("0 ");

        for (int i = 2; i < N + 1; i++) {
            int a = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty()) {
                if (a < stack.peek()) {
                    sb.append(idx.peek() + " ");
                    break;
                }
                stack.pop();
                idx.pop();
            }

            if (stack.isEmpty()) {
                sb.append("0 ");
            }

            stack.push(a);
            idx.push(i);
        }

        bw.write(sb.toString() + "\n");

        br.close();
        bw.flush();
        bw.close();
    }
}
