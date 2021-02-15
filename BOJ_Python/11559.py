# 뿌요뿌요
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

graph = [['.' for _ in range(12)] for _ in range(6)]
visited = [[False] * 12 for _ in range(6)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

combo = 0

for j in range(11, -1, -1):
    data = input()
    for i in range(6):
        graph[i][j] = data[i]


def bfs(x, y):
    queue, location = deque(), list()

    color = graph[x][y]
    visited[x][y] = True
    cnt = 1

    queue.append([x, y])
    location.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = True
                cnt += 1
                queue.append([nx, ny])
                location.append([nx, ny])

    if cnt >= 4:
        for i in location:
            graph[i[0]][i[1]] = '#'
        return True
    return False


def search():
    flag = False
    i = 0
    while i < 6:
        j = 0
        while j < 12:
            if graph[i][j] != '.' and not visited[i][j]:
                if bfs(i, j): flag = True
            j += 1
        i += 1
    return flag


def delete():
    i = 0
    while i < 6:
        j = 0
        while j < 12:
            visited[i][j] = False
            if graph[i][j] == '#':
                graph[i].pop(j)
                graph[i].append('.')

                visited[i].pop(j)
                visited[i].append(False)
                continue
            j += 1
        i += 1


while True:
    state = search()
    if not state:
        break
    else:
        delete()
        combo += 1
print(combo)