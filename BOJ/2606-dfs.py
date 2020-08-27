# 바이러스 - dfs

node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

for _ in range(edge):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start_node):
    global cnt
    cnt += 1
    visited[start_node] = True

    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)

    return cnt - 1


print(dfs(1))