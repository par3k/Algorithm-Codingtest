# 다리만들기
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans, k = 10 ** 9, 1


def dfs(x, y):
    visited[x][y] = True
    graph[x][y] = k
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny]:
                dfs(nx, ny)


def bfs(z):
    global ans
    distance = [[-1] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == z:
                queue.append((i, j))
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] and graph[nx][ny] != z:
                    ans = min(ans, distance[x][y])
                    return

                if not graph[nx][ny] and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            k += 1

for i in range(1, k + 1):
    bfs(i)

print(ans)