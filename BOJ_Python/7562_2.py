# 나이트의 이동
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()
dx, dy = [2, 1, -2, -1, 2, 1, -2, -1], [1, 2, 1, 2, -1, -2, -1, -2]

def bfs(x, y, xx, yy):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()

        if x == xx and y == yy:
            print(graph[xx][yy] - 1)
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    bfs(start_x, start_y, end_x, end_y)