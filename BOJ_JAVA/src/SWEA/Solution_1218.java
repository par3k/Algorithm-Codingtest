package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution_1218 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc < 11; tc++) {
            int N = Integer.parseInt(br.readLine());
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();
            int ans = 0;

            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);

                if (c == ')' && stack.peek() == '(') stack.pop();
                else if (c == ']' && stack.peek() == '[') stack.pop();
                else if (c == '>' && stack.peek() == '<') stack.pop();
                else if (c == '}' && stack.peek() == '{') stack.pop();
                else {
                    stack.push(c);
                }
            }
            if (stack.isEmpty()) ans = 1;
            else ans = 0;

            System.out.println("#" + tc + " " + ans);
        }
    }
}
