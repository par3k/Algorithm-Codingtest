# 현수막
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

ans = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            ans += 1

print(ans)