# 그림
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans, ans_cnt = 0, 0


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
    return size


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            ans_cnt += 1
            ans = max(ans, bfs(i, j))


print(ans_cnt)
print(ans)