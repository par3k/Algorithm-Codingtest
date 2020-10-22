# 안전영역
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > h:
                dfs(nx, ny, h)


ans = 1
for depth in range(0, 101):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > depth and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j, depth)
    ans = max(ans, cnt)

print(ans)