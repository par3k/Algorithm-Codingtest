import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solve_5357 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (; n > 0; n--) {
            String input = br.readLine();
            Stack<Character> stack = new Stack<>();

            for (int i = 0; i < input.length(); i++) {
                stack.push(input.charAt(i));
                if (stack.size() != 1) {
                    if (input.charAt(i - 1) == stack.peek()) {
                        stack.pop();
                    }
                }
            }

            for (Character c : stack) {
                sb.append(c);
            }
            sb.append("\n");
        }
        System.out.println(sb);
        br.close();
    }
}
