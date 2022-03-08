# 미로 탐색
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs()
print(visited[n - 1][m - 1])