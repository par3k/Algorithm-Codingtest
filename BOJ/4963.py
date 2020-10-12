# 섬의 갯수
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1 ,1, 0, -1, -1, -1]


def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if nx >= h or nx < 0 or ny >= w or ny < 0:
            continue

        if not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    graph = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False] * w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)