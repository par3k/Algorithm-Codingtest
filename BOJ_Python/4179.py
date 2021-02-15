# 불 !
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def fire():
    fqlen = len(fire_queue)
    while fqlen:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'F'
                    fire_queue.append((nx, ny))
        fqlen -= 1


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        qlen = len(queue)
        while qlen:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if not visited[nx][ny] and graph[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= r or ny >= c:
                    print(visited[x][y])
                    return
            qlen -= 1
        fire()
    print("IMPOSSIBLE")
    return


queue, fire_queue = deque(), deque()
for x in range(r):
    for y in range(c):
        if graph[x][y] == 'J':
            start_x, start_y = x, y
            graph[x][y] = '.'
        if graph[x][y] == 'F':
            fire_queue.append((x, y))

fire()
bfs(start_x, start_y)