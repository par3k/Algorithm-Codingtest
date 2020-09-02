# 가장 긴 증가하는 부분 수열2
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)

    else:
        dp[k] = i

print(len(dp))