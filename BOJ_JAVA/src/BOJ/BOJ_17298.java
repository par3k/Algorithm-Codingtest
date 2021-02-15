package BOJ;

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        Stack<Integer> stack = new Stack<>();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] ans = new int[N];
        for (int i = 0 ; i < N; i++) {
            ans[i] = -1;
        }

        stack.push(0);
        for (int i = 1; i < N; i++) {
            if (stack.isEmpty()) stack.push(i);
            while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
                ans[stack.peek()] = arr[i];
                stack.pop();
            }
            stack.push(i);
        }

        for(int i=0; i<ans.length; i++) {
            bw.write(ans[i] + " ");
        }
        bw.write("\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
