# 이분 그래프
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


def bfs(v, visited, color):
    queue = deque([v])
    visited[v] = True
    color[v] = 1

    while queue:
        now = queue.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                queue.append(nxt)
                color[nxt] = 3 - color[now]
                visited[nxt] = True
            else:
                if color[now] == color[nxt]:
                    return False
    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    color = [0 for _ in range(v + 1)]
    flag = True
    for i in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for node in range(1, v + 1):
        if not visited[node]:
            if not bfs(node, visited, color):
                flag = False
                break

    if not flag: print("NO")
    else: print("YES")