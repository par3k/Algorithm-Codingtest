package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1753 {
    private static final int INF = (int) 1e9;
    private static int v, e, k;
    private static ArrayList<Node> list[];
    private static int[] d;
    private static boolean[] visited;

    private static void dijkstra(){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(k, 0));

        while(!pq.isEmpty()) {
            Node a = pq.poll();
            int a_idx = a.idx;
            if (visited[a_idx]) continue;
            visited[a_idx] = true;
            for (Node o: list[a_idx]) {
                if (d[o.idx] > d[a_idx] + o.distance) {
                    d[o.idx] = d[a_idx] + o.distance;
                    pq.add(new Node(o.idx, d[o.idx]));
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        v = Integer.parseInt(line[0]);
        e = Integer.parseInt(line[1]);
        k = Integer.parseInt(br.readLine());

        d = new int[v + 1];
        list = new ArrayList[v + 1];
        visited = new boolean[v + 1];

        for (int i = 0 ; i <= v; i++) {
            list[i] = new ArrayList<>();
        }
        Arrays.fill(d, INF);
        d[k] = 0;

        for (int i = 0 ; i < e; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            list[a].add(new Node(b, c));
        }

        dijkstra();

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= v; i++) {
            if (d[i] == INF) {
                sb.append("INF").append("\n");
            } else {
                sb.append(d[i]).append("\n");
            }
        }
        System.out.print(sb);
        br.close();
    }

    private static class Node implements Comparable<Node>{
        int idx, distance;

        public Node(int idx, int distance) {
            this.idx = idx;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }
}
