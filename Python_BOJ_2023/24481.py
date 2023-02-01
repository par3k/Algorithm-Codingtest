# dfs3
import sys
sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline()

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    graph[node].sort()
    for next_node in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[node] + 1
            dfs(next_node)

visited[start] = 0
dfs(start)

for val in visited[1:]:
    print(val)