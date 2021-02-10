package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1068 {
    private static int[] parent;
    private static int N, ans;
    private static List<Integer>[] tree;
    private static Queue<Integer> queue;

    private static void sol() {
        while(!queue.isEmpty()) {
            Integer cur = queue.poll();
            if (parent[cur] != -1 && tree[cur].size() == 0) {
                ans++;
            } else if (parent[cur] == -1 && tree[cur].size() == 0) {
                ans = 1;
            }

            for (int i = 0; i < tree[cur].size(); i++) {
                Integer next = tree[cur].get(i);
                queue.add(next);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        parent = new int[N];
        tree = new ArrayList[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < N; i++) {
            tree[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < N; i++) {
            parent[i] = Integer.parseInt(st.nextToken());
            if (parent[i] == -1) continue;
            else {
                tree[parent[i]].add(i);
            }
        }

        int remove = Integer.parseInt(br.readLine());
        int removeParent = parent[remove];
        if (removeParent == -1) {
            tree[remove] = new ArrayList<Integer>();
        } else {
            for (int i = 0; i < tree[removeParent].size(); i++) {
                if (tree[removeParent].get(i) == remove) {
                    tree[removeParent].remove(i);
                    break;
                }
            }
        }

        queue = new LinkedList<Integer>();
        for (int i = 0; i < N; i++) {
            if (parent[i] == -1) {
                queue.add(i);
                sol();
            }
        }
        System.out.println(ans);
    }
}
