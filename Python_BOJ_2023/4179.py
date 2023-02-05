# 불!
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

def fire_spread():
    fqlen = len(fire_queue)
    while fqlen:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'F'
                    fire_queue.append(((nx, ny)))
        fqlen -= 1

def find_exit(x, y):
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
                else:
                    print(visited[x][y])
                    return
            qlen -= 1
        fire_spread()

    print("IMPOSSIBLE")
    return

queue, fire_queue = deque(), deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            s_x, s_y = i, j
            graph[i][j] = '.'
        elif graph[i][j] == 'F':
            fire_queue.append((i, j))

fire_spread()
find_exit(s_x, s_y)