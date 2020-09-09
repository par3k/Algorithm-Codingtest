# 가장 긴 증가하는 부분 수열

import sys
from bisect import bisect_left

A = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = []

for i in arr:
    bin_res = bisect_left(dp, i)

    if len(dp) <= bin_res:
        dp.append(i)

    else:
        dp[bin_res] = i

print(len(dp))