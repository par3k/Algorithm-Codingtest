# 점화식

dp = [0] * 36
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

n = int(input())

if n > 3:
    for i in range(4, 36):
        for j in range(i):
            dp[i] += (dp[j] * dp[i - 1 - j])
            
            if j == n:
                break

print(dp[n])