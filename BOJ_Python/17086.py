# 아기 상어2
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0, 1, 1, -1, -1], [0, 0, -1, 1, -1, 1, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
shark = deque()


def bfs():
    while shark:
        x, y = shark.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    shark.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append((i, j))

bfs()
max_length = -123456789
for i in range(n):
    for j in range(m):
        max_length = max(max_length, graph[i][j])

print(max_length - 1)