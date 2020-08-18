# DFS와 BFS
import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node + 1)]


for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

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