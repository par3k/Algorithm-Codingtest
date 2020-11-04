# LCS - Longest Common Subsequence
import sys
input = lambda : sys.stdin.readline().rstrip()

a = ' '+input()
b = ' '+input()

dp = [[0] * len(b) for _ in range(len(a))]
ans = 0

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    ans = max(ans, max(dp[i]))

print(ans)