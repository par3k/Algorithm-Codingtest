# 병사 배치하기
from sys import stdin

input = lambda: stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

