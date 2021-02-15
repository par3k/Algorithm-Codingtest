# 탈출
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int ,input().split())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue, w_queue = deque(), deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def water():
    wq_len = len(w_queue)
    while wq_len:
        x, y = w_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    w_queue.append([nx, ny])
        wq_len -= 1


def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        q_len = len(queue)
        while q_len:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])
                    elif graph[nx][ny] == 'D':
                        print(visited[x][y])
                        return
            q_len -= 1
        water()
    print('KAKTUS')
    return


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            x1, y1 = i, j
            graph[i][j] = '.'
        elif graph[i][j] == '*':
            w_queue.append([i, j])

water()
bfs(x1, y1)