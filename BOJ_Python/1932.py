# 정수 삼각형
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
best = [[-1 for _ in range(n)] for _ in range(n)]

ans = 0
best[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        best[i][j] = arr[i][j] + max(best[i-1][j-1], best[i-1][j])

print(max(best[n-1]))