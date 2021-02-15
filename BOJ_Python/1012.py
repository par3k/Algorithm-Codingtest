# 유기농 배추

import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[0] * (m+1) for _ in range(n+1)]
    visited = [[False] * (m+1) for _ in range(n+1)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1 and not visited[a][b]:
                cnt += 1
                dfs(a, b)

    print(cnt)