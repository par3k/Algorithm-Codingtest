# K번째 수
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in range(1, n+1):
        tmp += min(mid // i, n)

    if tmp >= k:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)