import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 후위연산자 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            Stack<Character> stack = new Stack<>();
            String line = br.readLine();
            String tmp = "";

            for (int i = 0; i < N; i++) { // 중위연산자를 후위연산자로 바꿔줌
                if (line.charAt(i) != '+' && line.charAt(i) != '*') {
                    tmp += line.charAt(i); // 숫자는 tmp에 저장
                } else {
                    if (line.charAt(i) == '*') {
                        stack.push(line.charAt(i)); // 곱셈 연산자가 있으면 스택에 넣는다
                    } else {
                        do {
                            if (stack.isEmpty()) break;
                            tmp += stack.pop(); // 곱셈 연산자를 tmp에 옮겨준다
                        } while (!stack.isEmpty() && stack.peek() != '+'); // 스택이 비어있지않고, top이 숫자나 곱셈연산자일 경우에 계속
                        stack.push(line.charAt(i)); // 덧셈 연산자를 스택에 넣는다.
                    }
                }
            }

            while (!stack.isEmpty()) tmp += stack.pop(); // 스택에 있는것을 전부 tmp에 넣는다.

            Stack<Integer> op = new Stack<>(); // 숫자 연산을 위한 스택
            for (int i =0 ; i < tmp.length(); i++) { // 후위연산자로 만든것을 계산함
                if (tmp.charAt(i) != '+' && tmp.charAt(i) != '*') op.push(tmp.charAt(i) - '0'); // tmp에 숫자가 있으면 그것을 op에 푸쉬
                else {
                    int a = op.pop(); // 연산을 위한 숫자 두개 팝
                    int b = op.pop();
                    char cmd = tmp.charAt(i); // tmp에 남아있던 연산자를 꺼낸다.

                    switch (cmd) { // 곱셈인지 덧셈인지 판단해서 연산후 op에 넣는다.
                        case '*':
                            int tmp1 = a * b;
                            op.push(tmp1);
                            break;
                        case '+':
                            int tmp2 = a + b;
                            op.push(tmp2);
                            break;
                    }
                }
            }
            System.out.println("#" + tc + " " + op.peek());
        }
    }
}
