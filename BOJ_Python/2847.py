# 게임을 만든 동준이
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0

for i in range(n-1, 0, -1):
    if arr[i] <= arr[i-1]:
        ans += arr[i-1] - arr[i] + 1
        arr[i-1] = arr[i] - 1

print(ans)



