# DFS
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
visited = [0] * (n + 1)
visited[r] = 1

def dfs(now):
    global cnt
    graph[now].sort()
    for next in graph[now]:
        if not visited[next]:
            cnt += 1
            visited[next] = cnt
            dfs(next)

dfs(r)
print(visited)