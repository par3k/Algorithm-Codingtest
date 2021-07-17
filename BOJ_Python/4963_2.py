# 섬의 갯수
import sys
input =lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)
dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == h == 0: break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)