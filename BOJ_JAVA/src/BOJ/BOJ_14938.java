package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_14938 {
    private static final int INF = (int) 1e9;
    private static int N, M, R; // 지역의 갯수, 수색 범위, 길의 갯수
    private static int[] items; // 아이템의 갯수
    private static ArrayList<ArrayList<Node>> graph; // 인접리스트 선언
    private static int[] d; // 최단 거리 배열
    private static boolean[] visited; // 방문 확인

    private static int dijikstra(int s) { // 우선 순위 큐 사용
        Arrays.fill(d, INF); // 배열에 값들 초기화
        Arrays.fill(visited, false);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(0, s)); // 처음 시작 노드는 거리 배열이 0이다.
        d[s] = 0; // 방문 처리

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.idx; // 거리가 가장 짧은 노드의 번호를 뽑아줌

            if (!visited[now]) {
                visited[now] = true;

                for (Node a : graph.get(now)) {
                    if (!visited[a.idx] && d[a.idx] > d[now] + a.dist) { // 방문한적이 없고 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧을경우
                        d[a.idx] = d[now] + a.dist; // 거리 배열에 값을 짧은 쪽으로 업데이트
                        pq.add(new Node(d[a.idx], a.idx)); // 그 노드의 값을 Priority Queue에 저장
                    }
                }
            }
        }

        int res = 0;
        for (int i = 1; i <= N; i++) {
            if (d[i] <= M) { // 거리 배열에 있는 값이 수색 범위 이내에 있다면
                res += items[i]; // 아이템을 전부 더해준다.
            }
        }
        return res;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        items = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        graph = new ArrayList<>();
        for (int i =0 ; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i <= R; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph.get(from).add(new Node(weight, to)); // 양방향 인접리스트 구현
            graph.get(to).add(new Node(weight, from));
        }

        d = new int[N + 1];
        visited = new boolean[N + 1];

        int ans = 0;
        for (int i = 1; i <= N; i++) {
            ans = Math.max(ans, dijikstra(i)); // 1번 노드부터 N번 노드까지 얻은 아이템중 최댓값을 저장
        }
        System.out.println(ans);
        br.close();
    }

    private static class Node implements Comparable<Node> {
        int dist, idx;

        public Node(int dist, int idx) {
            this.dist = dist;
            this.idx = idx;
        }

        @Override
        public int compareTo(Node o) {
            return dist - o.dist;
        }
    }
}
