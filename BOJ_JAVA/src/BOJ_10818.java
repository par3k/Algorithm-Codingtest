import java.io.*;
import java.util.StringTokenizer;

public class BOJ_10818 {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        String[] mm = br.readLine().split(" ");

        int min = 1000001;
        int max = -1000001;

        for (int i = 0; i < n; i++) {
            if (min > Integer.parseInt(mm[i])){
                min = Integer.parseInt(mm[i]);
            }
            if (max < Integer.parseInt(mm[i])){
                max = Integer.parseInt(mm[i]);
            }
        }
        bw.write(Integer.toString(min) + " " + Integer.toString(max));
        bw.close();
        br.close();

    }
}
