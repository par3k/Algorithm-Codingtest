# 미로 2
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    global ans
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        q = queue.popleft()
        for i in range(4):
            nx, ny = q[0] + dx[i], q[1] + dy[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and not visited[nx][ny] and graph[nx][ny] != 1:
                if graph[nx][ny] == 3:
                    ans = 1
                    return
                visited[nx][ny] = True
                queue.append([nx, ny])


for _ in range(1,11):
    t = int(input())
    graph = list()

    for i in range(100):
        line = list(map(int, list(input().strip())))
        graph.append(line)

    visited = [[False] * 100 for _ in range(100)]
    ans = 0

    queue = deque()
    bfs(1, 1)
    print(f'#{t} {ans}')