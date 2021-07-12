# 전쟁 - 전투
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(3000000)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
w, b = 0, 0


def dfs(x, y, cnt):
    soldier_color = graph[x][y]
    graph[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == soldier_color:
                cnt = dfs(nx, ny, cnt + 1)
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            w += dfs(i, j, 1) ** 2
        elif graph[i][j] == 'B':
            b += dfs(i, j, 1) ** 2

print(w, b)