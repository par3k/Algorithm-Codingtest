package BOJ;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_5397 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for(int j=0; j<t; j++) {
            char[] str = br.readLine().toCharArray();

            Stack<Character> a1 = new Stack<Character>();
            Stack<Character> a2 = new Stack<Character>();

            for(int i=0; i<str.length; i++) {
                switch(str[i]) {
                    case '<':
                        if(!a2.isEmpty()) {
                            a1.push(a2.pop());
                        }
                        break;
                    case '>':
                        if(!a1.isEmpty()) {
                            a2.push(a1.pop());
                        }
                        break;
                    case '-':
                        if(!a2.isEmpty()) {
                            a2.pop();
                        }
                        break;
                    default:
                        if(str[i] != '<' && str[i] != '>' && str[i] != '-') {
                            a2.push(str[i]);
                        }
                        break;
                }
            }

            while(!a1.isEmpty()) {
                a2.push(a1.pop());
            }

            StringBuilder sb = new StringBuilder();

            for(int i=0; i<a2.size(); i++) {
                sb.append(a2.elementAt(i));
            }

            System.out.println(sb);

        }
    }
}