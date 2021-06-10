# DFS와 BFS
from collections import deque
import sys
sys.setrecursionlimit(1000001)
input = lambda :sys.stdin.readline().rstrip()

m, n, v = map(int, input().split())
graph = [[] for _ in range(m + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def dfs(node):
    visited[node] = 1
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


visited = [0 for _ in range(m + 1)]
dfs(v)
print()
visited = [0 for _ in range(m + 1)]
bfs(v)