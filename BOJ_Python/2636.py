# 치즈
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
left = 0

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            left += 1


def bfs(left):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True

                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    left -= 1
                else:
                    queue.append([nx, ny])
    return left


def remove():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 0


queue = deque()
cnt = 0
tmp = left

while left != 0:
    visited = [[False] * m for _ in range(n)]
    queue.append([0, 0])
    visited[0][0] = True
    left = bfs(left)
    if left != 0:
        tmp = left
    cnt += 1
    remove()

print(cnt)
print(tmp)