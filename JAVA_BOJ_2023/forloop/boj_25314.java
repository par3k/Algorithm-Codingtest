package forloop;

import java.util.Scanner;

public class boj_25314 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = n / 4;

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= sum; ++i) {
            sb.append("long ");
        }

        sb.append("int");
        System.out.println(sb.toString());
    }
}