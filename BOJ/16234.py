# 인구 이동
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append([i, j])

    tmp = list()
    tmp.append([i, j])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if l <= abs(A[nx][ny] - A[x][y]) <= r:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                        tmp.append([nx, ny])
    return tmp


cnt = 0
while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                tmp = bfs(i, j)
                print(tmp)

                if len(tmp) > 1:
                    flag = True
                    num = sum([A[x][y] for x, y in tmp]) // len(tmp)

                    for x, y in tmp:
                        A[x][y] = num
    if not flag: break
    cnt += 1

print(cnt)