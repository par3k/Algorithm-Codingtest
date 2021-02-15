package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_2606 {
    static int N, M;
    static int[][] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        graph = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 1; i <= M; i++) {
            String[] tmp = br.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            graph[a][b] = graph[b][a] = 1;
        }
        System.out.println(BFS(1));
    }

    static int BFS(int start) {
        int cnt = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 1; i <= N; i++) {
                if (graph[x][i] == 1 && !visited[i]) {
                    q.offer(i);
                    visited[i] = true;
                    cnt++;
                }
            }
        }
        return cnt;
    }
}


/*
node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]
cnt = 0

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start_node):
    global cnt
    cnt +=1
    visited[start_node] = True

    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)
    return cnt -1


visited = [False] * (node + 1)
print(dfs(1))
 */