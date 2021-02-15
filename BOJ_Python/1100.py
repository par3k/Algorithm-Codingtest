# 하얀 칸
import sys
input = lambda :sys.stdin.readline().rstrip()

graph = [list(input()) for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if graph[i][j] == 'F': ans += 1

        if i % 2 == 1 and j % 2 == 1:
            if graph[i][j] == 'F': ans += 1

print(ans)