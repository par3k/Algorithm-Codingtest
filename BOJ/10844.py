# 쉬운 계단 수
import sys
n = int(sys.stdin.readline().rstrip())

dp = [[-1] * 10 for _ in range(n)]

dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for level in range(1, n):
    for idx in range(0, 10):
        if idx == 0:
            dp[level][idx] = dp[level-1][1]
        elif idx == 9:
            dp[level][idx] = dp[level-1][8]
        else:
            dp[level][idx] = dp[level-1][idx-1] + dp[level-1][idx+1]

print(sum(dp[n-1][1:]) % 1000000000)