# DFS와 BFS
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

dfs_visited = [False] * (n + 1)


def dfs(n):
    dfs_visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not dfs_visited[i]:
            dfs(i)

dfs(v)
print()
bfs_visited = [False] * (n + 1)

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        bfs_visited[x] = True
        print(x, end=' ')
        for i in graph[x]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

bfs(v)