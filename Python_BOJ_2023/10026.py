# 적록색약
import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    dfs(nx, ny)

ans = 0
visited = [[False] * n for _ in range(n)] # 정상시 용 초기화
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            ans += 1

for i in range(n): # 그래프를 색맹용으로 바꾸기
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

ans2 = 0
visited = [[False] * n for _ in range(n)] # 색맹용 초기화
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            ans2 += 1

print(ans, ans2)