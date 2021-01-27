package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1431 {

    public static int add(String s){
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                sum += s.charAt(i) - '0';
            }
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] arr= new String[N];

        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }

        Arrays.sort(arr, (o1, o2) -> {
            if(o1.length() < o2.length()) {
                return -1;
            } else if (o1.length() == o2.length()) {
                if (add(o1) == add(o2)) {
                    return o1.compareTo(o2);
                } else {
                    return Integer.compare(add(o1), add(o2));
                }
            } else {
                return 1;
            }
        });
        for (String i : arr) {
            System.out.println(i);
        }
        br.close();
    }
}
