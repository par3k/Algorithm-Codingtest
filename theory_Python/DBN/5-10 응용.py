# 다른 dfs 로 풀기

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs(nx, ny)


for a in range(n):
    for b in range(m):
        if graph[a][b] == 0 and not visited[a][b]:
            ans += 1
            dfs(a, b)

print(ans)