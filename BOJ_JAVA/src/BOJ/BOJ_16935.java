package BOJ;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_16935 {
    static int n, m, r;
    static int[] dx = { 0, 1, 0, -1 };
    static int[] dy = { 1, 0, -1, 0 };
    static int[][] arr;
    static List<Integer> List;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static void one() {
        for (int i = 1; i <= arr.length / 2; i++) {
            int[] temp = arr[i];
            arr[i] = arr[arr.length - i];
            arr[arr.length - i] = temp;
        }

    }

    static void two() {
        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j <= arr[i].length / 2; j++) {
                int temp = arr[i][j];
                arr[i][j] = arr[i][arr[i].length - j];
                arr[i][arr[i].length - j] = temp;
            }
        }
    }

    static void three() {
        int[][] temp = copy(arr);
        n = temp.length -1;
        m = temp[0].length - 1;
        arr = new int[m+1][n+1];
        for (int i = 1, j = n; j >= 1; j--, i++) {
            for (int k = 1; k <= m; k++) {
                arr[k][j] = temp[i][k];
            }
        }
    }

    static void four() {
        int[][] temp = copy(arr);
        n = temp.length -1;
        m = temp[0].length - 1;
        arr = new int[m+1][n+1];
        for (int i = 1, j = 1; j <= n; j++, i++) {
            for (int k = 1; k <= m; k++) {
                arr[k][j] = temp[i][m - k + 1];
            }
        }
    }

    static void five() {
        int[][] temp = copy(arr);
        n = temp.length-1;
        m = temp[0].length-1;
        // 1 -> 2
        for (int j = 1; j <= n / 2; j++) {
            for (int i = 1; i <= m / 2; i++) {
                arr[j][m / 2 + i] = temp[j][i];
            }
        }
        // 3 -> 4
        for (int j = n / 2 + 1; j <= n; j++) {
            for (int i = m / 2 + 1; i <= m; i++) {
                arr[j][i - m / 2] = temp[j][i];
            }
        }

        // 2 -> 3
        for (int j = 1; j <= n / 2; j++) {
            for (int i = m / 2 + 1; i <= m; i++) {
                arr[j + n / 2][i] = temp[j][i];
            }
        }

        // 4 -> 1
        for (int j = n / 2 + 1; j <= n; j++) {
            for (int i = 1; i <= m / 2; i++) {
                arr[j - n / 2][i] = temp[j][i];
            }
        }
    }

    static void six() {
        int[][] temp = copy(arr);
        n = temp.length-1;
        m = temp[0].length-1;
        // 1 -> 4
        for (int j = 1; j <= n / 2; j++) {
            for (int i = 1; i <= m / 2; i++) {
                arr[j + n / 2][i] = temp[j][i];
            }
        }
        // 4 -> 3
        for (int j = n / 2; j <= n; j++) {
            for (int i = 1; i <= m / 2; i++) {
                arr[j][m / 2 + i] = temp[j][i];
            }
        }
        // 3 -> 2
        for (int j = n / 2 + 1; j <= n; j++) {
            for (int i = m / 2 + 1; i <= m; i++) {
                arr[j - n / 2][i] = temp[j][i];
            }
        }
        // 2 -> 1
        for (int j = 1; j <= n / 2; j++) {
            for (int i = m / 2 + 1; i <= m; i++) {
                arr[j][i - m / 2] = temp[j][i];
            }
        }
    }

    static int[][] copy(int[][] arr) {
        int[][] temp = new int[arr.length][arr[0].length];
        for (int i = 1; i <= arr.length-1; i++) {
            for (int j = 1; j <= arr[0].length-1; j++) {
                temp[i][j] = arr[i][j];
            }
        }
        return temp;
    }

    static void print(int arr[][]) throws IOException {
        for (int i = 1; i < arr.length; i++) {
            for (int j = 1; j < arr[i].length; j++) {
                bw.append(arr[i][j] + " ");
            }
            bw.newLine();
        }
    }

    static int stoi(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = stoi(st.nextToken());
        m = stoi(st.nextToken());
        r = stoi(st.nextToken());

        arr = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                arr[i][j] = stoi(st.nextToken());
            }
        }

        List = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < r; i++) {
            List.add(stoi(st.nextToken()));
        }

        for (int i : List) {
            switch (i) {
                case 1: one(); break;
                case 2: two(); break;
                case 3: three(); break;
                case 4: four(); break;
                case 5: five(); break;
                case 6: six(); break;
                default: break;
            }
        }

        print(arr);
        bw.flush();
        bw.close();
    }

}
