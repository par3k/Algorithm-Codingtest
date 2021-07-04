# DOM
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n, m, p = map(int, input().split())
graph = [[] for _ in range(m + 1)]
visited = [[] for _ in range(m + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[b].append(a)
    visited[b].append(0)


def bfs(ch):
    queue = deque()
    queue.append(ch)
    cnt = 0
    while queue:
        cur = queue.popleft()
        for i in range(len(graph[cur])):
            if graph[cur][i] != 0 and visited[cur][i] == 0:
                queue.append(graph[cur][i])
                visited[cur][i] = 1
                cnt += 1
                break
            if visited[cur][i] == 1:
                return -1
    return cnt


print(bfs(p))