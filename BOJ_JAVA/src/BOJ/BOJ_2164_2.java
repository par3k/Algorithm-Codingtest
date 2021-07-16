package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_2164_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        LinkedList<Integer> queue = new LinkedList<>();

        for (int i = 0; i < N; ++i) {
            queue.add(i + 1);
        }

        while (true) {
            if (queue.size() == 1) {
                System.out.println(queue.poll());
                break;
            }
            queue.poll();
            queue.add(queue.poll());
        }

        br.close();
    }
}
