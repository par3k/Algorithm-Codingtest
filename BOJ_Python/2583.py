# 영역 구하기
import sys
sys.setrecursionlimit(10001)
input = lambda : sys.stdin.readline().rstrip()

m, n, k = map(int,input().strip().split())
graph = [[0] * n for i in range(m)]
visited = [[False] * n for i in range(m)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(k):
    x1, y1, x2, y2 = map(int,input().strip().split())
    for x in range((m - y2), (m - y1), 1):
        for y in range(x1, x2, 1):
            graph[x][y] = 1


def dfs(x, y):
    global val
    val += 1
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs(nx, ny)


ans = []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 0:
            val = 0
            dfs(i, j)
            ans.append(val)

print(len(ans))
for i in sorted(ans):
    print(i, end=" ")