package SWEA;

public class Baby_Gin {
    private static int[] arr = {2, 3, 7, 7, 1, 7};
    private static boolean check;

    private static boolean is_Run(int start, int end) {
        if (Math.abs(arr[start] - arr[start + 1]) == 1 && Math.abs(arr[start] - arr[start + 2]) == 2) {
            return true;
        }
        return false;
    }

    private static boolean is_Triplet (int start) {
        if(arr[start] == arr[start + 1] && arr[start] == arr[start + 2]) {
            return true;
        }
        return false;
    }

    private static void swap(int idx1, int idx2) {
        int tmp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = tmp;
    }

    private static void recursive(int cnt, int size) {
        if(cnt == size && !check) {
            if ((is_Run(0, 2) && is_Triplet(3)) || (is_Run(3, 5) && is_Triplet(0))) {
                check = true;
                for (int i = 0; i < 6; i++) {
                    System.out.print(arr[i] + " ");
                }
                System.out.println();
            }
        } else {
            for (int i = cnt; i < 6; i++) {
                swap(cnt, i);
                recursive(cnt + 1, size);
                swap(cnt, i);
            }
        }
    }

    private static boolean is_Babygin (int[] arr) {
        recursive(0, arr.length);
        return check;
    }

    public static void main(String[] args) {
        System.out.println(is_Babygin(arr));
    }
}
