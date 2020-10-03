# 행복 유치원
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, n):
    a[i-1] = a[i] - a[i-1]

a.sort()

for i in range(n-k):
    ans += a[i]

print(ans)