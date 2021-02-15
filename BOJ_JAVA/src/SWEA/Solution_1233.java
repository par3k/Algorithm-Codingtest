package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution_1233 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int tc = 1; tc <= 10; tc++) {
            int Size = Integer.parseInt(br.readLine());
            inOrder[] v = new inOrder[Size + 1];

            for (int i = 0; i <= Size; i++) v[i] = new inOrder();
            for (int i = 1; i <= Size; i++) {
               String s = br.readLine();
               int len = s.split(" ").length;

                v[i].num = Integer.parseInt(s.split(" ")[0]); // 안쓰는 데이터
                v[i].op = s.split(" ")[1];
                if (len == 4) {
                    v[i].lNode = Integer.parseInt(s.split(" ")[2]); // 이 문제에서는 안씀
                    v[i].rNode = Integer.parseInt(s.split(" ")[3]); // 자식노드를 이용하는 문제 아니기에
                } else if (len == 3) {
                    v[i].lNode = Integer.parseInt(s.split(" ")[2]);
                }
            }

            boolean flag = true;
            for (int i = 1; i<= Size; i++) {
                if ((v[i].lNode == -1) || v[i].rNode == -1) {
                    if ((v[i].op).equals("+") || (v[i].op).equals("-") || (v[i].op).equals("*") || (v[i].op).equals("/")) {
                        flag = false;
                        System.out.println("#" + tc + " 0");
                        break;
                    }
                }
            }
            if(flag) System.out.println("#" + tc + " 1");
        }
    }
}

class inOrder {
    int num;
    String op;
    int lNode = -1;
    int rNode = -1;
}
