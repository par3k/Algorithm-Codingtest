# 센서
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
tmp = [0] * n
arr.sort()

if n <= k:
    ans = 0
else:
    for i in range(n-1):
        tmp[i] = arr[i+1] - arr[i]
    tmp.sort()

    for _ in range(k-1):
        tmp.pop(len(tmp)-1)
    ans = sum(tmp)

print(ans)