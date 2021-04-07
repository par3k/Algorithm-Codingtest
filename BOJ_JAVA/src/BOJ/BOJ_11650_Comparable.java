package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BOJ_11650_Comparable {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Node> arr = new ArrayList<>();

        for (int i = 0 ;i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            arr.add(new Node(x, y));
        }
        Collections.sort(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i <N; i++) {
            sb.append(arr.get(i).toString()).append("\n");
        }
        System.out.print(sb);
        br.close();
    }


    private static class Node implements Comparable<Node> {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return x + " " + y;
        }

        @Override
        public int compareTo(Node o) {
            if (x == o.x) {
                return y - o.y;
            } return x - o.x;
        }
    }
}
