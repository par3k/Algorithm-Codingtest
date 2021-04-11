package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2941 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String text = br.readLine();

        int n = 0;

        for(int i=0; i<text.length();i++) {
            if(i<text.length()-1&&text.charAt(i)=='c'&&text.charAt(i+1)=='=') {
                i++;
            }
            else if(i<text.length()-1&&text.charAt(i)=='c'&&text.charAt(i+1)=='-') {
                i++;
            }
            else if(i<text.length()-2&&text.charAt(i)=='d'&&text.charAt(i+1)=='z'&&text.charAt(i+2)=='=') {
                i+=2;
            }
            else if(i<text.length()-1&&text.charAt(i)=='d'&&text.charAt(i+1)=='-') {
                i++;
            }
            else if(i<text.length()-1&&text.charAt(i)=='l'&&text.charAt(i+1)=='j') {
                i++;
            }
            else if(i<text.length()-1&&text.charAt(i)=='n'&&text.charAt(i+1)=='j') {
                i++;
            }
            else if(i<text.length()-1&&text.charAt(i)=='s'&&text.charAt(i+1)=='=') {
                i++;
            }
            else if(i<text.length()-1&&text.charAt(i)=='z'&&text.charAt(i+1)=='=') {
                i++;
            }
            n++;
        }
        System.out.println(n);
    }
}
