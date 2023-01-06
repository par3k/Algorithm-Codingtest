# BFS
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)
cnt = 1

def bfs():
    global cnt
    queue = deque()
    queue.append((r))
    visited[r] = 1

    while queue:
        now_node = queue.popleft()
        graph[now_node].sort()
        for next_node in graph[now_node]:
            if not visited[next_node]:
                cnt += 1
                visited[next_node] = cnt
                queue.append((next_node))

bfs()

for val in visited[1:]:
    print(val)