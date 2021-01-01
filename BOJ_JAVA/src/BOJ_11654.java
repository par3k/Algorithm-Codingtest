import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11654 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char Ascii = br.readLine().charAt(0);
        int ans = (int)Ascii;
        System.out.println(ans);
    }
}