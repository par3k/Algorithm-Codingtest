# 미로탈출
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue

            if graph[new_x][new_y] == 0:
                continue

            if graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append((new_x, new_y))

    return graph[n-1][m-1]


print(bfs(0, 0))


