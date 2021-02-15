# 불
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


def fire():
    fqlen = len(fire_queue)
    while fqlen:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    fire_queue.append((nx, ny))
        fqlen -= 1


def bfs(i, j):
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        qlen = len(queue)
        while qlen:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if graph[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    print(visited[x][y])
                    return
            qlen -= 1
        fire()
    print("IMPOSSIBLE")
    return


for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue, fire_queue = deque(), deque()

    for x in range(h):
        for y in range(w):
            if graph[x][y] == '@':
                start_x, start_y = x, y
                graph[x][y] = '.'
            if graph[x][y] == '*':
                fire_queue.append((x, y))
    fire()
    bfs(start_x, start_y)