# 로프

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
print(arr)
ans = list()

for i in range(n):
    ans.append(arr[i] * (i+1))

print(max(ans))