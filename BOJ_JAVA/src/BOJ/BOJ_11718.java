package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_11718 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> lst = new ArrayList<String>();
        String line;
        while ((line = br.readLine()) != null) {
            lst.add(line);
        }
        for (int i = 0; i < lst.size(); i++) {
            if ( i == lst.size()) {
                System.out.println(lst.get(i));
            }
            else {
                System.out.println(lst.get(i));
            }
        }
    }
}
