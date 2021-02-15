package SWEA;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_1228 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int tc = 1; tc < 11; tc++) {
            int n = Integer.parseInt(br.readLine());
            ArrayList<Integer> list = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                list.add(Integer.parseInt(st.nextToken()));
            }

            int k = Integer.parseInt(br.readLine());
            int cnt = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < k; i++) {
                String trash = st.nextToken();
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                for (int j = 0 ; j < y; j++) {
                    list.add(x, Integer.parseInt(st.nextToken()));
                    x++;
                }
                cnt++;
            }
            bw.write("#" + tc + " ");
            for (int i =0 ; i < 10; i++) {
                bw.write(list.get(i) + " ");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }

}
