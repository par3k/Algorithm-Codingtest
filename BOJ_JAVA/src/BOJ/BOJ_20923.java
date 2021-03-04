package BOJ;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class BOJ_20923 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Deque<Integer> do_deck = new ArrayDeque<>();
        Deque<Integer> su_deck  = new ArrayDeque<>();
        for (int tc = 0; tc < n; tc++) {
            st = new StringTokenizer(br.readLine());
            do_deck.add(Integer.parseInt(st.nextToken()));
            su_deck.add(Integer.parseInt(st.nextToken()));
        }

        Deque<Integer> do_ground = new ArrayDeque<>();
        Deque<Integer> su_ground = new ArrayDeque<>();
        int sum_is_five = 0;

        while (true) {
            if (m == 0) {
                if (do_deck.size() == su_deck.size()) {
                    System.out.println("dosu");
                    break;
                } else if (do_deck.size() > su_deck.size()) {
                    System.out.println("do");
                    break;
                } else if (do_deck.size() < su_deck.size()) {
                    System.out.println("su");
                    break;
                }
            }

            int tmp1 = do_deck.pollLast();
            m--;
            if (do_deck.isEmpty()) {
                System.out.println("su");
                break;
            }
            sum_is_five += tmp1;
            do_ground.add(tmp1);
            if (sum_is_five == 5) {
                // su가 종을 침
                while (!do_ground.isEmpty()) {
                    su_deck.addFirst(do_ground.pollFirst());
                }
                sum_is_five = 0;
            } else if (tmp1 == 5) {
                // do가 종을 침
                while (!su_ground.isEmpty()) {
                    do_deck.addFirst(su_ground.pollFirst());
                }
                sum_is_five = 0;
            }

            int tmp2 = su_deck.pollLast();
            m--;
            if (su_deck.isEmpty()) {
                System.out.println("do");
                break;
            }
            sum_is_five += tmp2;
            su_ground.add(tmp2);
            if (sum_is_five == 5) {
                // su가 이김
                while (!do_ground.isEmpty()) {
                    su_deck.addFirst(do_ground.pollFirst());
                }
                sum_is_five = 0;
            } else if (tmp2 == 5) {
                // do가 이김
                while (!su_ground.isEmpty()) {
                    do_deck.addFirst(su_ground.pollFirst());
                }
                sum_is_five = 0;
            }


        }

        br.close();
    }
}

