# bfs 3
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(node):
    queue = deque()
    queue.append((node))
    visited[node] = 1
    while queue:
        xnode = queue.popleft()
        for nnode in graph[xnode]:
            if not visited[nnode]:
                visited[nnode] = visited[xnode] + 1
                queue.append((nnode))

bfs(r)

for i in range(1, n + 1):
    print(visited[i] - 1)