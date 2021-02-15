# 결혼식
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y], graph[y][x] = 1, 1


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[a][i] == 1:
                queue.append(i)
                visited[i] = visited[a] + 1


bfs(1)

ans = 0
for i in range(2, n + 1):
    if visited[i] < 4 and visited[i] != 0:
        ans += 1

print(ans)