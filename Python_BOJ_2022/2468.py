# 안전 영역
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# O(n ^ 2)
def dfs(x, y, height):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > height:
                dfs(nx, ny, height)

ans = -9999
# O(n ^ 3)
for h in range(0, 101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                visited[i][j] = True
                cnt += 1
                dfs(i, j, h)
    ans = max(ans, cnt)
print(ans)
                