# 유기농 배추

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]


def dfs (y, x):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny, nx)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * (m+1) for _ in range(n+1)]
    visited = [[False] * (m+1) for _ in range(n+1)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and not visited[a][b]:
                cnt += 1
                dfs(a, b)

    print(cnt)




