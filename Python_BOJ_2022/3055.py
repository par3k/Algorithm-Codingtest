# 탈출
from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
hog, water = deque(), deque()

def spread_water():
    wq_len = len(water)
    while wq_len:
        x, y = water.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water.append((nx, ny))
        wq_len -= 1

def bfs():
    while hog:
        hq_len = len(hog)
        while hq_len:
            x, y = hog.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if  0 <= nx < n and 0 <= ny < m:
                    if not visit[nx][ny] and graph[nx][ny] == '.':
                        visit[nx][ny] = visit[x][y] + 1
                        hog.append((nx, ny))
                    elif graph[nx][ny] == 'D':
                        print(visit[x][y])
                        return
            hq_len -= 1
        spread_water()
    print("KAKTUS")
    return


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            hog.append((i, j))
            visit[i][j] = 1
            graph[i][j] = '.'
        elif graph[i][j] == '*':
            water.append((i, j))

spread_water()
bfs()