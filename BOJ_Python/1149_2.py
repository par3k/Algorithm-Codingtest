import sys
input = lambda :sys.stdin.readline().rstrip()
n = int(input())
arr = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + a
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + b
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + c

print(min(arr[n][0], arr[n][1], arr[n][2]))