# 24482 dfs-4
import sys
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

cnt = 0
answer = [-1] * n

def dfs(v):
    global cnt
    visited[v] = True
    answer[v] = cnt

    graph[v].sort(reverse=True)
    for new_one in graph[v]:
        if not visited[new_one]:
            visited[new_one] = True
            cnt += 1
            dfs(new_one)

dfs(r - 1)
print(answer)