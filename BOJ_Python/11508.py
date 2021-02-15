# 2+1 세일
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

ans = 0
for i in range(n):
    if i % 3 != 2:
        ans += arr[i]

print(ans)