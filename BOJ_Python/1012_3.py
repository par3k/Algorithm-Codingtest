# 유기농 배추
import sys
sys.setrecursionlimit(10001)
input = lambda :sys.stdin.readline().rstrip()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k): # 배추 좌표에 배추를 1로 표시
        y, x = map(int, input().split())
        graph[x][y] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                answer += 1
                dfs(i, j)

    print(answer)