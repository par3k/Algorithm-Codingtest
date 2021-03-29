package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class BOJ_1755 {
    private static ArrayList<Node> arr;
    private static String[] alphabet = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int M = Integer.parseInt(line[0]);
        int N = Integer.parseInt(line[1]);
        arr = new ArrayList<>();
        for (int i = M; i <= N; i++) {
            if (i < 10) {
                arr.add(new Node(i, alphabet[i]));
            } else {
                int ten = i / 10;
                int one = i % 10;
                arr.add(new Node(i, alphabet[ten] + " " + alphabet[one]));
            }
        }

        Collections.sort(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < arr.size(); i++) {
            if (i != 0 && i % 10 == 0) {
                sb.append("\n");
            }
            sb.append(arr.get(i).num).append(" ");
        }
        System.out.print(sb);
        br.close();
    }


    private static class Node implements Comparable<Node>{
        int num;
        String eng;

        public Node(int num, String eng) {
            this.num = num;
            this.eng = eng;
        }

        @Override
        public String toString() {
            return "[" + num + ", " + eng + "]";
        }

        @Override
        public int compareTo(Node o) {
            return this.eng.compareTo(o.eng);
        }
    }
}
