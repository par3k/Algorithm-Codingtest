# 양
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

wolf, sheep = 0, 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y, animal):
    global wolf, sheep
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    w, s = 0, 0

    if animal == 'v': w += 1
    elif animal == 'o': s += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] != '#':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

                    if graph[nx][ny] == 'v': w += 1
                    elif graph[nx][ny] == 'o': s += 1

    if w >= s: wolf += w
    elif s > w: sheep += s


for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            bfs(i, j, graph[i][j])

print(sheep, wolf)