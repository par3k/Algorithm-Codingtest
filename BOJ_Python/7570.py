# 줄 세우기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

dp =[0] * (int(1e6) + 1)
ans = 0

for i in arr:
    dp[i] = dp[i - 1] + 1
    ans = max(ans, dp[i])

print(n - ans)