package SWEA;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SWEA_1208 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc < 11; tc++) {

            int Dump = Integer.parseInt(br.readLine());

            int[] arr = new int[100];

            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < 100; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            int cnt = 0;
            while (true) {
                if (Dump == cnt) break;
                Arrays.sort(arr);
                arr[99]--;
                arr[0]++;
                cnt++;
            }
            Arrays.sort(arr);
            System.out.println("#" + tc + " " + (arr[99] - arr[0]));
        }// tc end
    }
}


