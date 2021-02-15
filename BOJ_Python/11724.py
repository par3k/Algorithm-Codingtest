# 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

ans = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)