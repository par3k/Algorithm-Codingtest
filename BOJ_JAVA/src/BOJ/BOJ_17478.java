package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_17478 {
    static String[] StringArr;
    static String underLine = "";

    private static void recursive(int n) {
        String ul = underLine;

        if (n == 0) {
            System.out.println(ul + StringArr[0]);
            System.out.println(ul + StringArr[4]);
            System.out.println(ul + StringArr[5]);
            return;
        }

        for (int i = 0; i < 4; i++) {
            System.out.println(ul + StringArr[i]);
        }

        underLine += "____";
        recursive(n - 1);
        System.out.println(ul + StringArr[5]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringArr = new String[6];
        for (int i = 0; i < StringArr.length; i++) {
            StringArr[i] = " ";
        }

        System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        StringArr[0] = "\"재귀함수가 뭔가요?\"";
        StringArr[1] = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
        StringArr[2] = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
        StringArr[3] = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
        StringArr[4] = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
        StringArr[5] = "라고 답변하였지.";

        recursive(T);

        br.close();
    }
}
