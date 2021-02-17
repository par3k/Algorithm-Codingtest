package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_2605 {
    private static int n;
    private static int[] cmd;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        cmd = new int[n];

        for (int i = 0; i < n; i++) {
            cmd[i] = Integer.parseInt(st.nextToken());
        }

        LinkedList<Integer> list=new LinkedList<>();

        for(int i = 0; i < n; i++)
            list.add(list.size() - cmd[i], i + 1);

        for(int i = 0; i < n; i++)
            System.out.print(list.get(i) + " ");
    }
}
