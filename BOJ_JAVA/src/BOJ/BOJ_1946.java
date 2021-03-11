package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1946 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            ArrayList<Node> arr = new ArrayList<>();
            for (int i = 0;  i< N; i++) {
                StringTokenizer st= new StringTokenizer(br.readLine());
                int s1 = Integer.parseInt(st.nextToken());
                int s2 = Integer.parseInt(st.nextToken());
                arr.add(new Node(s1, s2));
            }

            Collections.sort(arr, (s1, s2) -> s1.s1 - s2.s1);

            int tmp = arr.get(0).s2;
            int ans = 0;

            for (int i = 0; i < arr.size(); i++) {
                if (arr.get(i).s2 > tmp) {
                    ans++;
                } else {
                    tmp = arr.get(i).s2;
                }

            }
            System.out.println(N - ans);
        }
        br.close();
    }

    static class Node{
        int s1, s2;
        public Node(int s1, int s2) {
            this.s1 = s1;
            this.s2 = s2;
        }
    }
}
