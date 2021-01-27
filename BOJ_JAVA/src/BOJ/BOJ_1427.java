package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1427 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String N = st.nextToken();

        int size = N.length();
        char[] arr = new char[size];

        for (int i = 0; i < size; i++) {
            arr[i] = N.charAt(i);
        }
        Arrays.sort(arr);

        for (int j = arr.length - 1; j >= 0; j--) {
            System.out.print(arr[j]);
        }
    }
}
