# 스타트링크
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

F, S, G, U, D = map(int, input().split())
graph = [-1 for _ in range(F)]
graph[S-1] = 0
visited = [False] * (F + 1)
dy = [U, -D]


def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        y = queue.popleft()

        for i in range(2):
            ny = y + dy[i]
            if 0 <= ny < F and not visited[ny]:
                queue.append(ny)
                graph[ny] = graph[y] + 1
                visited[ny] = True


bfs(S-1)
print(graph[G-1] if graph[G-1] != -1 else 'use the stairs')