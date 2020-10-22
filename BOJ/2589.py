# 보물섬
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

L, W = map(int, input().split())
graph = [input() for _ in range(L)]
visited = [[False] * W for _ in range(L)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    distance = 0
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= L or ny >= W: continue
            if graph[nx][ny] == 'L' and not visited[nx][ny]:
                queue.append((nx, ny, d+1))
                visited[nx][ny] = True
                distance = d + 1
    return distance


ans = 0

for i in range(L):
    for j in range(W):
        if graph[i][j] == 'L':
            visited = [[False] * W for _ in range(L)]
            ans = max(ans, bfs(i, j))

print(ans)