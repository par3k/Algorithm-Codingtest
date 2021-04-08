# 알고스팟
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]


def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft([nx, ny])
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])

bfs()
print(visited[n - 1][m - 1])