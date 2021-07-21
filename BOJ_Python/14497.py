# 주난의 난
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == '1' or graph[nx][ny] == '#':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] == '0':
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))


bfs(x1 - 1, y1 - 1)
print(visited[x2 - 1][y2 - 1])