package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BOJ_8979 {
    private static int N, K;
    private static ArrayList<Node2> arr = new ArrayList<>();;
    private static int end_point = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int no = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());
            arr.add(new Node2(no, gold, silver, bronze, 0));
        }
        Collections.sort(arr);
        arr.get(0).rank = 1;

        for (int i = 1; i < arr.size(); i++) {
            int tmp_gold = arr.get(i - 1).gold;
            int tmp_silver = arr.get(i - 1).silver;
            int tmp_bronze = arr.get(i - 1).bronze;
            Node2 now = arr.get(i);

            if (arr.get(i).no == K) {
                end_point = i;
            }
            if (now.gold == tmp_gold && now.silver == tmp_silver && now.bronze == tmp_bronze) {
                arr.get(i).rank = arr.get(i - 1).rank;
            } else {
                arr.get(i).rank = i + 1;
            }
        }
        System.out.println(arr.get(end_point).rank);
    }
}

class Node2 implements Comparable<Node2> {
    int no;
    int gold;
    int silver;
    int bronze;
    int rank;

    public Node2(int no, int gold, int silver, int bronze, int rank) {
        this.no = no;
        this.gold = gold;
        this.silver = silver;
        this.bronze = bronze;
        this.rank = rank;
    }

    @Override
    public int compareTo(Node2 o) {
        if (this.gold == o.gold) {
            if (this.silver == o.silver) {
                return o.bronze - this.bronze;
            } else {
                return o.silver - this.silver;
            }
        } else {
            return o.gold - this.gold;
        }
    }
}