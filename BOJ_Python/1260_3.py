# DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(1000001)
input = lambda :sys.stdin.readline().rstrip()

n, m, v = map(int, input().split()) # 정점의 갯수, 간선의 갯수, 시작할 정점 번호
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append((to_))
    graph[from_].sort()
    graph[to_].append((from_))
    graph[to_].sort()
visited = [0] * (n + 1)


def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


dfs(v)
print()
visited = [0] * (n + 1)


def bfs(start):
    queue = deque()
    queue.append((start))
    while queue:
        x = queue.popleft()
        visited[x] = 1
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                queue.append((i))
                visited[i] = 1


bfs(v)