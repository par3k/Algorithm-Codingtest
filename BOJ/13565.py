import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()
        if x == m - 1:
            print("YES")
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    print("NO")


queue = deque()
for i in range(n):
    if graph[0][i] == 0:
        queue.append((0, i))
        visited[0][i] = True
bfs()