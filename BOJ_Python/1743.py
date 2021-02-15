# 음식물 피하기
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = [['.' for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = '#'


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt


for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == '#':
            ans = max(ans, bfs(x, y))
print(ans)