#  바이러스
import sys
input = lambda: sys.stdin.readline()

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = 0
visited = [0] * (n + 1)

def dfs(node):
    global ans
    visited[node] = 1
    graph[node].sort()
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            ans += 1

dfs(1)
print(ans)