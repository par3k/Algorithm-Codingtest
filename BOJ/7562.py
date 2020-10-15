# 나이트의 이동
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]


def bfs(x, y, p, q):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == p and y == q:
            print(visited[p][q] - 1)
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[0 for _ in range(n)] for _ in range(n)]

    bfs(start_x, start_y, end_x, end_y)