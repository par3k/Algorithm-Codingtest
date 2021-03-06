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
        Deque<Integer> su_deck = new ArrayDeque<>();

        for (int tc = 0; tc < n; tc++) {
            st = new StringTokenizer(br.readLine());
            do_deck.add(Integer.parseInt(st.nextToken()));
            su_deck.add(Integer.parseInt(st.nextToken()));
        }


        Deque<Integer> do_ground = new ArrayDeque<>();
        Deque<Integer> su_ground = new ArrayDeque<>();

        int l = 0;
        int r = 0;

        boolean turn = false;

        while (m-- > 0) {
            if (!turn) {
                l = do_deck.pollLast();
                do_ground.add(l);
            } else {
                r = su_deck.pollLast();
                su_ground.add(r);
            }
            turn = !turn;

            if (do_deck.isEmpty() || su_deck.isEmpty()) break;

            if (l == 5 || r == 5) { // do가 종칠때
                while (!su_ground.isEmpty()) {
                    do_deck.addFirst(su_ground.pollFirst());
                }
                while (!do_ground.isEmpty()) {
                    do_deck.addFirst(do_ground.pollFirst());
                }
                l = 0;
                r = 0;
            }

            if ((!do_ground.isEmpty() && l + r == 5) || (!su_ground.isEmpty() && l + r == 5)) { // su가 종칠때
                while (!do_ground.isEmpty()){
                    su_deck.addFirst(do_ground.pollFirst());
                }
                while (!su_ground.isEmpty()) {
                    su_deck.addFirst(su_ground.pollFirst());
                }
                l = 0;
                r = 0;
            }
        }

        if (do_deck.size() > su_deck.size()) {
            System.out.println("do");
        } else if (do_deck.size() < su_deck.size()) {
            System.out.println("su");
        } else {
            System.out.println("dosu");
        }

        br.close();
    }
}