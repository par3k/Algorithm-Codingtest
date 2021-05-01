# 다음 순열
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))

x = 0

for i in range(n - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        x = i - 1
        break

for i in range(n - 1, 0, -1):
    if arr[x] < arr[i]:
        arr[x], arr[i] = arr[i], arr[x]
        arr = arr[:x + 1] + sorted(arr[x + 1:])
        print(*arr)
        exit()

print(-1)