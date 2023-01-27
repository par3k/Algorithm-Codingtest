# 미로 탐색

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        visited[nx][ny] = visited[xx][yy] + 1
                        queue.append((nx, ny))

bfs(0, 0)
print(visited[n - 1][m - 1])