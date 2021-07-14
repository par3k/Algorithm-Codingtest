# 토마토
from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


queue = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == -1:
            visited[i][j] = -1
bfs()

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            print(-1)
            exit(0)

answer = -123456789
for i in range(m):
    for j in range(n):
        answer = max(visited[i][j], answer)
print(answer - 1)
