# 랜선 자르기
import sys
input = lambda : sys.stdin.readline().rstrip()

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for x in arr:
        cnt += x // mid

    if cnt >= n:
        start = mid + 1
        ans = mid
    else:
        end = mid -1


print(ans)