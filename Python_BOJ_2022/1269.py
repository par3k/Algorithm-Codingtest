# 대칭 차집합
import sys
input = lambda : sys.stdin.readline()

n, m = map(int, input().split())
arr_1 = set(map(int, input().split()))
arr_2 = set(map(int, input().split()))
ans = len(arr_1 ^ arr_2)

print(ans)