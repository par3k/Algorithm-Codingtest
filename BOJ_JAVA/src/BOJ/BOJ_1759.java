package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1759 {
    private static int L;
    private static int C;
    private static char[] srcArr;
    private static char[] resArr;

    private static final char[] mo = { 'a', 'e', 'i', 'o', 'u'};
    private static final char[] ja = {
            'b', 'c', 'd', 'f', 'g',
            'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's',
            't', 'v', 'w', 'x', 'y',
            'z'};
    private static StringBuilder sb = new StringBuilder();
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    private static boolean contains(char[] obj1, char[] obj2, int cnt){
        int res = 0;
        for(int i = 0; i < obj1.length; i++){
            for(int j = 0 ; j < obj2.length; j++){
                if(obj1[i] == obj2[j]){
                    if(++res == cnt )   return true;
                }
            }
        }
        return false;
    }

    private static void f(int idx, int idxStart){
        if(idx == L){
            if(contains(mo, resArr, 1) && contains(ja, resArr, 2))
                sb.append(resArr).append("\n");
            return ;
        }

        for(int i = idxStart ; i < C ; i++){
            resArr[idx] = srcArr[i];
            f(idx + 1, i + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        srcArr = new char[C];
        resArr = new char[L];

        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < C ; i++ ){
            srcArr[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(srcArr);
        f(0, 0);
        System.out.println(sb);
    }
}