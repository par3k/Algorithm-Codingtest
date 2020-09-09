# 가장 긴 바이토닉 부분 수열

import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n
ans = [0] * n

def up_side(n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                dp1[j] = max(dp1[i] + 1, dp1[j])
    return dp1

def down_side(n):
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:
                dp2[j] = max(dp2[i] + 1, dp2[j])
    return dp2

up_side(n)
down_side(n)

for i in range(n):
    ans[i] = dp1[i] + dp2[i] -1


print(max(ans))
