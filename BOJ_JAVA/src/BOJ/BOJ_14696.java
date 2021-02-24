package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_14696 {
    private static int[] arrA;
    private static int[] arrB;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            arrA = new int[5];
            for (int j = 0; j < a; j++) {
                arrA[Integer.parseInt(st.nextToken())]++;
            }

            st = new StringTokenizer(br.readLine());

            int b = Integer.parseInt(st.nextToken());
            arrB = new int[5];
            for (int j = 0; j < b; j++) {
                arrB[Integer.parseInt(st.nextToken())]++;
            }
            System.out.println(calc(arrA, arrB));
        }
        br.close();
    }

    private static char calc (int[] a, int[] b) {
        if (a[4] > b[4]) {
            return 'A';
        } else if (a[4] < b[4]) {
            return 'B';
        } else {
            if (a[3] > b[3]) {
                return 'A';
            } else if (a[3] < b[3]) {
                return 'B';
            } else {
                if (a[2] > b[2]) {
                    return 'A';
                } else if (a[2] < b[2]) {
                    return 'B';
                } else {
                    if (a[1] > b[1]) {
                        return 'A';
                    } else if (a[1] < b[1]) {
                        return 'B';
                    } else {
                        return 'D';
                    }
                }
            }
        }
    }
}
