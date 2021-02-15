# 스네이크버드
import sys
input = lambda : sys.stdin.readline().rstrip()

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n):
    if arr[i] <= l:
        l += 1

print(l)