# bfs2
from collections import deque
import sys
input = lambda:sys.stdin.readline()

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
def bfs(n):
    global cnt
    visited[n] = 1
    queue = deque()
    queue.append((n))

    while queue:
        node = queue.popleft()
        graph[node].sort(reverse=True)
        for next in graph[node]:
            if not visited[next]:
                cnt += 1
                visited[next] = cnt
                queue.append((next))

bfs(r)
for i in visited[1:]:
    print(i)
