# DFS와 BFS
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    graph[to_].append(from_)

    graph[from_].sort()
    graph[to_].sort()

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

dfs(start)
print()
from collections import deque
visited2 = [False] * (n + 1)
def bfs(node):
    visited2[node] = True
    queue = deque()
    queue.append(node)
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

bfs(start)