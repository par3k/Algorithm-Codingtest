package CODEUP;

import java.util.Scanner;

public class Codeup_7 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        a = a.replaceAll("-", "");

        System.out.print(a);
    }
}
