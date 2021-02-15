# 소수 경로
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

arr = [1 for _ in range(10000)]


def eratosthenes():
    for i in range(2, 100):
        if arr[i] == 1:
            for j in range(i, 10000, i):
                arr[j] = 0


def bfs(x):
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        if x == y:
            print(visited[x] - 1)
            return
        for i in range(10):
            if i != 0:
                nx = (x % 1000) + i * 1000
                if arr[nx] == 1 and visited[nx] == 0:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

            nx = int(x / 1000) * 1000 + (x % 100) + i * 100
            if arr[nx] == 1 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

            nx = int(x / 100) * 100 + (x % 10) + i * 10
            if arr[nx] == 1 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

            nx = int(x / 10) * 10 + i
            if arr[nx] == 1 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)


eratosthenes()
T = int(input())
for _ in range(T):
    queue = deque()
    visited = [0 for _ in range(10000)]
    x, y = map(int, input().split())
    bfs(x)