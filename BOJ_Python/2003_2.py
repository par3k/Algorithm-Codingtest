# 수들의 합 2
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans, interval_sum, end = 0, 0, 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1
    if interval_sum == m: ans += 1
    interval_sum -= arr[start]

print(ans)