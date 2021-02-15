package BOJ;

import java.io.*;
import java.util.*;

public class BOJ_1158 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> list = new ArrayList<>();
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= n; i++)
            list.add(i);

        StringBuilder sb = new StringBuilder("<");
        int i = k - 1;

        while(true) {
            sb.append(list.get(i));
            list.remove(i);

            if(list.size() == 0) {
                sb.append(">");
                break;
            }else
                sb.append(", ");
            i += k - 1;

            if(i >= list.size()) i %= list.size();
        }
        System.out.println(sb);
    }
}
