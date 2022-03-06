# 내리막 길
import sys
sys.setrecursionlimit(10 ** 5)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

# 이 알고리즘의 경우 TO가 난다.
# DFS + DP를 이용

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] < graph[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

print(dfs(0, 0))