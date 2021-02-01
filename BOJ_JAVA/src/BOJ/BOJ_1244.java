package BOJ;

import java.io.IOException;
import java.util.Scanner;

public class BOJ_1244 {
    private static int [] arr;

    private static void man (int n) {
        for (int i = n; i < arr.length; i += n) {
            arr[i] ^= 1; // xor op
        }
    }

    private static void woman (int n) {
        int left = n - 1; // left idx
        int right = n + 1; // right idx

        while (true) { // check the length how long do they have as same value
            if (left < 1 || right >= arr.length) break; // check the boundary
            if (arr[left] != arr[right]) break; // if they not symmetry, break
            left--; // move to left side
            right++; // move to right side
        }

        // when they checked done,
        // the pointer should go back to the starting spot.
        left++;
        right--;

        for ( ; left <= right; left++) {
            arr[left] ^= 1; // xor op
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt() + 1;

        arr = new int[N]; // initialize the arr

        for (int i = 1; i < N; i++) { // insert the data
            arr[i] = sc.nextInt();
        }

        int T = sc.nextInt();
        for (int tc = 0; tc < T; tc++) {
            int gender = sc.nextInt();
            int cmd = sc.nextInt();

            if (gender == 1) { // man's case
                man(cmd);
            } else if (gender == 2) { // woman's case
                woman(cmd);
            }
        } // tc end

        for (int i = 1; i < N; i++) {
            System.out.print(arr[i] + " ");
            if (i % 20 == 0) System.out.println();
        }
    } // psvm end
}
