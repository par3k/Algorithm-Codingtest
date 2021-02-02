package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_2164 {
    private static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 1; i <= N; i++) {
            queue.add(i);
        }

        for (int i = 0; i < N; i++) {
            if (queue.size() == 1) {
                System.out.println(queue.poll());
                break;
            }
            queue.poll();
            queue.add(queue.poll());
        }
    }
}
