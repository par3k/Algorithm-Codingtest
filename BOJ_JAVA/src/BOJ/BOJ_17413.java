package BOJ;

import java.io.*;
import java.util.Stack;

public class BOJ_17413 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        Stack<Character> stack = new Stack<>();

        boolean tag = false;

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '<') {
                tag = true;
                while(!stack.isEmpty()) bw.write(stack.pop());
                bw.write(str.charAt(i));
            } else if (str.charAt(i) == '>') {
                tag = false;
                bw.write(str.charAt(i));
            } else if (tag) {
                bw.write(str.charAt(i));
            } else {
                if (str.charAt(i) == ' ') {
                    while(!stack.isEmpty()) bw.write(stack.pop());
                    bw.write(str.charAt(i));
                } else {
                    stack.push(str.charAt(i));
                }
            }
        }

        while(!stack.isEmpty()) bw.write(stack.pop());

        br.close();
        bw.flush();
        bw.close();
    }
}
