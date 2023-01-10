# dfs2

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
def dfs(node):
    global cnt
    visited[node] = cnt
    graph[node].sort(reverse=True)
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt += 1
            dfs(next_node)

dfs(r)
for val in visited[1:]:
    print(val)