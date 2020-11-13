import java.util.Scanner;

public class Codeup_6 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String data[] = a.split("[.]");

        int year = Integer.parseInt(data[0]);
        int month = Integer.parseInt(data[1]);
        int day = Integer.parseInt(data[2]);

        System.out.print(String.format("%04d.%02d.%02d", year,month,day));
    }
}
