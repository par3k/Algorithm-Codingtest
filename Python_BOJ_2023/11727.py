# 2xN 타일링 2

n = int(input())

dp = [0] * 1001
dp[0], dp[1], dp[2] = 1, 3, 5

for i in range(3, n + 1):
    dp[i] = ((dp[i - 2] * 2 + dp[i - 1]) % 10007)

print(dp[n - 1])