package BOJ;

import java.io.*;
import java.util.Stack;

public class BOJ_17299 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = Integer.parseInt(br.readLine());
        String[] a = br.readLine().split(" ");

        int[] input = new int[num];
        int[] numCnt = new int[1000001];
        int[] ans = new int[num];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = -1;
        }

        Stack<Integer> stack = new Stack<>();

        for (int i = 0 ; i < num; i++) {
            input[i] = Integer.parseInt(a[i]);
            numCnt[input[i]]++;
        }

        // 로직부
        for (int i = 0; i < num; i++) {
            if (stack.isEmpty()) stack.push(i);
            while (!stack.isEmpty() && numCnt[input[stack.peek()]] < numCnt[input[i]]) {
                ans[stack.pop()] = input[i];
            }
            stack.push(i);
        }

        // 출력
        for (int i = 0 ; i < num; i++) {
            bw.write(ans[i] + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
