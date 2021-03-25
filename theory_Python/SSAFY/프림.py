n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
edgeList = [int(1e9)] * n
ans = 0
edgeList[0] = 0

for i in range(n):
    min = int(1e9)
    minVertex = 0

    for a in range(n):
        if not visited[a] and min > edgeList[i]:
            min = edgeList[i]
            minVertex = i

    ans += min
    visited[minVertex] = True

    for b in range(n):
        if not visited[b] and graph[minVertex][b] != 0 and edgeList[b] > graph[minVertex][b]:
            edgeList[b] = graph[minVertex][b]

print(ans)

# 5
# 0 5 10 15 30
# 5 0 7 12 20
# 10 7 0 0 0
# 15 12 0 0 0
# 30 20 0 0 0