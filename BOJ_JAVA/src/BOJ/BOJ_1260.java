package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1260 {
    private static int N, M, V;
    private static LinkedList<Integer>[] list;
    private static boolean[] visited;

    private static void dfs(int start) {
        visited[start] = true;
        System.out.print(start + " ");

        for (int i : list[start]) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(i);
            }
        }
    }

    private static void bfs(int start) {
        visited[start] = true;
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            int v = queue.pollFirst();
            System.out.print(v + " ");

            for (int i : list[v]) {
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
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        list = new LinkedList[N + 1];
        visited = new boolean[N + 1];

        for (int i = 1 ; i <=  N;  i ++) {
            list[i] = new LinkedList<>();
        }

        for (int i = 0 ; i < M; i ++){
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            list[node1].add(node2);
            list[node2].add(node1);
        }

        for (int j = 1; j <= N; j++) Collections.sort(list[j]);

        dfs(V);

        for (int i = 0; i < N + 1; i++) {
            visited[i] = false;
        }
        System.out.println();

        bfs(V);

    br.close();
    }
}
