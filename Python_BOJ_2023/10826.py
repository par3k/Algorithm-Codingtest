# 피보나치 수4

n = int(input())

dp = [0, 1]

if n > 1:
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(str(dp[n]))
else:
    print(str(dp[n]))