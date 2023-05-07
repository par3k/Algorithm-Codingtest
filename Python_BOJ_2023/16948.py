# 데스 나이트
from collections import deque

n = int(input())
sx, sy, ex, ey = map(int, input().split())

graph = [[0] * n for _ in range(n)]

dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


bfs(sx, sy)
print(graph[ex][ey] - 1)