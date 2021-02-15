# 적록색약
import sys
sys.setrecursionlimit(10001)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [list(input().upper()) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, type, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if type == 0 and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny, 0, visited)
            elif type == 1 and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny, 1, visited)


visited = [[False] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 0, visited)
            ans += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


visited2 = [[False] * n for _ in range(n)]
ans_2 = 0

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            dfs(i, j, 1, visited2)
            ans_2 += 1

print(ans, ans_2)