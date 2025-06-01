import java.util.Scanner;

public class Solve_9498 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();

        String answer = solve(score);
        System.out.println(answer);
    }

    public static String solve(int score) {
        String result = "F";
        if (score >= 90 && score <= 100) {
            return "A";
        } else if (score >= 80 && score < 90) {
            return "B";
        } else if (score >= 70 && score < 80) {
            return "C";
        } else if (score >= 60 && score < 70) {
            return "D";
        }
        return result;
    }
}
