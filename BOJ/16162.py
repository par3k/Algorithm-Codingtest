# 가희와 3단 고음
import sys
input = lambda : sys.stdin.readline().rstrip()

n, a, d = map(int, input().split())
arr = list(map(int, input().split()))
ans, now = 0, a

for i in range(n):
    if arr[i] == now:
        ans += 1
        now += d

print(ans)