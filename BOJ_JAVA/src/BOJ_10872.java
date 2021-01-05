import java.io.*;

public class BOJ_10872 {
    public static int recursive (int i) {
        if (i <= 1) {
            return 1;
        } else {
            return i * recursive(i - 1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(recursive(n));

    }
}
