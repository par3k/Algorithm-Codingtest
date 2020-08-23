# 다른 dfs 로 풀기

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]


def dfs(y, x):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and graph[ny][nx] == 0:
                dfs(ny, nx)


n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
ans = 0

for _ in range(n):
    graph.append(list(map(int, input())))

for a in range(n):
    for b in range(m):
        if graph[a][b] == 0 and not visited[a][b]:
            ans += 1
            dfs(a, b)

print(ans)