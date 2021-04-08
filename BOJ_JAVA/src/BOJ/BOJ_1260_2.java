package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1260_2 {
    private static int N, M, V;
    private static LinkedList<Integer>[] graph;
    private static boolean[] visited;
    private static StringBuilder sb;

    private static void dfs(int start) {
        visited[start] = true;
        sb.append(start).append(" ");
        for (int i : graph[start]) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(i);
            }
        }
    }

    private static void bfs(int start) {
        visited[start] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int v = queue.poll();
            sb.append(v).append(" ");
            for (int i : graph[v]) {
                if (!visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new LinkedList[N + 1];
        for (int i = 1 ; i <= N; i++) {
            graph[i] = new LinkedList<>();
        }

        for (int i = 0 ; i < M; i ++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph[from].add(to);
            graph[to].add(from);

        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        visited = new boolean[N + 1];
        dfs(V);

        sb.append("\n");

        for (int i = 0 ; i < visited.length; i++) {
            visited[i] = false;
        }

        bfs(V);

        System.out.print(sb);
        br.close();
    }
}
