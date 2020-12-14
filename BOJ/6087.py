# 레이저 통신
import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
graph = [list(input()) for _ in range(h)]
mirror = [[] for _ in range(h)]
C = []

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            C.append([i, j])
        if graph[i][j] != '*':
            mirror[i].append(-1)
        else:
            mirror[i].append(graph[i][j])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    mirror[x][y] = 0
    while q:
        x, y,  = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < h and 0 <= ny < w:
                if mirror[nx][ny] == '*':
                    break
                if mirror[nx][ny] == -1:
                    mirror[nx][ny] = mirror[x][y] + 1
                    q.append([nx, ny])
                nx += dx[i]
                ny += dy[i]


bfs(C[0][0], C[0][1])
print(mirror[C[1][0]][C[1][1]] - 1)