package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_1289 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char[] input = st.nextToken().toCharArray();
            char[] mem = new char[input.length];

            int ans = 0;

            for (int i = 0 ; i < input.length; i++) { // 초기화 상태
                mem[i] = '0';
            }

            for (int i = 0 ; i < input.length; i++) { // 받은 값의 길이로 돌면서
                if (input[i] != mem[i]) { // 복구하고자 하는 값과 0으로 초기화된 값이 다르면
                    char tmpN = input[i]; // tmpN에 그 값을 임시로 저장

                    for (int j = i; j < input.length; j++) {
                        mem[j] = tmpN; // 메모리에 그 값을 덮어 씌운다
                    }
                    ans++; // 카운트 + 1
                }
            }
            System.out.println("#" + (tc+1) + " " + ans);
        }
    }
}

