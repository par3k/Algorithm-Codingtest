# 피보나치 수
n = int(input())

dp = [0] * 1000
def fibo(n):
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[i]

ans = fibo(n)
print(ans, n - 2)