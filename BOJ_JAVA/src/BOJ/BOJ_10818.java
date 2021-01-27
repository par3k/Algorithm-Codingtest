package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_10818 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for ( int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] > max) {
                max = arr[i];
            }

            if (arr[i] < min) {
                min = arr[i];
            }
        }
        System.out.println(min + " " + max);
        br.close();

    }
}
