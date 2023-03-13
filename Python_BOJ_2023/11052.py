# 카드 구매하기

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i - j] + arr[j - 1], dp[i])

print(max(dp))