package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Solution_1251 {
    private static int N;
    private static double E;
    private static int[] parent;
    private static Node[] island;

    private static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    private static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) parent[y] = x;
    }

    private static double calc(long x, long y, long dx, long dy) {
        return E * Math.pow(Math.sqrt(Math.pow(dx - x, 2) + Math.pow(dy - y, 2 )), 2);
    } // E * L ^ 2

    private static boolean isSameParent(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) return false;
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            island = new Node[N];
            String[] tmp = br.readLine().split(" ");
            for (int i = 0 ; i < N; i++) { // x좌표
                island[i] = new Node(Integer.parseInt(tmp[i]), 0, 0);
            }
            tmp = br.readLine().split(" ");
            for (int i = 0 ; i < N; i++) { // y좌표
                island[i].y = Integer.parseInt(tmp[i]);
            }
            E = Double.parseDouble(br.readLine()); // 환경 부담 세율

            ArrayList<Node> weights = new ArrayList<>();
            for (int i = 0 ; i < N - 1; i++) { // 모든 점들과 각각의 weight 구하기
                for (int j = i + 1; j < N; j++) {
                    weights.add(new Node(i, j, calc(island[i].x, island[i].y, island[j].x, island[j].y)));
                }
            }

            Collections.sort(weights, new Comparator<Node>() { // 크루스칼 알고리즘을 위해 weight 기준으로 정렬
                @Override
                public int compare(Node o1, Node o2) {
                    if (o1.weight < o2.weight) {
                        return -1;
                    } else if (o1.weight > o2.weight) {
                        return 1;
                    }
                    return 0;
                }
            });

            parent = new int[N]; // 유니온 파인드를 쓰기 위해 parent 배열 초기화
            for (int i = 0 ; i < N; i++) {
                parent[i] = i;
            }

            double ans = 0.0;
            for (int i = 0; i < weights.size(); i++) {
                if (!isSameParent(weights.get(i).x, weights.get(i).y)) { // 같은 부모인지 확인, 부모가 같지않다면 연결되어 있지 않으므로 union 필요
                    union(weights.get(i).x, weights.get(i).y); // union
                    ans = ans + weights.get(i).weight; // weight
                }
            }
            System.out.format("#%d %.0f\n", tc, ans);
        } // tc end
        br.close();
    } // psvm end

    private static class Node{
        int x, y;
        double weight;

        public Node(int x, int y, double weight) {
            this.x = x;
            this.y = y;
            this.weight = weight;
        }
    }
}
