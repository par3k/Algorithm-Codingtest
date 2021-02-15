# 인접 리스트 방식으로 구현

from collections import deque

node, edge, start = map(int, input().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

visited = [False] * (node + 1)

bfs(graph, start, visited)