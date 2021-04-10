package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_20055 {
    private static int N, K, broken;
    private static int[] arr;
    private static boolean[] robot;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N * 2];
        robot = new boolean[N * 2]; // 벨트에 로봇이 있는지 없는지

        st = new StringTokenizer(br.readLine());
        broken = 0; // 벨트 고장 갯수

        for (int i = 0 ; i< N * 2; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] == 0) broken++;
        }

        int ans = 0;
        while (broken < K) {
            ans++;

            int tmp = arr[2 * N - 1]; // 컨베이어 벨트가 움직임
            for (int i = 2 * N - 1; i >= 1; i--) {
                robot[i] = robot[i - 1];
                arr[i] = arr[i- 1];
            }
            arr[0] = tmp;
            robot[0] = false;
            if (robot[N - 1]) robot[N - 1] = false; // 컨베이어 벨트로 로봇이 N에 이동했을때

            for (int i = N - 2; i >= 0; i--) {
                if (robot[i] && arr[i + 1] > 0 && !robot[i + 1]) { // 현재위치에 로봇이 있고, 다음칸이 0이 아니고, 로봇이 없다면
                    robot[i] = false;
                    robot[i + 1] = true; // 로봇 이동
                    arr[i + 1] -= 1; // 내구도 -1 해주기
                    if (arr[i + 1] == 0) broken++; // 현재 이동하고 나서의 자리 내구도 확인
                }
            }
            if (robot[N - 1]) robot[N - 1] = false; // 로봇 이동후 n에 도착했을 때 내려오므로 false

            if (arr[0] > 0 && !robot[0]) { // 로봇을 올림
                robot[0] = true;
                arr[0] -= 1;
                if (arr[0] == 0) broken++;
            }
        }
        System.out.println(ans);
        br.close();
    }
}
