package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_12517 {
    public static char[] mo = {'a', 'e', 'i', 'o', 'u'};
    public static char[] za = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                                'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z'};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        ArrayList<String> arr = new ArrayList<>();

        for (int tc = 1; tc < T + 1; tc++) {
            String str = br.readLine();
            arr.add(str);
        }
        System.out.println(arr);
    }
}
