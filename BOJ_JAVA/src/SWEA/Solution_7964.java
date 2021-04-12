package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_7964 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Queue<Integer> queue =  new LinkedList<>();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int city = Integer.parseInt(st.nextToken());
            int limit = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for (int i = 0 ; i <city; i++) {
                queue.offer(Integer.parseInt(st.nextToken()));
            }

            int gate = 0;
            int distance = limit;

            for (int i = 0; i < city; i++) {
                int isGate = queue.poll();
                if (isGate == 0) {
                    distance--;
                } else if (isGate == 1) {
                    distance = limit;
                }
                if (distance == 0) {
                    gate++;
                    distance = limit;
                }
            }
            System.out.println("#" + tc + " " + gate);
        }
    }
}

/*

3
6 2
1 0 0 0 0 1
10 2
0 0 1 0 1 0 0 0 0 1
10 1
0 0 0 0 0 0 0 0 0 0
 */