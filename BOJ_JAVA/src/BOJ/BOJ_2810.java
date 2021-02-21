package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class BOJ_2810 {
    static boolean[] cupHolders;
    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        String line = br.readLine();
// True : 컵홀더 사용중 또는 컵홀더 사용 불가능.  False : 컵홀더 미사용
        cupHolders = new boolean[n + 1];
        int count = 0;
        boolean checked = false;	// 커플석 한 쌍 중 커플석 시작한 경우 True
// 컵홀더 개수 세기

        for(int i = 0; i < n; i++) {
            char ch = line.charAt(i);
// 커플석 판단
            if(ch == 'L') {
                if(!checked) {
                    checked = true;
// 커플석 오른쪽 컵홀더 제거
                    cupHolders[i + 1] = true;
                }
                else {
                    checked = false;
                }
            }
// 컵홀더에 컵두기
            if(!cupHolders[i]) { // 왼쪽
                cupHolders[i] = true;
                count++;
            }
            else if(!cupHolders[i + 1]) { // 오른쪽
                cupHolders[i + 1] = true;
                count++;
            }
            else {	// 양쪽 다 컵이 놓여져있으면
            }
        }
        System.out.println(count);
    }
}

