# LCS 2
import sys
input = lambda : sys.stdin.readline().rstrip()

arr = list(input())
arr2 = list(input())

dp = [[0] * (len(arr2) + 1) for _ in range(len(arr) + 1)]
strdp = [[""] * (len(arr2) + 1) for _ in range(len(arr) + 1)]

for i in range(1, len(arr) + 1):
    for j in range(1, len(arr2) + 1):
        if arr[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            strdp[i][j] = strdp[i - 1][j - 1] + arr[i - 1]
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                strdp[i][j] = strdp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
                strdp[i][j] = strdp[i][j - 1]

print(dp[len(arr)][len(arr2)])
print(strdp[len(arr)][len(arr2)])