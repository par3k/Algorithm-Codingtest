import sys
input = lambda :sys.stdin.readline().rstrip()

n, k = map(int, input().split())

weight, value = list(), list()
weight.append(0)
value.append(0)

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
        if weight[i] <= j:
            dp[i][j] = max(dp[i - 1][j], value[i] + dp[i - 1][j - weight[i]])


print(dp[n][k])