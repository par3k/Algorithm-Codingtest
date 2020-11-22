# 치즈 - 안풀려 ㅅㅂ
from collections import deque
import copy
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def air_check(x, y, graph, n, m):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] =- 1
                queue.append((nx, ny))
    return graph


def bfs(graph, n, m):
    cnt = 0
    tmp = copy.deepcopy(graph)
    changes = list()

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                flag = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        if graph[nx][ny] == -1:
                            flag += 1
                if flag >= 2:
                    tmp[x][y] =-1
                    changes.append([x, y])
                    cnt += 1
    return tmp, cnt, changes


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time, cnt2 = 0, 0
graph = air_check(0, 0, graph, n, m)

while True:
    tmp, cnt, changes = bfs(graph, n, m)
    if cnt == 0:
        print(time)
        break
    else:
        graph = tmp

    for i in changes:
        graph = air_check(i[0], i[1], graph, n, m)
    time += 1
    cnt2 = cnt