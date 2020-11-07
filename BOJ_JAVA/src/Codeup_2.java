import java.util.Scanner;

public class Codeup_2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Float number = scanner.nextFloat();
        String s3 = String.format("%.6f", number);
        System.out.println(s3);
    }
}
