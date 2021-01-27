package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class myPoint {

    int x, y, z;
    myPoint(int z, int y, int x){
        this.z = z;
        this.y = y;
        this.x = x;
    }
}

public class BOJ_7569 {
    static int w, h, channel;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        channel = Integer.parseInt(st.nextToken());

        int map[][][] = new int[channel][h][w];
        boolean visited[][][] = new boolean[channel][h][w];
        Queue<myPoint> q = new LinkedList<myPoint>();
        for (int i = 0; i < channel; i++) {
            for (int j = 0; j < h; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < w; k++) {
                    map[i][j][k] = Integer.parseInt(st.nextToken());
                    if (map[i][j][k] == 1) {
                        visited[i][j][k] = true;
                        q.offer(new myPoint(i, j, k));
                        map[i][j][k] = 0;
                    }
                }
            }
        }
        int dz[] = {-1,1,0,0,0,0};
        int dy[] = {0,0,1,-1,0,0};
        int dx[] = {0,0,0,0,1,-1};

        int ans = 0;
        while (!q.isEmpty()) {
            int z = q.peek().z;
            int y = q.peek().y;
            int x = q.peek().x;
            q.poll();
            for (int i = 0; i < 6; i++){
                int nz = z + dz[i];
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (condition(nz, ny, nx) && !visited[nz][ny][nx] && map[nz][ny][nx] == 0){
                    map[nz][ny][nx] = map[z][y][x] + 1;
                    visited[nz][ny][nx] = true;
                    q.offer(new myPoint(nz, ny, nx));
                    ans = ans <= map[nz][ny][nx] ? map[nz][ny][nx] : ans;
                }
            }
        }
        if (!checkZero(map, visited)) ans = -1;
        System.out.println(ans);
    }

    static boolean condition(int z, int y, int x) {
        if (z >= 0 && y >= 0 && x >= 0 && z < channel && y < h && x <w)
            return true;
        else
            return false;
    }

    static boolean checkZero(int[][][] map, boolean[][][] visited) {
        for (int z = 0; z<channel; z++)
            for (int y = 0; y<h; y++)
                for (int x = 0; x<w; x++)
                    if (!visited[z][y][x] && map[z][y][x] == 0)
                        return false;
        return true;
    }
}