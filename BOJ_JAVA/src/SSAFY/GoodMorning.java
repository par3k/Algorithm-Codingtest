package SSAFY;

import java.util.Arrays;
import java.util.Scanner;

public class GoodMorning {


   static int N,R; //N:입력받을 데이터 수(전체데이터) R:선택할 데이터 수
   static int[] input,res; //input:입력데이터저장    res:결과데이터저장
   static boolean[] visited; //visited: 방문체크용 배열
	
   public static void main(String[] args) {
	  Scanner sc = new Scanner(System.in);
  	  N = sc.nextInt();
	  R = sc.nextInt();
	  input = new int[N];
	  res = new int[R];
	  visited = new boolean[N];
	
	  for (int i = 0; i < N; i++) {
		input[i] = sc.nextInt();
	  }
//      1. input배열에서 R개의 수를 뽑아서 만들 수 있는 순열을 모두 출력하시오.
      System.out.println("----- 순열 -----");
      makePermutation(0);
      
//      2. input배열에서 R개의 수를 뽑아서 만들 수 있는 조합을 모두 출력하시오.
      System.out.println("----- 조합 -----");
      makeCombination(0,0);
      
	  visited = new boolean[N];      
//      3. input배열로 구성할 수 있는 모든 부분집합을 출력하시오.
      System.out.println("----- 부분집합 -----");
      makeSubset(0);
      
      sc.close();
   }//main
   
   private static void makePermutation(int cnt) {
   	if (cnt == R) {
		System.out.println(Arrays.toString(res));
		return;
	}

   	for (int i = 0; i < N; i++) {
   		if (visited[i]) continue;
   		res[cnt] = input[i];
   		visited[i] = true;
   		makePermutation(cnt + 1);
   		visited[i] = false;
	}
   }
	
   private static void makeCombination(int cnt,int start) {
   	if (cnt == R) {
		System.out.println(Arrays.toString(res));
		return;
	}

   	for (int i = start; i < N; i++) {
   		res[cnt] = input[i];
   		makeCombination(cnt + 1, i + 1);
	}
   }
	
   private static void makeSubset(int cnt) {
   	if (cnt == N) {
		System.out.print("[");
		for (int i = 0; i < N; ++i) {
			if (visited[i]) System.out.print(input[i] + " ");
		}
		System.out.println("]");
		return;
	}
   	visited[cnt] = true;
   	makeSubset(cnt + 1);
   	visited[cnt] = false;
   	makeSubset(cnt + 1);
//		if(cnt==N) {
//			System.out.print("[");
//			for(int i=0; i<N; ++i) {
//				if(visited[i])
//				  System.out.print(input[i]+" ");
//			}
//			System.out.println("]");
//			return;
//		}
//		visited[cnt] = true;
//		makeSubset(cnt+1);
//		visited[cnt] = false;
//		makeSubset(cnt+1);
   }
   
}