package season_2025;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solve_1672 {
    static char[][] rules = {
            {'A', 'C', 'A', 'G'},
            {'C', 'G', 'T', 'A'},
            {'A', 'T', 'C', 'G'},
            {'G', 'A', 'G', 'T'}
    };

    static int getIndex (char c) {
        switch (c) {
            case 'A': return 0;
            case 'G': return 1;
            case 'C': return 2;
            case 'T': return 3;
            default: return -1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int length = Integer.parseInt(br.readLine());
        String dna = br.readLine();

        char result = dna.charAt(length - 1);
        for (int i = length - 2; i >= 0; i--) {
            char left = dna.charAt(i);
            int idx1 = getIndex(left);
            int idx2 = getIndex(result);
            result = rules[idx1][idx2];
        }

        System.out.println(result);
        br.close();
    }
}
