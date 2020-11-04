# 아기 상어
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    global cnt, shark_size, start_point, answer

    queue = deque()
    queue.append([x, y])

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    food = []
    state = False
    level = 0

    while queue:
        level += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if graph[nx][ny] == 0 or graph[nx][ny] == shark_size:
                        queue.append([nx, ny])
                    elif 0 < graph[nx][ny] < shark_size:
                        food.append([nx, ny])
                        state = True

        if state: break

    if state:
        food.sort(key=lambda x: [x[0], x[1]])

        graph[food[0][0]][food[0][1]] = 9
        graph[start_point[0]][start_point[1]] = 0
        start_point = food[0]

        cnt += 1
        answer += level

        if cnt == shark_size:
            shark_size += 1
            cnt = 0
    else: pass
    return state


n = int(input())
graph = list()

cnt, shark_size, start_point, answer = 0, 2, 0, 0

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

    for j, e in enumerate(data):
        if e == 9:
            start_point = [i, j]

while True:
    condition = bfs(start_point[0], start_point[1])
    if not condition: break

print(answer)