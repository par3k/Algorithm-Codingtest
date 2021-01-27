package BOJ;

import java.io.*;
import java.math.BigInteger;


public class BOJ_10757 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        System.out.println(new BigInteger(arr[0]).add(new BigInteger(arr[1])));
    }
}
