package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution_1238 {
    private static LinkedList<Integer>[] list;

    private static int bfs(int start) {
        int lastCNT = -123456789;
        int lastNode = -123456789;
        boolean[] visited = new boolean[101];

        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(start, 0));
        visited[start] = true;

        while (!queue.isEmpty()) {
            Node q = queue.poll();
            int now = q.now;
            int nowCNT = q.cnt;

            if (lastCNT == nowCNT && lastNode <= now) {
                lastNode = now;
            } else if (lastCNT < nowCNT) {
                lastCNT = nowCNT;
                lastNode = now;
            }

            for (int i = 0 ; i < list[now].size(); i++) {
                int next = list[now].get(i);
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(new Node(next, nowCNT + 1));
                }
            }
        }
        return lastNode;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc =1; tc <= 10; tc++) {
            String[] line = br.readLine().split(" ");
            int n = Integer.parseInt(line[0]);
            int startNode = Integer.parseInt(line[1]);

            list = new LinkedList[101];
            Set<String> set = new HashSet<>();

            for (int i = 0 ; i < 101; i++) {
                list[i] = new LinkedList<>();
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                String token = from + " " + to;
                set.add(token);
            }

            for (String e: set) {
                String[] tmp = e.split(" ");
                list[Integer.parseInt(tmp[0])].add(Integer.parseInt(tmp[1]));
            }

            sb.append("#").append(tc).append(" ").append(bfs(startNode)).append("\n");
        }
        System.out.print(sb.toString());
        br.close();
    }

    private static class Node{
        int now, cnt;

        public Node(int now, int cnt) {
            this.now = now;
            this.cnt = cnt;
        }
    }
}
