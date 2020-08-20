from collections import deque

node, edge, start = map(int, input().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()


visited = [False] * (node + 1)


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

bfs(graph, start, visited)