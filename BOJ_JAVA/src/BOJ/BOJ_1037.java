package BOJ;

import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_1037 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            arr.add(sc.nextInt());
        }
        arr.sort(null);
        System.out.println(arr.get(0) * arr.get(N - 1));
    }
}
