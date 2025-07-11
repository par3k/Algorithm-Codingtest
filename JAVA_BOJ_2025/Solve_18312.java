import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_18312 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        String target = input[1];
        int result = 0;

        for (int i = 0; i <= N; i++) { // 시간
            for (int j = 0; j <= 59; j++) { // 분
                for (int k = 0; k <= 59; k++) { // 초
                    String time = String.format("%02d:%02d:%02d", i, j, k);
                    if (time.contains(target)) {
                        result++;
                    }
                }
            }
        }
        System.out.println(result);
        br.close();
    }
}
