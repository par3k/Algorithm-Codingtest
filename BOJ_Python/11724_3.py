# 연결 요소의 개수 dfs
import sys
sys.setrecursionlimit(10000)
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)