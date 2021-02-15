package BOJ;

import java.io.*;
import java.util.Stack;

public class BOJ_1918 {
    public static int Check_Op(char c) {
        switch (c) {
            case '*':
            case '/':
                return 2;
            case '+':
            case '-':
                return 1;
            case '(':
            case ')':
                return 0;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> op = new Stack<>();
        StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        char[] s = br.readLine().toCharArray();

        for (int i = 0; i < s.length; i++) {
            int op_check = Check_Op(s[i]);
            char c = s[i];

            switch (c) {
                case '+':
                case '-':
                case '*':
                case '/':
                    while (!op.isEmpty() && Check_Op(op.peek()) >= op_check) {
                        sb.append(op.pop());
                    }
                    op.push(c);
                    break;
                case '(':
                    op.push(c);
                    break;
                case ')':
                    while (!op.isEmpty() && op.peek() != '(') {
                        sb.append(op.pop());
                    }
                    op.pop();
                    break;
                default:
                    sb.append(c);
            }
        }
        while(!op.isEmpty()) {
            sb.append(op.pop());
        }
        bw.write(sb.toString() + "\n");
        br.close();
        bw.flush();
        bw.close();
    }
}
