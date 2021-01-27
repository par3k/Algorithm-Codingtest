package BOJ;

import java.util.Scanner;

public class BOJ_4740 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true){
            StringBuilder sb = new StringBuilder();
            String s = sc.nextLine();
            if (s.equals("***")) break;

            for (int i = 0; i < s.length(); i++) {
                sb.append(s.charAt(s.length() - i - 1));
            }
            System.out.print(sb.toString() + "\n");
        }
        sc.close();
    }
}
