package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_1225 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());

            Queue<Integer> arr = new LinkedList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 8; i++) {
                arr.offer(Integer.parseInt(st.nextToken()));
            }

            outer:
            while (true) {
                for (int i = 1; i <= 5; i++) {
                    int front = arr.poll();
                    front -= i;
                    if (front < 1) front = 0;
                    arr.offer(front);
                    if (front == 0) break outer;
                }
            }

            System.out.print("#" + N + " ");
            while (!arr.isEmpty()) {
                System.out.print(arr.poll() + " ");
            }
            System.out.println();
        }
        br.close();
    }
}
