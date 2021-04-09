package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_15686 {
    private static int N, M;
    private static int[][] graph;
    private static int ans = 123456789;
    private static ArrayList<Pair> house = new ArrayList<>();
    private static ArrayList<Pair> chicken = new ArrayList<>();

    private static void Combination(int depth, int n, int r, boolean[] visited) {
        if (r == 0) {
            ArrayList<Pair> list = new ArrayList<>(); // list에 뽑힌 치킨집 담을 예정
            for (int i = 0; i < n; i++) {
                if (visited[i]) {
                    list.add(new Pair(chicken.get(i).x, chicken.get(i).y));
                }
            }
            ans = Math.min(ans, DistanceCalc(list)); // 치킨거리 최소값 담기
            return;
        }
        if (depth == n) return;

        visited[depth] = true;
        Combination(depth + 1, n, r - 1, visited);

        visited[depth] = false;
        Combination(depth + 1, n, r, visited);
    }

    private static int DistanceCalc (ArrayList<Pair> list) { // 집과 가장 가까운 치킨집의 치킨거리 구하고
        int sum = 0;

        for (int i = 0; i < house.size(); i++) {
            int tmp = 123456789;
            for (int j = 0; j < list.size(); j++) {
                int distance = Math.abs(house.get(i).x - list.get(j).x) + Math.abs(house.get(i).y - list.get(j).y);
                tmp = Math.min(tmp, distance);
            }
            sum += tmp; // 모든 치킨거리의 합을 구함
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken()); // 맵에 데이터 저장
                if (graph[i][j] == 1) { // 집이 있으면 house 배열에 좌표를 쌍으로 묶어 저장
                    house.add(new Pair(i, j));
                } else if (graph[i][j] == 2) { // 치킨집이 있으면 chicken 배열에 좌표를 쌍으로 묶어 저장
                    chicken.add(new Pair(i, j));
                }
            }
        }

        boolean[] visited = new boolean[chicken.size()];
        Combination(0, chicken.size(), M, visited); // 치킨집의 갯수와 뽑을 수를 지정해서 조합을 돌려본다
        System.out.println(ans);
        br.close();
    }

    static class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}

