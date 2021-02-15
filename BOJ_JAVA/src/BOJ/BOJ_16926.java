package BOJ;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ_16926 {
    private static int N, M, R;
    private static int[] dx = {0, 1, 0, -1}; // 반시계방향 지정
    private static int[] dy = {1, 0, -1, 0};
    private static int[][] arr;

    private static void find(int s) {
        for (int i = 0 ; i < s; i ++) {
            int x = i; // 회전 할 횟수마다 기준이 되는 좌표를 잡는다.
            int y = i;
            int dir = 0; // 아래부터 이동
            int tmp = arr[x][y]; // 값 스왑할 때, (1) tmp = a 부분

            while (dir < 4) { // 반시계 방향으로 돌아보자
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (i <= nx && nx < N - i && i <= ny && ny < M - i) { // 범위 이내라면
                    arr[x][y] = arr[nx][ny]; // (2) a = b 부분
                    x = nx; // 기준이 되는 그 다음 좌표 지정
                    y = ny;
                } else { // 범위를 벗어난다면
                    dir++; // 방향을 바꿔준다.
                }
            }
            arr[i + 1][i] = tmp; // (3) b = tmp 부분
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        arr =  new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

// 사각형의 내부 사각형이 있다면 회전시키기 위해서
// 높이, 너비중 작은값으로 반 쪼개본다.
// 1 1
// 1 1 라면 1이 나올테고
//
// 1 1 1 1
// 1 1 1 1
// 1 1 1 1
// 1 1 1 1 면 2가 나올테니

        for (int i = 0 ; i < R; i++) {
            find(Math.min(N, M) / 2);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j< M; j++) {
                bw.write(arr[i][j] + " ");
            }
            bw.write('\n');
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
