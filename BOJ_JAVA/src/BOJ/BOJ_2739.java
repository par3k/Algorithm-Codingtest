package BOJ;

import java.util.Scanner;

public class BOJ_2739 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i< 10; i++){
            System.out.println(String.format("%d * %d = %d", n, i, n * i));
        }
    }
}
