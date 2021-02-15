# 사탕
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    j, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(len(arr)):
        arr[i] = arr[i][0] * arr[i][1]
    arr.sort(reverse=True)

    ans = 0
    for i in arr:
        j -= i
        ans += 1
        if j <= 0: break
    print(ans)