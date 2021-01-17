# 스카이라인 쉬운거 - 못 품
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [0] * (n+1)
ans = 0

for i in range(n-1):
    while len(tmp) != 0 and arr[i][1] > arr[i+1][1]:
        tmp.pop()
        ans += 1
    if len(tmp) != 0 and arr[i][1] > arr[i+1][1]: continue
    tmp[i] = arr[i][1]

print(ans)