package BOJ;

import java.util.Scanner;

public class BOJ_1110 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int ans = 0;
        int tmp = x;

        while (true){
            int a = tmp / 10;
            int b = tmp % 10;
            if (a + b < 10){
                tmp = b * 10 + a + b;
            } else {
                tmp = b * 10 + (a + b) % 10;
            }
            ans ++;
            if (tmp == x){
                break;
            }
        }
        System.out.println(ans);
        sc.close();
    }
}
