package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution_1223 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 0; tc <= 10; tc++) {

            int N = Integer.parseInt(br.readLine());
            Stack<Character> op_store = new Stack<>();
            String line = br.readLine();
            String postFix = "";

            for (int i = 0; i < N; i++) {
                if (line.charAt(i) != '+' && line.charAt(i) != '*') {
                    postFix += line.charAt(i);
                } else {
                    if (line.charAt(i) == '*') {
                        op_store.push(line.charAt(i));
                    } else {
                        do {
                            if (op_store.isEmpty()) break;
                            postFix += op_store.pop();
                        } while (!op_store.isEmpty() && op_store.peek() != '+');
                        op_store.push(line.charAt(i));
                    }
                }
            }

            while (!op_store.isEmpty()) postFix += op_store.pop();

            Stack<Integer> op = new Stack<>();
            for (int i =0; i < postFix.length(); i++) {
                if (postFix.charAt(i) != '+' && postFix.charAt(i) != '*') {
                    op.push(postFix.charAt(i) - '0');
                } else {
                    int op1 = op.pop();
                    int op2 = op.pop();
                    char operator = postFix.charAt(i);
                    switch (operator) {
                        case '*':
                            int tmp1 = op1 * op2;
                            op.push(tmp1);
                            break;
                        case '+':
                            int tmp2 = op1 + op2;
                            op.push(tmp2);
                            break;
                    }
                }
            }
            System.out.println("#" + tc + 1 + " " + op.peek());
        }
    }
}
