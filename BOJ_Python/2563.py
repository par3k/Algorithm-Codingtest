# 색종이
import sys
input = lambda : sys.stdin.readline().rstrip()

graph = [[0] * 100 for _ in range(100)]
ans = 0

n = int(input())
for i in range(n):
    x, y = map(int,input().split())

    for a in range(x, x + 10):
        for b in range(y, y + 10):
            if graph[a][b] == 1: continue
            graph[a][b] = 1
            ans += 1

print(ans)