package BOJ;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_1062 {

    static int n, k;
    static List<Integer> words = new ArrayList<>();
    static int answer = 0;
    static boolean[] alphaBool;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        k -= 5;
        for (int i = 0; i < n; i++) {
            int word = 0;
            char[] s = sc.next().toCharArray();
            for (char c: s) {
                if (anticCheck(c)) continue;
                else {
                    if (c == 'b') {
                        word |= (1 << (c-'a'-1));
                    } else if (c <= 'i') {
                        word |= (1 << (c-'a'-2));
                    } else if (c <= 'n') {
                        word |= (1 << (c-'a'-3));
                    } else if (c <= 't') {
                        word |= (1 << (c-'a'-4));
                    } else {
                        word |= (1 << (c-'a'-5));
                    }
                }
            }
            words.add(word);
        }
        if (k < 0) {
            System.out.println(answer);
            return;
        }
        for (int i = 0; i<1<<21; i++) {
            int cnt = 0;
            for (int j = 0; j<21; j++) {
                if((i &(1 <<j)) > 0) {
                    cnt++;
                }
            }
            if (cnt == k) {
                alphaBool = new boolean[21];
                for (int j = 0; j < 21; j ++) {
                    if ((i & (1<<j)) > 0) {
                        alphaBool[j] = true;
                    }
                }
                int mask = 0;
                for (int j = 0; j < 21; j++) {
                    if (alphaBool[j]) {
                        mask |= (1<<j);
                    }
                }
                check(mask);
            }
        }
        System.out.println(answer);
    }

    static boolean anticCheck(char c) {
        if (c == 'a' || c == 'n' || c == 't' || c == 'i' || c == 'c') return true;
        return false;
    }

    static void check(int mask) {
        int cnt = 0;
        for (int word : words) {
            if ((word & mask) == word) {
                cnt++;
            }
        }
        answer = answer < cnt ? cnt : answer;
    }
}
