package BOJ;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class BOJ_1931 {
    private static int cnt;
    static class MeetingRoom implements Comparable<MeetingRoom> {
        int no, start, end;

        public MeetingRoom(int no, int start, int end) {
            super();
            this.no = no;
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(MeetingRoom o) {
            int diff = this.end - o.end;
            return diff != 0 ? diff : this.start - o.start;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        MeetingRoom[] room  = new MeetingRoom[N];

        for (int i = 0; i < N; i++) {
            room[i] = new MeetingRoom(i + 1, sc.nextInt(), sc.nextInt());
        }
        List<MeetingRoom> list = getSchedule(room);
        System.out.println(cnt);
    }

    public static List<MeetingRoom> getSchedule(MeetingRoom[] room) {
        cnt = 1;
        ArrayList<MeetingRoom> list = new ArrayList<>();
        Arrays.sort(room);
        list.add(room[0]);

        for (int i = 1, size = room.length; i < size; i++) {
            if (list.get(list.size() - 1).end <= room[i].start) {
                list.add(room[i]);
                cnt++;
            }
        }
        return list;
    }
}
