# 안전 영역
from collections import deque
import sys
input = lambda: sys.stdin.readline()
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(graph))

answer = list()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

def decreasing_height():
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                graph[i][j] -= 1

while max_height > 0:
    visited = [[False] * n for _ in range(n)]
    cnt_building = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > 0:
                bfs(i, j)
                cnt_building += 1
    
    answer.append(cnt_building)
    max_height -= 1
    decreasing_height()

print(max(answer))