import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
graph = [list(input().upper()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y, visited):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


queue = deque()
visited = [[False] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            ans += 1

queue = deque()
visited2 = [[False] * n for _ in range(n)]
ans_2 = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, visited2)
            ans_2 += 1

print(ans, ans_2)