package SSAFY;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 다익스트라_우선순위큐 {
    private static final int INF = (int) 1e9;
    private static int n, m, start;
    private static ArrayList<ArrayList<Node>> graph;
    private static int[] d = new int[100001];

    private static void dijikstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        d[start] = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int dist = node.dist;
            int now = node.idx;

            if (d[now] < dist) continue; // 현재 노드가 이미 처리된 적이 있다면 무시

            for (int i = 0; i < graph.get(now).size(); i++) {
                int cost = d[now] + graph.get(now).get(i).dist;
                if (cost < d[graph.get(now).get(i).idx]) {
                    d[graph.get(now).get(i).idx] = cost;
                    pq.offer(new Node(graph.get(now).get(i).idx, cost));
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(br.readLine());
        graph = new ArrayList<ArrayList<Node>>();
        for (int i = 0 ; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0 ; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
        }

        Arrays.fill(d, INF);

        dijikstra(start);
//        System.out.println(graph.get(1));
        for (int i = 1; i <= n; i++) {
            if (d[i] == INF) {
                System.out.println("INF");
            } else {
                System.out.println(d[i]);
            }
        }
        br.close();
    }

    private static class Node implements Comparable<Node> {
        int idx, dist;

        public Node(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }


        @Override
        public int compareTo(Node o) {
            if (this.dist < o.dist) {
                return -1;
            }
            return 1;
        }

        @Override
        public String toString() {
            return "[" + idx +
                    ", " + dist +
                    ']';
        }
    }
}
