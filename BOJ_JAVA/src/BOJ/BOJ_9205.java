package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_9205 {
    private static int t, n;
    private static ArrayList<Node> arr;
    private static ArrayList<Integer>[] edges;
    private static boolean[] visited;


    private static boolean checkBeer(Node point1, Node point2) {
        int distance = Math.abs(point1.x - point2.x) + Math.abs(point1.y - point2.y);
        if (distance <= 1000) {
            return true;
        } else{
            return false;
        }
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer((start));
        visited[start] = true;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int i : edges[current]) {
                if (!visited[i]) {
                    queue.offer((i));
                    visited[i] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= t; tc++) {
            n = Integer.parseInt(br.readLine()); // 편의점 갯수

            arr = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int house_x = Integer.parseInt(st.nextToken());
            int house_y = Integer.parseInt(st.nextToken());
            arr.add(new Node(house_x, house_y)); // 집 좌표 넣기

            for (int i = 0; i <n; i++) {
                st = new StringTokenizer(br.readLine());
                int conv_x = Integer.parseInt(st.nextToken());
                int conv_y = Integer.parseInt(st.nextToken());
                arr.add(new Node(conv_x, conv_y)); // 편의점 좌표 넣기
            }

            st = new StringTokenizer(br.readLine());
            int festi_x = Integer.parseInt(st.nextToken());
            int festi_y = Integer.parseInt(st.nextToken());
            arr.add(new Node(festi_x, festi_y)); // 락페 좌표 넣기

//            System.out.println(arr.toString());

            visited = new boolean[n + 2];

            edges = new ArrayList[n + 2];
            for (int i = 0; i < n + 2; i++) {
                edges[i] = new ArrayList<>();
            }

            for (int i = 0; i < n + 2; i++) {
                for (int j = 0; j < n + 2; j++) {
                    if (i != j) {
                        if (checkBeer(arr.get(i), arr.get(j))) {
                            edges[i].add(j);
                        }
                    }
                }
            }

//            for (int i = 0 ; i < n + 2; i++) {
//                System.out.println(edges[i].toString());
//            }

            bfs(0);

            if (visited[n + 1]) {
                System.out.println("happy");
            } else {
                System.out.println("sad");
            }
        }

        br.close();
    }

    private static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "[" + x + ", " + y + ']';
        }
    }
}
