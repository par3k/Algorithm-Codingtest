# 2xn 타일링
import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[-1])