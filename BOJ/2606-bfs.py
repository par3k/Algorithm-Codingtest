# 바이러스 - dfs

from collections import deque

node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (node + 1)

def bfs():
    cnt = 0
    queue = deque([1])

    while queue:
        v = queue.popleft()

        if visited[v] == False:
            visited[v] = True
            cnt += 1

            for i in graph[v]:
                queue.append(i)
    return cnt - 1

print(bfs())
