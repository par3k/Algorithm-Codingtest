# DFS와 BFS
from collections import deque

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]


for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = [False] * (node + 1)


def dfs(graph, start, dfs_visited):
    dfs_visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if dfs_visited[i] == False:
            dfs_visited[i] = True
            dfs(graph, i, dfs_visited)


bfs_visited = [False] * (node + 1)


def bfs(graph, start, bfs_visited):
    bfs_visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if bfs_visited[i] == False:
                queue.append(i)
                bfs_visited[i] = True



dfs(graph, start, dfs_visited)
print()
bfs(graph, start, bfs_visited)