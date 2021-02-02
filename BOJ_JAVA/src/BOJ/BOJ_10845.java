package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_10845 {
    private static Queue<Integer> queue = new LinkedList<>();
    static int X;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int Order = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < Order; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String cmd = st.nextToken();

            if (cmd.equals("push")) {
                X = Integer.parseInt(st.nextToken());
                queue.add(X);
            } else if (cmd.equals("pop")) {
                if (queue.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(queue.poll());
                }
            } else if (cmd.equals("size")) {
                System.out.println(queue.size());
            } else if (cmd.equals("empty")) {
                if (queue.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (cmd.equals("front")) {
                if (queue.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(queue.peek());
                }
            } else if (cmd.equals("back")) {
                if (queue.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(X);
                }
            }
        }
    }
}
