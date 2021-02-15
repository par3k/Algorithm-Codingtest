# 공유기 설치
import sys
input = lambda : sys.stdin.readline().rstrip()

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

start = 0
end = max(arr)


while start <= end:
    cnt = 1
    value = arr[0]
    mid = (start + end) // 2

    for i in range(n):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid -1


print(ans)