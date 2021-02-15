# 바이러스 - dfs
from collections import deque

node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    cnt = 0
    will_visit = deque([1])

    while will_visit:
        start = will_visit.popleft()
        if visited[start] == False:
            visited[start] = True
            cnt += 1

            for i in graph[start]:
                if visited[i] == False:
                    will_visit.append(i)

    return cnt - 1

print(bfs())