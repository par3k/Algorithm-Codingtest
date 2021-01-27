package BOJ;

import java.io.*;

public class BOJ_2798 {
    static int ans = 0;
    static int tmp = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputStr = br.readLine().split(" ");
        String[] arr = br.readLine().split(" ");

        int n = Integer.parseInt(inputStr[0]);
        int m = Integer.parseInt(inputStr[1]);

        for (int i = 0; i < n - 2; i++) {
            for (int j = (i + 1); j < n - 1; j++) {
                for (int k = (i + 2); k < n; k++) {
                    if (!(i == j) && !(j == k) && !(i == k)) {
                        tmp = Integer.parseInt(arr[i]) +
                                Integer.parseInt(arr[j]) +
                                Integer.parseInt(arr[k]);
                        if (m >= tmp && ans < tmp) {
                            ans = tmp;
                        }
                    }
                }
            }
        }
        br.close();
        System.out.println(ans);
    }
}
