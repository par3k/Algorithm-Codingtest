# 상범 빌딩
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]


def bfs(k, i, j):
    queue = deque()
    queue.append((k, i, j))
    visited[k][i][j] = 0

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                if graph[nz][nx][ny] == 'E':
                    print(f'Escaped in {visited[z][x][y] + 1} minute(s).')
                    return

                if visited[nz][nx][ny] == -1 and graph[nz][nx][ny] == '.':
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append((nz, nx, ny))
    print('Trapped!')


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break

    graph = [[[] * c for _ in range(r)] for _ in range(l)]
    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        graph[i] = [list(input()) for _ in range(r)]
        input()

    for k in range(l):
        for i in range(r):
            for j in range(c):
                if graph[k][i][j] == 'S':
                    bfs(k, i, j)